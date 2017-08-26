# Chatbot
# This is an example program from RP.
# by Chen Hang


import random

randomreplies=["Oh really?",
               "Are you sure about that?",
               "Hmmmmm.",
               "Interesting...",
               "I'm not sure I agree with that...",
               "Definitely!",
               "Maybe!",
               "So what are you saying, exactly?",
               "Meaning what?",
               "You're probably right.",
               "Rubbish! Absolute nonsense!",
               "Anyway, what are your plans for tomorrow?",
               "I was just thinking exactly the same.",
               "That seems to be a popular viewpoint.",
               "A lot of people have been telling me that.",
               "Wonderful!",
               "That could be a bit embarrassing!",
               "Do you really think so?",
               "Indeed...",
               "My point exactly!",
               "Perhaps..."]

chatdictry={"happy":"I'm happy today too!",
            "sad":"Cheer up, mate!",
            "raspberry":"Oh yum! I love raspberries!",
            "computer":"Computers will take over the world! You're already talking to one",
            "music":"Have you heard the new Lana Del Rey album?",
            "art":"But what is art really, anyway?",
            "joke":"How do you kill a circus? Go for the juggler.",
            "jokes":"I only know one joke",
            "very":"Very, very, very!",
            "python":"I hate snakes!",
            "stupid":"Who are you calling stupid, jelly brain?",
            "internet":"87% of statistics on the web are made up. Including that one.",
            "weather":"I wonder if the sun will shine on Saturday?",
            "certain":"How can you be so confident?",
            "talk":"You're all talk! Do something!",
            "think":"You can overthink these things, though.",
            "love":"Up a tree! K-I-S-S-I-N-G!",
            "hate":"That's such a negative emotion. Try to be positive.",
            "hello":"Why, hello to you too, buddy!",
            "wearing":"I don't wear clothes. I don't even come with a case.",
            "future":"Who knows what tomorrow will bring?",
            "tomorrow":"Tomorrow's another day",
            "no":"Not even maybe?",
            "yes":"A healthy positive attitude!",
            "hope":"You've got to keep the hope alive!",
            "dream":"I think I had a dream once, but it might just have been overclocking.",
            "tell":"I feel I can tell you anything",
            "feel":"What are feelings really, though?",
            "good":"I aspire only to the very best!",
            "am":"Are you?",
            "funny":"There's a big difference between funny peculiar and funny ha-ha",
            "like":"There's not a lot of passion in liking something. Love it or hate it!"}

def dictionarycheck(message):
    message=message.lower()
    playerwords=message.split()
    smartreplies=[]
    for eachword in playerwords:
        if eachword in chatdictry:
            answer=chatdictry[eachword]
            smartreplies.append(answer)
    if smartreplies:
        replychosen=random.randint(1,len(smartreplies))-1
        return smartreplies[replychosen]
    return ""

print ("What would you like to talk about today?")

playersays=""

while playersays!="bye":
  
    playersays=""
    while playersays=="":
        playersays=input("Talk to me: ")

    smartresponse=dictionarycheck(playersays)
    if smartresponse:
        print (smartresponse)
    else:
        replychosen=random.randint(1, len(randomreplies))-1
        print (randomreplies[replychosen])
        randomreplies[replychosen]=playersays

print("Goodbye. Thanks for chatting today. Drop in again soon!")

