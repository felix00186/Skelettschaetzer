const fs = require('fs');
const path = require('path');
const { createCanvas, loadImage } = require('canvas');
const posenet = require('@tensorflow-models/posenet');
const tensorflow = require('@tensorflow/tfjs-node');
const { extractFrames, createVideoFromFrames } = require('./ffmpeg-wrapper');

const jointNameMap = {
  'leftShoulder': 'SHOULDER_LEFT',
  'leftElbow': 'ELBOW_LEFT',
  'leftWrist': 'WRIST_LEFT',
  'rightShoulder': 'SHOULDER_RIGHT',
  'rightElbow': 'ELBOW_RIGHT',
  'rightWrist': 'WRIST_RIGHT',
  'leftHip': 'HIP_LEFT',
  'leftKnee': 'KNEE_LEFT',
  'leftAnkle': 'ANKLE_LEFT',
  'rightHip': 'HIP_RIGHT',
  'rightKnee': 'KNEE_RIGHT',
  'rightAnkle': 'ANKLE_RIGHT',
  'leftEye': 'EYE_LEFT',
  'rightEye': 'EYE_RIGHT',
  'nose': 'NOSE',
  'leftEar': 'EAR_LEFT',
  'rightEar': 'EAR_RIGHT'
};

const adjacentKeyPoints = [
  // Arme
  ['leftShoulder', 'leftElbow'],
  ['leftElbow', 'leftWrist'],
  ['rightShoulder', 'rightElbow'],
  ['rightElbow', 'rightWrist'],

  // Beine
  ['leftHip', 'leftKnee'],
  ['leftKnee', 'leftAnkle'],
  ['rightHip', 'rightKnee'],
  ['rightKnee', 'rightAnkle'],

  // Torso
  ['leftShoulder', 'rightShoulder'],
  ['leftHip', 'rightHip'],
  ['leftShoulder', 'leftHip'],
  ['rightShoulder', 'rightHip'],

  // Gesicht
  ['leftEye', 'rightEye'],
  ['leftEye', 'nose'],
  ['rightEye', 'nose'],
  ['leftEar', 'leftEye'],
  ['rightEar', 'rightEye'],
  ['leftEar', 'nose'],
  ['rightEar', 'nose']
];

function drawSkeleton(keypoints, ctx) {
  function getKeypoint(name) {
    return keypoints.find(kp => kp.part === name);
  }

  ctx.strokeStyle = 'lime';
  ctx.lineWidth = 2;

  adjacentKeyPoints.forEach(([p1, p2]) => {
    const kp1 = getKeypoint(p1);
    const kp2 = getKeypoint(p2);
    if (kp1.score > 0.5 && kp2.score > 0.5) {
      ctx.beginPath();
      ctx.moveTo(kp1.position.x, kp1.position.y);
      ctx.lineTo(kp2.position.x, kp2.position.y);
      ctx.stroke();
    }
  });
}

async function runPoseEstimation(videoPath) {
  const filename = path.basename(videoPath, '.mp4');
  const framesDir = `/tmp/${filename}-frames`;
  const outputVideo = `/data/PoseNet/${filename}.mp4`;
  const outputJSON = `/data/PoseNet/${filename}.json`;

  const net = await posenet.load({
    architecture: 'ResNet50',
    outputStride: 16,
    inputResolution: { width: 640, height: 480 },
    quantBytes: 2
  });
  await extractFrames(videoPath, framesDir);

  const frameFiles = fs.readdirSync(framesDir).filter(f => f.endsWith('.png'));
  const output = [];

  for (const file of frameFiles) {
    const fullPath = path.join(framesDir, file);
    const image = await loadImage(fullPath);
    const canvas = createCanvas(image.width, image.height);
    const ctx = canvas.getContext('2d');
    ctx.drawImage(image, 0, 0);

    const input = tensorflow.browser.fromPixels(canvas);
    const pose = await net.estimateSinglePose(input, { flipHorizontal: false });

    // Zeichne Punkte und Skeleton
    ctx.fillStyle = 'red';
    for (const kp of pose.keypoints) {
      if (kp.score > 0.5) {
        ctx.beginPath();
        ctx.arc(kp.position.x, kp.position.y, 3, 0, 2 * Math.PI);
        ctx.fill();
      }
    }

    drawSkeleton(pose.keypoints, ctx);
    fs.writeFileSync(fullPath, canvas.toBuffer('image/png'));

    const jointDict = {};

    for (const kp of pose.keypoints) {
      const mappedName = jointNameMap[kp.part];
      if (mappedName) {
        jointDict[mappedName] = {
          x: kp.position.x/image.width,
          y: kp.position.y/image.height,
          score: kp.score
        };
      }
    }

    // Nur eine Person pro Frame → Liste mit einer Person
    output.push([jointDict]);
  }

  fs.writeFileSync(outputJSON, JSON.stringify(output, null, 2));

  await createVideoFromFrames(framesDir, outputVideo);
}

runPoseEstimation(process.argv[2]);
