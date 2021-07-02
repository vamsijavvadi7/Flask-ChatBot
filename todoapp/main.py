from flask import Flask,request,render_template,jsonify


app=Flask(__name__)


@app.route("/")
def introduce():#controller
    from .data.about import bot
    return render_template('index.html',
    data=bot,
    question={'key':"name","text":"How may i call you by"})

@app.route("/summary")
def summary():#controller
    from .data.summary import get_summary
    d=get_summary()
    return jsonify(d)



@app.route("/message",methods=['POST'])
def user_message():
    if request.method=='POST':
        from .intents import handle
        return handle(request.form)
    else:
        return "INVALID"

if __name__=="__main__":
    app.run(threaded=True,port=5000)



