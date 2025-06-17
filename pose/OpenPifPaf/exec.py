import os
import time
import json
import torch

from openpifpaf import decoder, logger, network, show, visualizer
from openpifpaf.predictor import Predictor
from openpifpaf.stream import Stream
from openpifpaf.plugins.coco import CocoPose

# Konfiguration (konstant oder über Umgebungsvariablen)
INPUT_FOLDER = "/data/input"
OUTPUT_FOLDER = "/data/OpenPifPaf"

# Gerätewahl
device = torch.device('cuda')
pin_memory = True

# Module konfigurieren
class Args:
    def __init__(self):
        self.device = device
        self.pin_memory = pin_memory
        self.decoder_workers = 1
        self.head_metas = None
        self.checkpoint = None
        self.force_complete_pose = False
        self.force_dense_connections = False
        self.seed_threshold = 0.2
        self.instance_threshold = 0.2
        self.keypoint_threshold = 0.05
        self.ablation_pose = None
        self.ablation_decoder = None
        self.headnets = None
        self.decoder = 'caf'
        self.debug = False
        self.dense_connections = None
        self.show_decoder_heatmap = False
        self.show_only_decoded_connections = False
        self.annotation_filter = False
        self.checkpoint_reset_heads = False
        self.share_decode = False
        self.align_pose_heads = False
        self.line_width = 6
        self.dpi = None
        self.output_directory = None
        self.json_output = None
        self.video_output = None
        self.separate_debug_ax = False
        self.disable_cuda = False
        self.debug_indices = []
        self.profile_decoder = False
        self.cif_th = 0.3
        self.caf_th = 0.1
        self.caf_seeds = False
        self.force_complete_caf_th = 0.15
        self.nms_before_force_complete = True
        self.keypoint_threshold_rel = 0.5
        self.greedy = False
        self.connection_method = "cif"
        self.reverse_match = True
        self.ablation_cifseeds_nms = False
        self.ablation_cifseeds_no_rescore = False
        self.ablation_caf_no_rescore = False
        self.xcit_out_channels = [64, 128, 256, 512]
        self.mobilenetv2_pretrained = True
        self.xcit_out_maxpool = True
        self.squeezenet_pretrained = True
        self.resnet_pretrained = True
        self.resnet_pool0_stride = 2
        self.shufflenetv2k_input_conv2_stride = 2
        self.shufflenetv2_pretrained = True
        self.swin_drop_path_rate = 0.1
        self.swin_input_upsample = False
        self.xcit_pretrained = True
        self.swin_use_fpn = True
        self.mobilenetv3_pretrained = True
        self.shufflenetv2k_input_conv2_outchannels = 24
        self.shufflenetv2k_stage4_dilation = 1
        self.shufflenetv2k_kernel = 3
        self.swin_fpn_out_channels = 256
        self.swin_fpn_level = [0, 1, 2, 3]
        self.resnet_input_conv_stride = 2
        self.swin_pretrained = True
        self.shufflenetv2k_conv5_as_stage = False
        self.shufflenetv2k_instance_norm = False
        self.resnet_input_conv2_stride = 1
        self.shufflenetv2k_group_norm = False
        self.shufflenetv2k_leaky_relu = False
        self.resnet_block5_dilation = 1
        self.resnet_remove_last_block = False
        self.cf3_dropout = 0.2
        self.cf3_inplace_ops = True
        self.basenet = os.environ["CHECKPOINT"]
        self.cross_talk = False
        self.download_progress = True
        self.head_consolidation = True
        self.batch_size = 1
        self.fast_rescaling = False
        self.loader_workers = 4
        self.long_edge = 640
        self.save_all = False
        self.show = False
        self.image_width = 640
        self.image_height = 480
        self.image_dpi_factor = 1.0
        self.white_overlay = False
        self.image_min_dpi = 100
        self.show_file_extension = True
        self.show_box = True
        self.show_joint_scales = True
        self.show_joint_confidences = True
        self.show_decoding_order = False
        self.show_frontier_order = False
        self.textbox_alpha = 0.6
        self.text_color = "white"
        self.monocolor_connections = False
        self.skeleton_solid_threshold = 0.3
        self.font_size = 12
        self.video_fps = 30
        self.video_dpi = 100
        self.horizontal_flip = False
        self.scale = 1.0
        self.start_frame = 0
        self.start_msec = 0
        self.crop = None
        self.rotate = 0
        self.max_frames = None

args = Args()
head_metas = [CocoPose()]
decoder.configure(args)
network.Factory.factory(head_metas=head_metas).configure(args)
Predictor.configure(args)
show.configure(args)
Stream.configure(args)
visualizer.configure(args)

# Ordner vorbereiten
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Alle .mp4-Dateien verarbeiten
video_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.mp4')]

for filename in video_files:
    input_path = os.path.join(INPUT_FOLDER, filename)
    base_name = os.path.splitext(filename)[0]

    # Ausgabedateien definieren
    video_out_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.mp4")
    json_out_path = os.path.join(OUTPUT_FOLDER, f"{base_name}.json")

    if os.path.exists(video_out_path):
        os.remove(video_out_path)
    if os.path.exists(json_out_path):
        os.remove(json_out_path)

    # Predictor initialisieren
    predictor = Predictor(visualize_image=True, visualize_processed_image=False)
    capture = Stream(input_path, preprocess=predictor.preprocess)

    annotation_painter = show.AnnotationPainter()
    animation = show.AnimationFrame(
        video_output=video_out_path,
        second_visual=False
    )
    ax, ax_second = animation.frame_init()
    visualizer.Base.common_ax = ax

    last_loop = time.perf_counter()
    for (ax, ax_second), (preds, _, meta) in \
            zip(animation.iter(), predictor.dataset(capture)):
        start_post = time.perf_counter()

        # strukturierte Daten erstellen
        with open(json_out_path, 'a+', encoding='utf8') as f:
            json.dump({
                'frame': meta['frame_i'],
                'predictions': [ann.json_data() for ann in preds]
            }, f, separators=(',', ':'))
            f.write('\n')

        postprocessing_time = time.perf_counter() - start_post
        if animation.last_draw_time is not None:
            postprocessing_time += animation.last_draw_time

        last_loop = time.perf_counter()

print("Alle Videos wurden verarbeitet.")
