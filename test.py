import unittest
from flask import json
from app import app, db
from models import WikiSearch

class WikiSearchAPITestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_wiki_search_count(self):
        payload = {
            "keyword": "Python",
            "limit": 5
        }

        response = self.app.post('/wiki-search-count', json=payload)
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, dict))
        self.assertIn("word1", data)
        self.assertIn("word2", data)
        self.assertIn("word3", data)

    def test_wiki_search_count_limit_exceeds(self):
        payload = {
            "keyword": "Python",
            "limit": 20  # Exceeding limit intentionally
        }

        response = self.app.post('/wiki-search-count', json=payload)
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 500)
        self.assertIn("Limit exceeds word count", data["message"])

    def test_wiki_search_history(self):
        # Add a record to the database for testing
        search_entry = WikiSearch(keyword="Python", results='{"programming": 15, "language": 10, "snake": 5}')
        db.session.add(search_entry)
        db.session.commit()

        response = self.app.get('/wiki-search-history')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["keyword"], "Python")
        self.assertIn("programming", data[0]["results"])
        self.assertIn("language", data[0]["results"])
        self.assertIn("snake", data[0]["results"])

if __name__ == '__main__':
    unittest.main()
