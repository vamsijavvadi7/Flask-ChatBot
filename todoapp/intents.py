name=" "
from .movieapi import *
def get_intent(data):
    global name
    m=data['message'].lower()
    if data['key']=='name':
        name=m
        return 'next'
    if data['key']=='movie':
        return 'movieresult'
    if data['key']=='expression':
        return 'expressionres'
    


    
    if any(x in m for x in ["game","play","tic tac toe"]):
        return "game"
    elif any(x in m for x in ["expression","evaluate","calculate","calculations"]):
        return "expression"
    elif "movie" in m:
        return "movie"
    elif "fetch" in m:
        return "fetch"
    else:
        return "echo"


def handle(data):
    global name
    from flask import render_template
   

    intent=get_intent(data)
    if intent =='game':
        return render_template('messages/random.html')
    elif intent == 'next':
         return render_template('messages/greet.html',data={'greet':welcome_Greeting()},name=name,question={'key':'Request','text':'what would you like to do'})
    elif intent == 'movie':
        return render_template('messages/botmsgs.html',name=name,question={'key':'movie','text':'Tell me the movie you wanted to know about'})
    elif intent =='movieresult':
         return render_template('messages/movieres.html',data=movie_Info(data['message']),name=name,question={'key':'Request','text':'what would you like to do'})
    elif intent =='expression':
        return render_template('messages/botmsgs.html',name=name,question={'key':'expression','text':'Enter the expression you want to calculate'})
    elif intent =='expressionres':
        return render_template('messages/expression.html',data=evaluator(data['message']),name=name,question={'key':'Request','text':'what would you like to do'})
    elif data['key'].startswith("random"):
        return render_template('messages/randomgame.html',data=randomnum(),name=name,question={'key':data["key"].split("+")[1],'text':'what would you like to do'})
    elif data["message"].lower()=='bye':
         return render_template('messages/botmsgs.html',name=name,question={'key':'Request','text':'Bye!Have a nice day'})
    else:
        return render_template('messages/botmsgs.html',name=name,question={'key':'Request','text':'Sorry we cannot full fill your request'})

    