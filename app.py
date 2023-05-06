from flask import Flask, render_template, request

unitCircle = {'pi/6':"√3/2, 1/2", '':""}

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/input', methods=["POST"])
def getInput():
    user_input = request.form.get('input_1')
    if user_input == unitCircle['pi/6']:
        result = 'true'
    else:
        result = 'false'
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()