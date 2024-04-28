from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def d3():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('moviesynopsis.csv')# Replace 'your_file.csv' with your actual file name/path

    df2= pd.read_csv("movielinesDataset.csv")

    lines = df2['cleaned_line'].iloc[:30].astype(str).tolist()

    lemma = df['lemmatized_text'].tolist()

    return render_template('index.html', lines=lines, lemma=lemma)

@app.route('/wordcloud')
def wordcloud():

    df = pd.read_csv('moviesynopsis.csv')  # Replace 'your_file.csv' with your actual file name/path

    df2 = pd.read_csv("movielinesDataset.csv")

    lines = df2['cleaned_line'].iloc[:30].astype(str).tolist()

    lemma = df['lemmatized_text'].tolist()

    return render_template('d3.html', lines=lines, lemma=lemma)

if __name__ == '__main__':
    app.run(debug=True)
