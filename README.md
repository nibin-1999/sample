Django Countries API

A Django REST Framework API that provides country information, including country codes, names, flag URLs, and calling codes. This project demonstrates the integration of Django with external libraries for dynamic data without a database model.

🚀 Features
Country List API: Get a paginated list of all countries.

Search Functionality: Search for countries by name using a query parameter.

Comprehensive Country Data: Each country includes:

Country code (ISO 3166-1 alpha-2)

Country name

Flag image URL (via FlagCDN)

International calling code (via the phonenumbers library)

🛠️ Tech Stack
Django - Web framework

Django REST Framework - API framework

django-countries - Provides country data

phonenumbers - Handles phone number and calling code utilities

🚀 Getting Started
Prerequisites
Python 3.8+

pip (Python package installer)

Installation
Clone the repository:

Bash

git clone <repository-url>
cd <project-directory>
Create and activate a virtual environment:

Bash

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install dependencies:

Bash

pip install django-countries phonenumbers djangorestframework
Configure INSTALLED_APPS:
In your project's settings.py, ensure the following are included:

Python

INSTALLED_APPS = [
    ...
    'rest_framework',
    'django_countries',
    'main', # Your app name
]
Run the development server:

Bash

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

📚 API Endpoints
Get All Countries (Paginated)
HTTP

GET http://127.0.0.1:8000/api/countries/
This endpoint returns a list of 10 countries per page by default.

Pagination example:

HTTP

GET http://127.0.0.1:8000/countries/?page=2
This request retrieves the second page of countries.

Search Countries by Name
HTTP

GET http://127.0.0.1:8000/api/countries/?search=india
This endpoint returns a list of countries whose names contain "india". The search is case-insensitive.

📝 Development Notes
Architectural Decisions
No Database Model: The project uses the django-countries library directly instead of a database model to ensure country data is always current.

External Data Sources:

Flag images are served from a reliable third-party CDN (FlagCDN).

Phone number data is handled by the phonenumbers library.

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Commit your changes (git commit -m 'feat: Add your feature').

Push to the branch (git push origin feature/your-feature).

Open a Pull Request.

