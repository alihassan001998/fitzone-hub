from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")  # index.html me navbar already included

# About Us Page
@app.route("/about")
def about():
    return render_template("about.html")  # navbar already included

# Membership Page
@app.route("/membership")
def membership():
    return render_template("membership.html")  # navbar included here too

if __name__ == "__main__":
    app.run(debug=True)
