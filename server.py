#
# main script for starting server
#

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    templateData = { 'title' : 'Home' }

    # pass the template data into the template index.html and
    # return it to the user
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
