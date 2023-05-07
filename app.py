from flask import Flask, render_template, request

unitCircle = {'0':"correct answer", '30':"correct answer", '45':"correct answer", '60':"correct answer", '90':"correct answer"}

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/input', methods=["POST"])
def getInput():
    user_input1 = request.form.get('input_1')
    user_input2 = request.form.get('input_2')
    user_input3 = request.form.get('input_3')
    user_input4 = request.form.get('input_4')
    user_input5 = request.form.get('input_5')

    if user_input1 == unitCircle['0']:
        result1 = 'true'
    else:
        result1 = 'false'

    if user_input2 == unitCircle['30']:
        result2 = 'true'
    else:
        result2 = 'false'

    if user_input3 == unitCircle['45']:
        result3 = 'true'
    else:
        result3 = 'false'

    if user_input4 == unitCircle['60']:
        result4 = 'true'
    else:
        result4 = 'false'

    if user_input5 == unitCircle['90']:
        result5 = 'true'
    else:
        result5 = 'false'

    return render_template('index.html', result1=result1, result2=result2, result3 = result3, result4=result4, result5=result5)

if __name__ == "__main__":
    app.run()