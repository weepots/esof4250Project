# importing needed libraries
from flask import *
from flask_bootstrap import Bootstrap

# configuring flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(app)


# # homepage route
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/login/")
def login():

    return render_template("login.html")


@app.route("/login/", methods=["POST"])
def login_form():
    if request.method == 'POST':
        # demo creds
        creds = {"username": "test", "password": "password"}
        # getting form data
        username = request.form.get("username")
        password = request.form.get("password")

        # authenticating submitted creds with demo creds
        if username == creds["username"] and password == creds["password"]:
            # inform users if creds are valid
            flash("The credentials provided are valid", "success")
            return redirect(url_for("login"))
        else:
            # inform users if creds are invalid
            flash("You have supplied invalid login credentials!", "danger")
            return redirect(url_for("login"))


# running flask server
if __name__ == "__main__":
    app.run(debug=True)
