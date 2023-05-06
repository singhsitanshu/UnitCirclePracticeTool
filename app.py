from flask import Flask, render_template, request

unitCircle = {'pi/6':"correct answer", 'pi/4':"correct answer"}

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/input', methods=["POST"])
def getInput():
    user_input1 = request.form.get('input_1')
    user_input2 = request.form.get('input_2')

    if user_input1 == unitCircle['pi/6']:
        result1 = 'true'
    else:
        result1 = 'false'

    if user_input2 == unitCircle['pi/4']:
        result2 = 'true'
    else:
        result2 = 'false'

    return render_template('index.html', result1=result1, result2=result2)

if __name__ == "__main__":
    app.run()