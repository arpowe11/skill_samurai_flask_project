from flask import (
    Flask, 
    render_template, 
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("helloWorld.html")













#---------------------------------------#
#   This is the "main" entry point      #   
#   if we are accessing this project    #
#   from this file specifically.        #
#---------------------------------------#
if __name__ == "__main__":
    app.run(debug=True)
    