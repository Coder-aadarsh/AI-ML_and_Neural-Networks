# Real-Time AI Face Landmark Detection
<img src = "https://github.com/aadarsh-nagrath/AI-ML_and_Neural-Networks/assets/92307537/69e76ab2-a11a-460f-9ec6-6b557657a20d" alt ="ss" width ="300px" />
<img src = "https://github.com/aadarsh-nagrath/AI-ML_and_Neural-Networks/assets/92307537/84c737ba-ceb6-4205-ae1e-54e87a4c14fe" alt ="ss" width ="300px" />
<img src = "https://github.com/aadarsh-nagrath/AI-ML_and_Neural-Networks/assets/92307537/35f4ffba-397b-48b0-bf70-50d14537b030" alt ="ss" width ="300px" />

## Overview

This project utilizes TensorFlow.js and the FaceMesh model to achieve real-time face landmark detection in a React application. By integrating these technologies, the application captures facial keypoints through a webcam feed and displays them on an HTML canvas.

## Resources

- TensorFlow.js Models: [TensorFlow.js Models](https://www.tensorflow.org/js/models)
- HTML Canvas: [MDN Web Docs - Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

## Getting Started

1. Create a React app.
2. Install the necessary dependencies:
   - `@tensorflow/tfjs`
   - `@tensorflow-models/facemesh`
   - `react-webcam`

Import React and necessary libraries, including TensorFlow.js, the FaceMesh model, the react-webcam component, and the CSS file for styling.

```javascript
import React, { useRef, useEffect } from 'react';
import * as tf from '@tensorflow/tfjs';
import * as facemesh from '@tensorflow-models/facemesh';
import Webcam from 'react-webcam';
import './App.css';
```

## Application Components

### Define Functional Component
Create the App functional component that will serve as the main application.
Utilize the useEffect hook to run code after the component has mounted. Inside it, load the FaceMesh model and continuously detect faces at a 100ms interval.

```javascript
function App() {
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);

  useEffect(() => {
    const runFacemesh = async () => {
      const net = await facemesh.load();
      setInterval(() => {
        detectFace(net);
      }, 100);
    };
    runFacemesh();
  }, []);
```

### Face Detection Function
Implement the detectFace function, which checks if the webcam is loaded and if so, captures video properties, performs face detection using the FaceMesh model, and draws the facial keypoints on the canvas.

```javascript
const detectFace = async (net) => {
  if (
    typeof webcamRef.current !== 'undefined' &&
    webcamRef.current !== null &&
    webcamRef.current.video.readyState === 4
  ) {
    const video = webcamRef.current.video;
    const videoWidth = video.videoWidth;
    const videoHeight = video.videoHeight;

    video.width = videoWidth;
    video.height = videoHeight;
    canvasRef.current.width = videoWidth;
    canvasRef.current.height = videoHeight;

    const face = await net.estimateFaces(video);
    const ctx = canvasRef.current.getContext('2d');
    drawMesh(face, ctx);
  }
};
```

### Draw Mesh Function
Implement the drawMesh function, which takes the detected faces and draws facial keypoints on the canvas using red circles.

```javascript
const drawMesh = (faces, ctx) => {
  faces.forEach((face) => {
    for (let i = 0; i < face.scaledMesh.length; i++) {
      const x = face.scaledMesh[i][0];
      const y = face.scaledMesh[i][1];

      ctx.beginPath();
      ctx.arc(x, y, 1, 0, 3 * Math.PI);
      ctx.fillStyle = 'red';
      ctx.fill();
    }
  });
};
```

### Render Components
Return the JSX elements for rendering the webcam and canvas components within the App component.

```javascript
return (
  <div className="App">
    <header className='App-header'>
      <Webcam
        ref={webcamRef}
        style={{
          // Webcam styling
        }}
      />

      <canvas
        ref={canvasRef}
        style={{
          // Canvas styling
        }}
      />
    </header>
  </div>
);
}
```

## Utilities.js

This file contains a utility function, `drawPath`, designed to draw a path on the canvas connecting specified points. The function takes a canvas rendering context (`ctx`), an array of points, and a boolean value `closePath` as parameters.

By following these steps, the React application seamlessly integrates TensorFlow.js and FaceMesh to perform real-time face detection, displaying the detected facial keypoints on an HTML canvas.
