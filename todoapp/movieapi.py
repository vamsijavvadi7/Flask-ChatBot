import random
from datetime import datetime
import requests

# from chatterbot.trainers import ListTrainer

# chatbot=ChatBot('vamsi')
# trainer=ListTrainer(chatbot)


# trainer.train(['hi man','hi vamsi'])
# reponse=chatbot.get_response('hi man')
# print(reponse)
def Greeting():
    #a list of responses from bot
    res=["Nice to see you.\n",
    "\nIts wonderful to see to you.","Great to see you"]
    #to select a response at random and to return that

   
    return random.choice(res)

def randomnum():
    r=[1,2,3,4,5,6,7,8,9,10]
    return random.choice(r)



# greets the person based on the time of the day
def time_Of_The_Day():
    current_time=datetime.now()
    time_Greeting="Good Morning"
    if current_time.hour>21:
        time_Greeting="Good Night"
    elif current_time.hour>16 and current_time.hour<22:
        time_Greeting="Good Evening"
    elif current_time.hour>=12 and current_time.hour<17:
        time_Greeting="Good AfterNoon"
    
    return time_Greeting



#bot welcomes the person with his name 
def welcome_Greeting():
    
    return f"{time_Of_The_Day()},{Greeting()}"





def evaluator(expression):
  
    try:
        return str(eval(expression))
    except Exception as e:
        return "Sry this expression cannot be calculated"



def movie_Info(movie_name):
    
    
    
    try:
        data=requests.get("https://www.omdbapi.com/?t="+str(movie_name)+"&apikey=6637725e").json()
        
    except:
        data={'message':"Movie Not Found"}
    return data




