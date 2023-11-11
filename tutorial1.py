# Import the Flask class from the flask module
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") that maps to the home function
@app.route("/")
def home():
    # Return a simple HTML response as a string
    return "Hello! This is the main page <h1>Home</h1>"

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run()
