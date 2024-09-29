# File Management API

## Overview

The File Management API is a FastAPI application that allows users to manage files through a secure client-server architecture. It supports user authentication, file uploads, downloads, and listing of uploaded files. The application leverages JSON Web Tokens (JWT) for secure access control.

## Features

- User registration (sign-up)
- User login with token-based authentication
- Upload files to the server
- List uploaded files
- Download files from the server
- Secure file management

## Technologies Used

- FastAPI
- SQLAlchemy
- PostgreSQL (or any other database you choose)
- Python
- JWT (JSON Web Tokens)
- Pydantic for data validation

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A database (e.g., PostgreSQL)


### Clone the Repository

```bash
git clone <repository-url>
cd file-management-api
pip install -r requirements.txt

add .env variables  to your requirements 

-SECRET_KEY=
-ALGORITHM=HS256
-ACCESS_TOKEN_EXPIRE_MINUTES=30
-DATABASE_URL=


# secure-file-sharing/
# ├── main.py                  # Main FastAPI app
# ├── auth.py                  # JWT utility functions for authentication
# ├── models.py                # User and File models for MongoDB
# ├── routes/                  # API route handlers
# │   ├── admin.py             # Admin (Ops User) API routes
# │   └── client.py            # Client API routes
# ├── utils.py                 # Helper utilities (encryption, file handling)
# ├── uploads/                 # Directory for storing uploaded files
# ├── config.py                # Configuration (JWT secrets, DB connection)
# └── requirements.txt         # Python dependencies

Run the Application
bash

uvicorn main:app --reload
The API will be accessible at http://127.0.0.1:8000.

API Endpoints
Authentication
Sign Up

Endpoint: POST /client/signup
Body:
json

{
  "username": "your_username",
  "password": "your_password"
}
Login

Endpoint: POST /client/login
Body:
json

{
  "username": "your_username",
  "password": "your_password"
}
File Management
List Files

Endpoint: GET /client/list-files
Headers:
Authorization: Bearer <access_token>
Upload File

Endpoint: POST /client/upload-file
Headers:
Authorization: Bearer <access_token>
Form Data:
file: (the file to upload)
Download File

Endpoint: GET /client/download-file/{filename}
Headers:
Authorization: Bearer <access_token>
Usage
Sign up for a new account using the sign-up endpoint.
Log in to receive an access token.
Use the access token to perform file management actions (upload, list, download).
Testing
You can use tools like Postman to test the API endpoints. Make sure to set the correct headers and body as specified in the API Endpoints section.

Contributing
If you'd like to contribute to this project, please perform on local machine

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
FastAPI Documentation: https://fastapi.tiangolo.com
SQLAlchemy Documentation: https://docs.sqlalchemy.org
