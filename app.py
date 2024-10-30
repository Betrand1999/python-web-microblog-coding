# from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# from urllib.parse import quote_plus

# app = Flask(__name__)

# # Updated username and properly encoded password
# # username = "betrand1999"
# # password = quote_plus("Cameroon@10KCameroon@10K")  # Encode special characters in the password
# # client = MongoClient(
# #     f"mongodb+srv://{username}:{password}@cluster.7plpy.mongodb.net/microblog?retryWrites=true&w=majority",
# #     tls=True,
# #     tlsAllowInvalidCertificates=True
# # )


# db = client["microblog"]  # Your database name
# entries_collection = db["entries"]  # Use the existing collection

# # Route to display the form
# @app.route("/")
# def home():
#     entries = entries_collection.find({})
#     return render_template("index.html", entries=entries)

# # Route to handle form submission
# @app.route("/submit", methods=["POST"])
# def submit():
#     name = request.form.get("name")
#     email = request.form.get("email")
#     # Insert the submitted data into MongoDB
#     entries_collection.insert_one({"name": name, "email": email})
#     return redirect(url_for("home"))

# if __name__ == "__main__":
#     app.run(debug=True, port=8080)


from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Retrieve MongoDB credentials from environment variables
username = os.getenv("MONGO_USERNAME")
password = quote_plus(os.getenv("MONGO_PASSWORD"))  # Encode special characters
cluster = os.getenv("MONGO_CLUSTER")
db_name = os.getenv("MONGO_DB")

# Initialize MongoDB client
client = MongoClient(
    f"mongodb+srv://{username}:{password}@{cluster}/{db_name}?retryWrites=true&w=majority",
    tls=True,
    tlsAllowInvalidCertificates=True
)

db = client[db_name]
entries_collection = db["entries"]

@app.route("/")
def home():
    entries = entries_collection.find({})
    return render_template("index.html", entries=entries)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    entries_collection.insert_one({"name": name, "email": email})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=8080)
