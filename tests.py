from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Homepage</h1>'

@app.route('/submit', methods=['POST'])
def submit():
    text_input = request.form['text_input']
    return f'<h1>You entered: {text_input}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000