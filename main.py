from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template("home.html")

@app.route("/projects")
def projects():
  return render_template("projects.html")

@app.route("/Ideas")
def ideas():
  return render_template("ideas.html")

if __name__ == "__main__":
    
    app.run(port='3000', host='0.0.0.0')
    app.run(debug=True)