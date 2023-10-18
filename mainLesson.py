from flask import Flask, render_template, request
import sqlRequests

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
