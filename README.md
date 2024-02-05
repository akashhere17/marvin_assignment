# Wiki Search API

This is a Flask API for searching and retrieving word frequency from Wikipedia using the Wikipedia library. The application stores search history in an SQLite database.

## Getting Started

### Prerequisites

- Python (3.7 or higher)
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/wiki-search-api.git

Navigate to the project directory:

   ```bash
   cd wiki-search-api

Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv

Activate the virtual environment:

On Windows:

   ```bash
   venv\Scripts\activate

On Unix or MacOS:

   ```bash
   source venv/bin/activate

Install dependencies:

   ```bash
   pip install -r requirements.txt

Usage
Run the Flask application:

   ```bash
   python app.py

The API will be accessible at http://localhost:5000.

Access the API endpoints:

Search Wikipedia and count word frequency:

   ```bash
   POST /wiki-search-count

Example Payload:

   ```json
   {
     "keyword": "Python",
     "limit": 5
   }

Retrieve search history from the database:
GET /wiki-search-history

Test the application:

   ```bash
   python -m unittest test_app.py

Database
The application uses an SQLite database (wiki.db) to store search history. The database is created automatically when the application runs.
