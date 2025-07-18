const ffmpeg = require('fluent-ffmpeg');
const path = require('path');
const fs = require('fs');

function extractFrames(inputPath, framesDir) {
  return new Promise((resolve, reject) => {
    if (!fs.existsSync(framesDir)) fs.mkdirSync(framesDir, { recursive: true });

    ffmpeg(inputPath)
      .output(path.join(framesDir, 'frame-%04d.png'))
      .outputOptions('-qscale:v 2')
      .on('end', resolve)
      .on('error', reject)
      .run();
  });
}

function createVideoFromFrames(framesDir, outputPath) {
  return new Promise((resolve, reject) => {
    ffmpeg()
      .addInput(path.join(framesDir, 'frame-%04d.png'))
      .inputOptions('-framerate 25')
      .outputOptions('-pix_fmt yuv420p')
      .save(outputPath)
      .on('end', resolve)
      .on('error', reject);
  });
}

module.exports = {
  extractFrames,
  createVideoFromFrames
};
