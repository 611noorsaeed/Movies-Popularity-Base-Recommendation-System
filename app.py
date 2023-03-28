from flask import Flask, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the popular_df data from the pickled file
with open('popular_movies.pkl', 'rb') as f:
    popular_df = pickle.load(f)

# Sort the data based on the average ratings in descending order and get the top 50 movies
movies = popular_df.sort_values(by='avg_vote', ascending=False)[:50]

# Define a Flask route to render the top 50 movies HTML template
@app.route('/')
def top_movies():
    top_movies = movies.to_dict('records')
    return render_template('home.html', movies=top_movies)

if __name__ == '__main__':
    app.run(debug=True)