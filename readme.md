# Image Watermarking using OpenCV and Flask

This project demonstrates a Python application for adding watermarks to images using OpenCV. Watermarking is crucial for protecting image copyrights and ensuring content security.

## Setting Up the Environment

To set up this project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone (https://github.com/Diksha1312/Image-Watermarking-Using-OpenCV-and-Flask-API
   cd Image-Watermarking-Using-OpenCV-and-Flask-AP


2. **Create and Activate Conda Environment**

   ```bash
   conda create -n env python=3.8
   conda activate env

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt

## Project Overview

### Steps:

1. **Loading Image and Logo from URL:**
   - Images are fetched from URLs using Python requests and then loaded into the application using OpenCV.
   
2. **Resizing and Converting Images:**
   - Images are resized to fit specific dimensions and converted to the RGB format. OpenCV (`cv2`) is used for image processing tasks.
   
3. **Defining Region of Interest (ROI):**
   - The region of interest (ROI) is defined on the image where the watermark (logo or text) will be placed. Coordinates are calculated based on image and logo dimensions.
   
4. **Adding Logo Watermark:**
   - The logo is merged with the image using OpenCV's `cv2.addWeighted()` function. Lines are drawn to mark the placement of the watermark.
   
5. **Adding Text Watermark:**
   - Text watermarking involves using OpenCV to write text on the image. Text properties such as font, color, and position are defined and applied to the image.

## Flask API

The project includes a Flask web application (`app.py`) that allows users to:

- Upload images from their local system.
- Choose between logo or text watermark options.
- View the watermarked image in the browser.
- Clear the form to reset the interface.

### Usage:

1. **Run the Flask Application:**

   ```bash
   python app.py

Access the application at http://localhost:5000 in your web browser.

### Uploading an Image

1. Browse and select an image file to upload.

### Choosing Watermark Type

1. Select either logo or text watermark option.

### Viewing the Watermarked Image

1. After processing, the watermarked image will display on the web interface.
