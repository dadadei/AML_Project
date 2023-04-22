# AML_Project (Web Application)

Project Description:

Title: Document Data Extraction and Confirmation Application

Objective: The primary goal of this application is to enable users to upload images of documents containing either personal or banking information, extract the relevant text from the image using Optical Character Recognition (OCR), and then present the extracted data to the user for confirmation.

Features:

- Document type selection: The application provides an interface for users to choose between uploading personal or banking information documents.

- Image upload: Users can upload an image of the document they wish to process.

- OCR processing: The uploaded image is processed using an OCR algorithm to extract the relevant text from the document.

- Data confirmation: The extracted data is presented to the user in a form based on the selected document type. Users can then confirm the information and submit the form.

- Data storage: The user's confirmed information, image file path, and extracted text are stored in a database for further processing or retrieval.

- Pre-population of form fields: The confirmation form fields can be pre-populated with sample data from a JSON file, making it easier for users to review and confirm the extracted information.

Technologies used:

- Front-end: HTML, CSS, and JavaScript for building user interfaces and handling user interactions.
- Back-end: 
1. Python with Flask as the web framework for handling server-side logic, including image processing and database management.
2. OCR library: Tesseract for Optical Character Recognition to extract text from images.
3. Database: SQLite for storing user information, image file paths, and extracted text.

This application streamlines the process of extracting data from document images and confirming its accuracy, making it an efficient tool for users who need to process personal or banking information quickly and accurately.
