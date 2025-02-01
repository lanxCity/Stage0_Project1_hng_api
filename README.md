# HNG Internship 12 - Stage 0 Backend Task

## Project Overview

This project is a simple public API designed to retrieve basic information as required by the HNG Internship 12 - Stage 0 backend task. The API is built using **Django Rest Framework (DRF)** and provides a fast response time (<500ms).

## Features

- Returns a JSON response containing basic user details
- Supports `GET` requests
- Fast response time
- Deployed for public access

## API Endpoint

### **1. Retrieve User Information**

#### **Request:**

```http
GET /api/profile/
```

#### **Response:**

```json
{
  "slack_name": "Your Name",
  "track": "Backend",
  "github_repo": "https://github.com/yourusername/HNG12-Stage0-Backend",
  "status_code": 200
}
```

## Installation & Setup

### **Prerequisites**

Ensure you have the following installed:

- Python 3.10+
- Django & Django Rest Framework
- Virtual environment (recommended)

### **Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/lanxCity/Stage0_Project1_hng_api
   cd HNG12-Stage0-Backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   .venv\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Django server:
   ```bash
   python manage.py runserver
   ```
5. Access the API at:
   ```
   http://127.0.0.1:8000/api/profile/
   ```

## Deployment

The API can be deployed using **Heroku, Railway, or Render, Pythonanywhere**. Make sure to configure `ALLOWED_HOSTS` and set up the necessary environment variables.

## Testing API Response Time

You can test the API response time using:

```bash
curl -w "Time: %{time_total}s\n" -o /dev/null -s "http://127.0.0.1:8000/api/profile/"
```

## Contributing

Feel free to submit pull requests or issues if you find any bugs or improvements!

## License

This project is licensed under the **MIT License**.

---

**Author:** Abdulramon Sodiq  
**Slack Handle:** `@Lanx`  
**GitHub:** [LanxCity](https://github.com/Lanxcity)
