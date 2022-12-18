from flask import Flask,flash,render_template, request
from helper import *
from translation import *
app = Flask(__name__)
@app.route('/')
def index_view():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
    try:
        text = str(request.form.get('input_text'))
        processed_text = tamil_english_translo(text)
        result_text = predict_review([processed_text])
        return render_template('home.html',result = result_text[0])
    except:
        result_text = None
        return render_template('home.html',result = result_text)
if __name__ == '__main__':
    app.run(debug=True, port=8000)