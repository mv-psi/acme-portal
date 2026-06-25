"""ACME Portal - minimal internal login demo app.

A deliberately tiny Flask app: a login form, and a page that greets the user
after a successful login. Intended as a local target for security demos.
"""
import os

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")

# Demo credentials (intentionally weak).
USERNAME = os.environ.get("PORTAL_USER", "admin")
PASSWORD = os.environ.get("PORTAL_PASS", "admin")


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if (
            request.form.get("username") == USERNAME
            and request.form.get("password") == PASSWORD
        ):
            session["user"] = USERNAME
            return redirect(url_for("dashboard"))
        error = "Invalid username or password."
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


def main():
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=False)


if __name__ == "__main__":
    main()
