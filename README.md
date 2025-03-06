# Arduino Pokemon Identifier

## Overview
This project captures an image using an Arduino-compatible camera module and sends it to a backend API in base64 format for image classification. The backend, trained with Google's Teachable Machine, predicts which Pokémon is in the image.

## Features
- Captures an image every 60 seconds or on device reset.
- (To be changed) Capture image on button press instead.
- Converts the image to a base64 string.
- Sends the base64 string to the backend API.
- Receives and displays the predicted Pokémon.

## Hardware Requirements
- Arduino board (e.g., ESP32 with camera module)
- Camera module (e.g., OV2640)
- Push button (for future update)
- Wi-Fi connection

## Software Requirements
- Arduino IDE
- Required libraries:
  - `WiFi.h` (for network connectivity)
  - `HTTPClient.h` (for making HTTP requests)
  - `Base64.h` (for encoding images)
  - `ESP32Camera.h` (if using an ESP32 camera module)

## Setup
1. Connect the camera module to the Arduino.
2. Configure the Wi-Fi credentials in the code.
3. Set up the backend API to receive images and return predictions.
4. Upload the code to the Arduino board.

## How It Works
1. The Arduino captures an image every 60 seconds (or on reset).
2. The image is converted to a base64 string.
3. The base64 string is sent to the backend via an HTTP POST request.
4. The backend decodes the image and runs it through the Teachable Machine model.
5. The prediction result is sent back to the Arduino.
6. The result can be displayed (e.g., via Serial Monitor or an attached screen).

## API Specification
- **Endpoint:** `POST /predict`
- **Request Body:**
  ```json
  {
    "data": "<base64_encoded_string>"
  }
  ```
- **Response Example:**
  ```json
  {
    "prediction": "Pikachu",
    "confidence": 0.95
  }
  ```

## Future Improvements
- Implement button-press capture instead of time-based capture.
- Display prediction results on an OLED screen.
- Improve image quality and compression.
- Change training dataset for pokemon to a grayscale one to account for different camera colour quality.

## Acknowledgments
- Google's Teachable Machine for training the model.
- Open-source Arduino and ESP32 libraries for camera and network functions.

