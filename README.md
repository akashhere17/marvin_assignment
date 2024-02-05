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

   cd wiki-search-api
Create a virtual environment (optional but recommended):

   python -m venv venv
Activate the virtual environment:

On Windows:

   venv\Scripts\activate
On Unix or MacOS:

   source venv/bin/activate
Install dependencies:

   pip install -r requirements.txt
Usage
Run the Flask application:

   python app.py
The API will be accessible at http://localhost:5000.

Access the API endpoints:

Search Wikipedia and count word frequency:

   POST /wiki-search-count
Example Payload:

json
Copy code
{
  "keyword": "Python",
  "limit": 5
}
Retrieve search history from the database:

sql
Copy code
GET /wiki-search-history
Test the application:

   python -m unittest test_app.py
Database
The application uses an SQLite database (wiki.db) to store search history. The database is created automatically when the application runs.
