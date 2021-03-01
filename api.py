# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:03:22 2021

@author: raha_
"""

import flask
from flask import request, jsonify
import main as m

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    demoText = open("Data/data.txt", "rb").read().decode(encoding="utf-8")
    return """
<h1>Flashcard Generator API</h1>
<h3>Demo:</h3>
<form method="post" action="/api" target="_blank">
    <label for="text">Text to generate flashcards from:</label><br/>
    <textarea id="text" name="text" rows="12" cols="200">{}</textarea><br/><br/>
    <label for="qty">Number of flashcards to generate:</label>
    <input type="text" id="qty" name="qty" value="10" /><br/><br/>
    <input type="submit" value="Generate Flashcards" />
</form>""".format(demoText)
    
@app.route('/api', methods=['POST'])
def api_post():
    text = request.form.get('text')
    qty = request.form.get('qty', 10)
    if text:
        res = m.generateFlashcards(text, qty)
        return jsonify({"status":"success", "flashcards":res})
    else:
        return jsonify({"status":"failed", "msg":"field text can't be empty!"})
    
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# running the app on localhost port 5000
app.run(port=5000)

