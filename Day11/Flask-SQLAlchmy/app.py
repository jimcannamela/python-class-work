from flask import Flask, render_template, request, redirect, url_for
import requests
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app and to instantiate the flask function as app 
app = Flask(__name__)


# # in-memory database for simplicty 
# posts = [{"title": "Post 1", "content": "This is the content of post 1"}, {"title": "Post 2", "content": "This is the content of post 2"}]

# to replace my in-memory database with a real database
# flask sql alchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# this model class can be imported from a different file models.py
# create a model for the database

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


# all of this nasa config can be in a different file 
# and imported into this file
# NASA API configuration
NASA_API_KEY = "DRmrvSEjggbV0PgSlJ44057kSQFFvnvnGJ6y1fkE"
NASA_API_URL = "https://api.nasa.gov/planetary/apod"

def get_nasa_apod(api_key):
    params = {
        "api_key": api_key
    }
    try:
        response = requests.get(NASA_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

# up to this point can be imported from a different file


# view functions ( in the MVT pattern)
# Route to the home page

@app.route('/')
def index():
    # get data from api on index page
    apod_data = get_nasa_apod(NASA_API_KEY)


    # get all the posts from the database
    posts = Post.query.all()
    return render_template('index.html', posts=posts, apod_data=apod_data)



@app.route('/new', methods=['GET', 'POST'])
def new_post():
    # first check if the request method is POST
    if request.method == 'POST':
        # get the title and content from the form 
        title = request.form['title']
        content = request.form['content']
        print("this is my new title", title)
        print("this is my new content", content)
        # create a new post object and put it in our 
        # posts list - -- append the new object 
        # posts.append({"title": title, "content": content})
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        print("this is my updated posts database", new_post)
        # once the object is created redirect to the index page and show us the new post that was created
        return redirect(url_for('index'))
    # if the request method is not POST, then render the new.html template
    return render_template('new_post.html')





if __name__ == '__main__':

    # create the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)