from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def home():
  return render_template("login.html")
  
@app.route("/login", methods=["POST"])
def login():
  user = request.form["nama"]
  pw = request.form["pass"]
  
  file = open("data.txt","a")
  file.write(f"username:{user} | password:{pw}\n")
  file.close()
  return "data tersimpan"

app.run(debug=True)
  