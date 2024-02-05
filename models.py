from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WikiSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #autoincrement id as PK. Not needed for result display
    keyword = db.Column(db.String(500), unique=False, nullable=True)
    results = db.Column(db.String(10000), unique=False, nullable=True)

    def __repr__(self): #to get result in str format
        return f"{self.keyword}: {self.results}"

    def to_json(self): #to jsonify
        return {
            "keyword": self.keyword,
            "results": self.results,
        }