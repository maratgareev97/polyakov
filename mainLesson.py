from flask import Flask, render_template, request
import sqlRequests
import time

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    all = sqlRequests.allSelect()
    radio = ""
    if request.method == "GET" and request.args.get('delete') != None:
        radio = request.args.get('delete')
        sqlRequests.deleteById(radio)
    # for i in all:
    #     print(i.get('id'),i.get('name'),)
    return render_template("index.html", allTable=all, result=radio)


@app.route('/pythonfile', methods=['POST', 'GET'])
def python_subprocess():
    if request.method == "POST":
        pole = request.form['python_file']
        time.sleep(1)
        f = open('test_python.py', 'w')
        f.write(pole)
        f.close()

    return render_template('sobprocess.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
