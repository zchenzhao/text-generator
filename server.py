import flask
from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)

from markov_generator import MarkovGenerator, WordNotFoundError

generator = None
texts = None


@app.route('/welcome', methods=['GET'])
def welcome():
    return 'Welcome to text-generator!', 200


@app.route('/train', methods=['POST'])
def train():
    pass


@app.route('/generate_text', methods=['POST'])
def generate():
    global generator

    data = request.json

    if 'opening_word' in data:
        opening_word = data['opening_word']
    else:
        return 'Must provide opening word', 400

    if not generator:
        texts = [
                '/Users/cindyzhao/Downloads/war-and-peace.txt',
                '/Users/cindyzhao/Downloads/the-mysterious-affair-at-styles.txt',
                '/Users/cindyzhao/Downloads/the-secret-adversary.txt'
            ]
        generator = MarkovGenerator()
        generator.train(texts)

    try:
        generated_text = generator.generate_text(opening_word)
    except WordNotFoundError:
        return 'Opening word not found. Please try a different word.', 400

    return generated_text, 200



if __name__ == '__main__':
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.run(host='localhost', port=5000)