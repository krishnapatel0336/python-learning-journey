# MINI AI CHATBOT
#RULE BASE CHAT ASSISTAN IN PYTHON
import datetime
import time
name= input("welcome,enter your name : ")
presentHour= datetime.datetime.now().hour

if 5<=presentHour<=11:
    print("good morning ,", name)
elif 11<=presentHour<=17:
    print("good afternooon")
elif 17<=presentHour<=20:
    print("good evening")
else :
    print("good night,",name)

COUNT=int(2)
print("\ncountdown starts now")
for i in range(COUNT,0,-1):
    print(i)
    time.sleep(1)




print(" NAMSTE! Welcome to chatbot☺️")
print("You can ask me basic questions, Type 'bye' to exit from the bot")
# memory creation of chatbot (dictionary of responses)
responses ={
    "hello": "hi welcome . how can i help you?",
    "how are you":"i am very fine thank you.",
    "who are you": "i am smart AI chatbot.",
    "motivate me": "keep going. because present efforts only deside your past and future ",
    "happy":"great to here that",
    "what are function in computer": "function are topic of programming language, for detailed information you can checkout chapter 7 of python series by saumya1shingh.",
    "sad":"soory to see this ",
    "bye":"see you again byyyy",
    "who is saumya1singh":"pro  softwear engg...",
}
# function to get response
def getResponseofbot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "i am in learning mode"
# userinput
while True:

    userInput= input("pl. ask your question:")
    reply= getResponseofbot(userInput)
    print("Bot Response :",reply)

    if "bye" in userInput.lower():
        break 
