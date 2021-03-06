from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body> 
        <form action="/" method="post">
            <label>
                Rotate by:
                <input name="rot" type="text" value="0"></input>                
            </label>
            <textarea name="msg">{0}</textarea>
            <button type="submit">submit</button>
        </form
    </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    print(request)
    rot_amt = int(request.form['rot'])
    stuff = request.form['msg']
    x = rotate_string(stuff, rot_amt)
    return form.format(x)

app.run()

