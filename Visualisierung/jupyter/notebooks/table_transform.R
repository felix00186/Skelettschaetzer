suppressPackageStartupMessages({
  library(dplyr)
  library(tidyr)
  library(stringr)
})

# === Parameter ===
path <- "../data/input/poses.csv"
min.valid.values <- 2

# === Daten laden ===
df <- read.csv(path, header = TRUE)

# === LONG-Format erzeugen ===
df_long <- df %>%
  mutate(frame = META.FRAME_NUMBER) %>%
  pivot_longer(
    cols = starts_with("JOINT."),
    names_to = c("prefix", "software", "joint", "ax"),
    names_sep = "\\."
  ) %>%
  select(frame, software, joint, ax, value)

# === Median pro frame/joint/ax berechnen ===
medians <- df_long %>%
  group_by(frame, joint, ax) %>%
  summarise(
    median = if (sum(!is.na(value)) >= min.valid.values)
      median(value, na.rm = TRUE)
    else
      NA_real_,
    .groups = "drop"
  )

# === Mit Medians verknüpfen und Differenz berechnen ===
df_diff <- df_long %>%
  left_join(medians, by = c("frame", "joint", "ax")) %>%
  mutate(
    diff = value - median,
    diff_name = paste0("JOINT_DIFF.", software, ".", joint, ".", ax),
    median_name = paste0("JOINT_MEDIAN.", joint, ".", ax)
  )

# === Pivot für Mediane ===
df_medians_wide <- df_diff %>%
  select(frame, median_name, median) %>%
  distinct() %>%
  pivot_wider(names_from = median_name, values_from = median)

# === Pivot für Differenzen ===
df_diff_wide <- df_diff %>%
  select(frame, diff_name, diff) %>%
  pivot_wider(names_from = diff_name, values_from = diff)

# === Zusammenführen mit Originaldaten ===
df_result <- df %>%
  left_join(df_medians_wide, by = c("META.FRAME_NUMBER" = "frame")) %>%
  left_join(df_diff_wide, by = c("META.FRAME_NUMBER" = "frame"))

# === Speichern ===
write.csv(df_result, "./cache/data.csv")
invisible(NULL)
