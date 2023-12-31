import React, { useRef, useEffect } from 'react';
import * as tf from '@tensorflow/tfjs';
import * as facemesh from '@tensorflow-models/facemesh';
import Webcam from 'react-webcam';
import './App.css';
import { TRIANGULATION } from './utilities';
import { drawpath } from './utilities';

function App() {
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);

  useEffect(() => {
    const runFacemesh = async () => {
      // Load the FaceMesh model
      const net = await facemesh.load();

      // Continuously detect faces
      setInterval(() => {
        detectFace(net);
      }, 100);
    };

    const detectFace = async (net) => {
      // Check if webcam is loaded
      if (
        typeof webcamRef.current !== 'undefined' &&
        webcamRef.current !== null &&
        webcamRef.current.video.readyState === 4
      ) {
        // Get video properties
        const video = webcamRef.current.video;
        const videoWidth = webcamRef.current.video.videoWidth;
        const videoHeight = webcamRef.current.video.videoHeight;

        // Set video width and height
        webcamRef.current.video.width = videoWidth;
        webcamRef.current.video.height = videoHeight;

        // Set canvas width and height
        canvasRef.current.width = videoWidth;
        canvasRef.current.height = videoHeight;

        // Make face detection
        const face = await net.estimateFaces(video);
        console.log(face);

        // Draw mesh on canvas
        const ctx = canvasRef.current.getContext('2d');
        drawMesh(face, ctx);
      }
    };

    const drawMesh = (faces, ctx) => {
      // Loop through each prediction
      faces.forEach((face) => {
        const keypoints = face.scaledMesh;

        //Lets draw triangles
        for(let i = 0; i < TRIANGULATION.length / 3; i++){
          const points = [
            TRIANGULATION[i * 3],
            TRIANGULATION[i * 3 + 1],
            TRIANGULATION[i * 3 + 2]
          ].map((index) => keypoints[index]);
          drawpath(ctx,points,true);
        }

        // Draw facial keypoints
        for (let i = 0; i < face.scaledMesh.length; i++) {
          const x = face.scaledMesh[i][0];
          const y = face.scaledMesh[i][1];

          ctx.beginPath();
          ctx.arc(x, y, 1, 0, 3 * Math.PI);
          ctx.fillStyle = 'blue';
          ctx.fill();
        }
      });
    };

    runFacemesh();
  }, []);

  return (
    <div className="App">
      <header className='App-header'>
        <Webcam
          ref={webcamRef}
          style={{
            position: 'absolute',
            marginLeft: 'auto',
            marginRight: 'auto',
            left: 0,
            right: 0,
            textAlign: 'center',
            zIndex: 10,
            width: 640,
            height: 480,
          }}
        />

        <canvas
          ref={canvasRef}
          style={{
            position: 'absolute',
            marginLeft: 'auto',
            marginRight: 'auto',
            left: 0,
            right: 0,
            textAlign: 'center',
            zIndex: 10,
            width: 640,
            height: 480,
          }}
        />
      </header>
    </div>
  );
}

export default App;
