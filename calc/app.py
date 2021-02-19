from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route("/add")
# def addd():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     result = add(a,b)
#     return str(result)
operations ={
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}
@app.route('/math/<op>')
def cal(op):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations[op](a,b)
    return str(result)