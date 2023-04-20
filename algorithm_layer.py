import cv2
import pytesseract
import numpy as np
from PIL import Image

# Function to check image resolution
def check_image_resolution(image, min_width=600, min_height=400):
    width, height = image.size
    return width >= min_width and height >= min_height

# Function to check image quality using blur detection
def check_image_blur(image, threshold=100):
    np_image = np.array(image)
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return laplacian > threshold

# Function to check image quality
def check_image_quality(image):
    image = Image.open(image)
    if not check_image_resolution(image):
        return False, 'Image resolution is too low'
    if not check_image_blur(image):
        return False, 'Image is too blurry'
    return True, ''

# Function to preprocess the image
def preprocess_image(image):
    np_image = np.array(Image.open(image))
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    thresh_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh_image

# Function to perform OCR
def perform_ocr(image):
    text = pytesseract.image_to_string(image)
    return text

# Main function to process the image
def process_image(image):
    quality_status, message = check_image_quality(image)
    if not quality_status:
        return {'status': 'error', 'message': message}

    preprocessed_image = preprocess_image(image)
    text = perform_ocr(preprocessed_image)
import cv2
import pytesseract
import numpy as np
from PIL import Image

# Function to check image resolution
def check_image_resolution(image, min_width=600, min_height=400):
    width, height = image.size
    return width >= min_width and height >= min_height

# Function to check image quality using blur detection
def check_image_blur(image, threshold=100):
    np_image = np.array(image)
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return laplacian > threshold

# Function to check image quality
def check_image_quality(image):
    image = Image.open(image)
    if not check_image_resolution(image):
        return False, 'Image resolution is too low'
    if not check_image_blur(image):
        return False, 'Image is too blurry'
    return True, ''

# Function to preprocess the image
def preprocess_image(image):
    np_image = np.array(Image.open(image))
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    thresh_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh_image

# Function to perform OCR
def perform_ocr(image):
    text = pytesseract.image_to_string(image)
    return text

# Main function to process the image
def process_image(image):
    quality_status, message = check_image_quality(image)
    if not quality_status:
        return {'status': 'error', 'message': message}

    preprocessed_image = preprocess_image(image)
    text = perform_ocr(preprocessed_image)
    return {'status': 'success', 'text': teiiiimport cv2
import pytesseract
import numpy as np
from PIL import Image

# Function to check image resolution
def check_image_resolution(image, min_width=600, min_height=400):
    width, height = image.size
    return width >= min_width and height >= min_height

# Function to check image quality using blur detection
def check_image_blur(image, threshold=100):
    np_image = np.array(image)
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return laplacian > threshold

# Function to check image quality
def check_image_quality(image):
    image = Image.open(image)
    if not check_image_resolution(image):
        return False, 'Image resolution is too low'
    if not check_image_blur(image):
        return False, 'Image is too blurry'
    return True, ''

# Function to preprocess the image
def preprocess_image(image):
    np_image = np.array(Image.open(image))
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    thresh_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh_image

# Function to perform OCR
def perform_ocr(image):
    text = pytesseract.image_to_string(image)
    return text

# Main function to process the image
def process_image(image):
    quality_status, message = check_image_quality(image)
    if not quality_status:
        return {'status': 'error', 'message': message}

    preprocessed_image = preprocess_image(image)
    text = perform_ocr(preprocessed_image)
    return {'status': 'success', 'text': textimport cv2
import pytesseract
import numpy as np
from PIL import Image

# Function to check image resolution
def check_image_resolution(image, min_width=600, min_height=400):
    width, height = image.size
    return width >= min_width and height >= min_height

# Function to check image quality using blur detection
def check_image_blur(image, threshold=100):
    np_image = np.array(image)
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return laplacian > threshold

# Function to check image quality
def check_image_quality(image):
    image = Image.open(image)
    if not check_image_resolution(image):
        return False, 'Image resolution is too low'
    if not check_image_blur(image):
        return False, 'Image is too blurry'
    return True, ''

# Function to preprocess the image
def preprocess_image(image):
    np_image = np.array(Image.open(image))
    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
    thresh_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh_image

# Function to perform OCR
def perform_ocr(image):
    text = pytesseract.image_to_string(image)
    return text

# Main function to process the image
def process_image(image):
    quality_status, message = check_image_quality(image)
    if not quality_status:
        return {'status': 'error', 'message': message}

    preprocessed_image = preprocess_image(image)
    text = perform_ocr(preprocessed_image)
    return {'status': 'success', 'text': text}
x    return {'status': 'success', 'text': text}
