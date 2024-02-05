#import required libraries
from flask import Flask, request
from models import db, WikiSearch
import wikipedia
from collections import Counter
import re

#Initialize your Flask APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wiki.db'
db.init_app(app)

#Helper function to count number of words
def word_frequency_count(data):
    cleaned_data = re.sub('[!,*)@#%(&$_?.^]', '', data) #remove special characters
    split_list = cleaned_data.split(" ")
    counts = dict(Counter(split_list)) #use counter to get count of words from cleaned list
    final_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)) #return result in reversed order of count
    return final_counts

@app.route('/wiki-search-count', methods=['POST'])
def wiki_search_count():
    request_data = request.json
    keyword = request_data["keyword"]
    limit = request_data["limit"]
    page_object = wikipedia.page(keyword, auto_suggest=False, redirect=True, preload=False) #obtain data using the wikipedia library. to overcome error, keep keywords as coded
    result_data = page_object.content #get content in str
    word_counts = word_frequency_count(result_data)
    if limit > len(word_counts):
        raise Exception("Limit exceeds word count") #error handling
    else:
        result = dict(list(word_counts.items())[:limit]) #obtain only N number of words queried by user
        push = WikiSearch(keyword=keyword, results=str(result))
        db.session.add(push) #push data into DB
        db.session.commit()
        return result

@app.route('/wiki-search-history', methods=['GET'])
def wiki_search_history():
    result_data = WikiSearch.query.all() #Get all keywords result from DB
    clean_result = [z.to_json() for z in result_data] #clean data to get jsonified result
    return clean_result


if __name__ == '__main__':
    with app.app_context():
        db.create_all() #create db when app runs
    app.run(debug=False)