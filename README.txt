# Student Library Portal

## Overview
The Student Library Portal is a web application designed to facilitate the management of library resources for students. It allows users to upload, view, and manage PDF documents, providing a user-friendly interface for accessing library materials.

## Features
- User authentication (registration, login, logout)
- Upload and manage PDF documents
- Browse and access library resources
- Responsive design for various devices

## Technologies Used
- **Django**: A high-level Python web framework for building web applications.
- **Python**: The programming language used for backend development.
- **HTML/CSS**: For creating the frontend user interface.
- **SQLite**: The database used for storing user and PDF data.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Student-Library-Portal
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Register a new account or log in with existing credentials.
- Use the interface to upload and manage PDF documents.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License
This project is licensed under the MIT License.

## Git Commands
To manage your changes with Git, use the following commands:
- Check the status of your repository:
  ```bash
  git status
  ```

- Add all changes:
  ```bash
  git add .
  ```

- Commit your changes:
  ```bash
  git commit -m "Your commit message"
  ```

- Push changes to the repository:
  ```bash
  git push
  ```

- If you have uncommitted changes and need to pull updates:
  ```bash
  git stash
  git pull
  git stash pop
