from flask import Flask, render_template

app = Flask(__name__)

@app.route("/brewery")
def brewery():
    return render_template("brewery.html")

if __name__ == "__main__":
    app.run(debug=True)