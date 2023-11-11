# Import the Flask class from the flask module
from flask import Flask, redirect, url_for

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") that maps to the home function
@app.route("/")
def home():
    # Return a simple HTML response as a string
    return "Hello! This is the main page <h1>Home page</h1>"

# Define a route that takes a dynamic parameter 'name'
@app.route("/<name>")
def user(name):
    # Return a personalized greeting with the provided name
    return f"Hello! {name}!.."

# Define a route for the "/admin" URL
@app.route("/admin")
def admin():
    # Redirect to the home page using the url_for function
    return redirect(url_for("user", name="Admin"))

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run()
    