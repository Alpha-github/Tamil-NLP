from flask import Flask, render_template, request
from helper import *
from translation import *
app = Flask(__name__)
@app.route('/')
def index_view():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = tamil_english_rapid(text)
    print(processed_text)
    result_text = predict_review([processed_text])
    return render_template('home.html',result = result_text)
if __name__ == '__main__':
    app.run(debug=True, port=8000)