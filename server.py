# This will be our "server" file where we will set up all of our routes to handle requests.
# You'll want to create a new folder for each assignment moving forward. It will seem tedious at first, but as we 
# add additional files to each project, we'll want to keep everything organized by assignment/project!

# Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
# The "@" decorator associates this route with the function immediately following
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/success')
def success():
  return "success"

# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<name>') 
def hello(name):
    print(name)
    return "Hello, " + name

# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":
    app.run(debug=True)
