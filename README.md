# HNG12 Stage 0 Backend Task  

## Project Overview  
This is a simple public API developed for the HNG12 internship Stage 0 backend task. The API provides basic information, including:  

- The registered email address used in the HNG12 Slack workspace  
- The current datetime in ISO 8601 format (UTC)  
- The GitHub URL of this project's codebase  

## API Documentation  

### Endpoint  
**GET** `<your-deployed-api-url>`  

### Response Format  
The API returns a JSON response with the following structure:  

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Setup Instructions

### Prerequisites
Ensure you have the following installed:

- Python 3.x (or any other supported programming language)
- Git
- A hosting platform

## Running the Project Locally

### 1: Clone the project Repository

Clone the Repository
Clone your FastAPI backend project repository from GitHub or any other version control system.

```bash
git clone https://github.com/SOO2023/HNG0.git

cd HNG0
```

### 2: Create and Activate a Virtual Environment

Create a virtual environment for your project to isolate dependencies.

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 3: Install Dependencies (For Python FastAPI)
```
pip install -r requirements.txt
```

### 4: Start the FastAPI Application with Uvicorn
Run the FastAPI application using Uvicorn.

```bash
uvicorn app.main:app --port 8000
```

### 5: Test the API
Open a browser and make a GET request to: `http://127.0.0.1:8000`

## Additional Resources

- Official FastAPI Documentation: https://fastapi.tiangolo.com/
- Learn More About Python Backend Developers: https://hng.tech/hire/python-developers

## Author

Samson Olaide
GitHub: https://github.com/SOO2023