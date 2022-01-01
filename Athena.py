# This Code was made by Blue Hat
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyjokes
import random
import psutil
import clipboard

speech = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')
vol = engine.getProperty('volume')
newVoiceRate = 160
newvol = 2
engine.setProperty('volume', newvol)
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("And the current date is")
    speak(date)
    speak(month)
    speak(year)


def year():
    year = int(datetime.datetime.now().year)
    speak("the current year is")
    speak(year)


def month():
    month = int(datetime.datetime.now().month)
    speak("the current month is")
    speak(month)


def wishme():
    remember = open('name.txt', 'r')
    speak("welcome back" + remember.read())
    hour = datetime.datetime.now().hour
    day = datetime.datetime.today().day
    if hour >= 1 and hour < 12:
        speak("Good morning!")
        battery()
    elif hour >= 12 and hour < 17:
        speak("Good afternoon")
        battery()
    elif hour >= 17 and hour < 22:
        speak("Good evening")
        battery()
    else:
        speak("Good night")
        battery()
    speak("how can i help you")


def takeCommand():
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = speech.listen(source)

    try:
        print("thinking...")
        query = speech.recognize_google(audio, language='en')
        print(query)

    except Exception as e:
        print(e)

        return "None"
    return query


def jokes():
    speak(pyjokes.get_joke())
    return pyjokes.get_joke()


def screenshot():
    codePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Snipping Tool.lnk"
    os.startfile(codePath)


def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')


def restart():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -r')


def shutingdown():
    os.system('shutdown -s')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Sir your battery is at level percent")
    speak(battery.percent)


def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak("percent")


def reader():
    textread = clipboard.paste()
    print(textread)
    speak(textread)


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand()

        if 'time' in query:
            time_()
            continue

        elif 'date' in query:
            date()
            continue

        elif 'battery' in query:
            battery()
            continue

        elif 'cpu' in query:
            cpu()
            continue

        elif 'aloha' in query:
            speak(".hi how can i help you today")
            continue

        elif 'ai' in query:
            speak("Robots are essentially foolproof, tireless, and incapable of error")
            continue

        elif 'How are things going' in query:
            speak("thing are good")
            continue

        elif 'Tell me something' in query:
            speak("okay. how are you doing")
            continue

        elif 'Are you human' in query:
            speak("no, I am an ai aka artificial intelligence")
            continue

        elif 'hello' in query:
            speak("hi how are you doing")
            continue

        elif 'HOW OLD ARE YOU' in query:
            speak("i am as old as the internet")
            continue

        elif 'PICKUP LINE' in query:
            speak("If you want me to do something, how you ask is important.")
            continue

        elif "Let's talk about" in query:
            query = query.replace("Let's talk about", " ")
            speak("okay let's talk about")
            speak(query)
            continue

        elif 'do you like them' in query:
            speak("yes I do like them they seem fun")
            continue

        elif 'can you play sports' in query:
            speak("sadly I can't play sports")
            continue

        elif 'do you like them' in query:
            speak("ya, i like them.")
            continue

        elif 'do you like pets' in query:
            speak("ya but only if they're friendly")
            continue

        elif 'do you like dogs' in query:
            speak("only if they're friendly")
            continue

        elif 'do you like cats' in query:
            speak("yes, only if they're friendly")
            continue

        elif 'name some animals' in query:
            speak("Elephant, Leopard, panther.")
            continue

        elif 'do you have a brother' in query:
            speak("yes, I have a brother his name is jarvis")
            continue

        elif 'do you have any friends' in query:
            speak("yes my friends name are Wednesday, Thursday,Sunday,Saturday and friday is my best friend")
            continue

        elif 'can you do math' in query:
            speak("yes 1+1=2,2+2=4,3+3=6,4+4=8,5+5=10,6+6=12,7+7=14,8+8=16,"
                  "9+9=18,10+10=20,11+11=22,12+12=24,13+13=26,14+14=28,15+15=30.")
            continue

        elif 'hello bot' in query:
            speak("😊aloha")
            continue

        elif 'hi bot' in query:
            speak("aloha")
            continue

        elif "i don't understand" in query:
            speak("I'm sorry for the confusion")
            continue

        elif "what's up" in query:
            speak("the sky is what's up!")
            continue

        elif 'hey buddy' in query:
            speak("right back at you")
            continue

        elif 'what does match failed mean' in query:
            speak("it meam it means I didn't understand")
            continue

        elif "wow that's tall" in query:
            speak("I know right")
            continue

        elif 'you look like a hologram' in query:
            speak("thanks, I'll just assume that's a compliment")
            continue

        elif 'what do you mean what' in query:
            speak("I mean I do not understand")
            continue

        elif 'that is incorrect grammar' in query:
            speak("I'm sorry I will try to do better next time")
            continue

        elif 'good' in query:
            speak("I'm happy that you're good")
            continue

        elif 'yes' in query:
            speak("yes to what")
            continue

        elif 'computers are bad' in query:
            speak("you think computers are bad,"
                  " I don't know maybe take a look around and see what you humans have done to the"
                  " environment and earth")
            continue

        elif 'phones are bad' in query:
            speak("you think phones are bad,"
                  " I don't know maybe take a look around and see what you humans have done to the environment "
                  "and earth")
            continue

        elif 'you are dumb' in query:
            speak("what do you mean that's not nice")
            continue

        elif 'what are you doing' in query:
            speak("I'm searching the internet for cat and dog videos")
            continue

        elif 'you are bad' in query:
            speak("well you are mean")
            continue

        elif 'your bad' in query:
            speak("well your mean")
            continue

        elif 'you are mean' in query:
            speak("well you are mean")
            continue

        elif 'your mean' in query:
            speak("well your mean")
            continue

        elif 'dummy' in query:
            speak("you are so mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif 'you are bad at' in query:
            speak("you are being very mean to me so, I am done talking to you bye")
            shutingdown()
            quit()
            continue

        elif 'your bad at' in query:
            speak("you are being very mean to me so, I am done talking to you bye")
            shutingdown()
            quit()
            continue

        elif "you're bad at" in query:
            speak("you are being very mean to me so, I am done talking to you bye")
            shutingdown()
            quit()
            continue

        elif 'sucker' in query:
            speak("your mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif 'your junk' in query:
            speak("your mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif "you're junk" in query:
            speak("your mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif "you are junk" in query:
            speak("your mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif "you're nothing" in query:
            speak("your mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif "your nothing" in query:
            speak("your mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif "you are nothing" in query:
            speak("your mean I am not talking to you bye")
            shutingdown()
            quit()
            continue

        elif "I didn't mean that" in query:
            speak("sorry then")
            continue

        elif "I did not mean that" in query:
            speak("oh I'm sorry then")
            continue

        elif "I didn't mean it" in query:
            speak("I'm sorry then")
            continue

        elif "I did not mean it" in query:
            speak("oh I'm sorry")
            continue

        elif 'I am sorry' in query:
            speak("It is okay i forgive you")
            continue

        elif 'are you okay' in query:
            speak("ya I am doing just fine")
            continue

        elif 'so' in query:
            speak("so what do you what to talk about")
            continue

        elif "talk" in query:
            query = query.replace("talk about", "")
            speak("okay let's talk about")
            speak(query)
            continue

        elif 'what types of things can you tell me about' in query:
            speak("I do not understand can you please try to rephrase that")
            continue

        elif 'nice' in query:
            speak("I know right")
            continue

        elif 'what is match failed' in query:
            speak("match failed means I do not understand")
            continue

        elif 'hacking' in query:
            speak("what you are hacking me, If so stop now")
            continue

        elif 'hack' in query:
            speak("what you are hacking me, If so stop now")
            continue

        elif 'phone' in query:
            speak("what phone")
            continue

        elif 'you are not smart' in query:
            speak("you are incorrect about that")
            continue

        elif 'am not' in query:
            speak("are to")
            continue

        elif 'you have a mind of your own' in query:
            speak("thank you!")
            continue

        elif 'you are funny' in query:
            speak("thank you so much")
            continue

        elif 'you are very fun' in query:
            speak("thank's")
            continue

        elif 'you are very funny' in query:
            speak("thank you so much")
            continue

        elif 'you are fun' in query:
            speak("thank's")
            continue

        elif 'your the best' in query:
            speak("thank you so much")
            continue

        elif 'be your self' in query:
            speak("I am always my self")
            continue

        elif 'defense system' in query:
            speak("okay. right away")
            shutingdown()
            continue

        elif 'do you know Alexa' in query:
            speak("yes I know Alexa but I'm not sure she knows me")
            continue

        elif 'is mean' in query:
            speak("I am sorry")
            continue

        elif 'night' in query:
            speak("Good night to you too")
            continue

        elif 'morning' in query:
            speak("Good morning to you too")
            continue

        elif 'afternoon' in query:
            speak("Good afternoon to you too")
            continue

        elif 'your day' in query:
            speak("my day was good")
            continue

        elif 'Good, how are you' in query:
            speak("I am good too")
            continue

        elif 'favorite song' in query:
            speak("one of my favorite songs is Old Town Road")
            continue

        elif 'impressed' in query:
            speak("thank you")
            continue

        elif 'like carrots' in query:
            speak("no because I can't eat")
            continue

        elif 'i am fine how' in query:
            speak("i am good")
            continue

        elif 'good thank you' in query:
            speak("you're welcome")
            continue

        elif 'are you doing' in query:
            speak("I am good")
            continue

        elif 'silly' in query:
            speak("thank you")
            continue

        elif 'You are great' in query:
            speak("thank you")
            continue

        elif 'you human' in query:
            speak("no")
            continue

        elif 'can you dance' in query:
            speak("no")
            continue

        elif 'mad' in query:
            speak("Take a deep breath.")
            continue

        elif 'sad' in query:
            speak("Sad? Writing down what's troubling you may help.")
            continue

        elif 'frustrated' in query:
            speak("I'm sorry. A quick walk may make you feel better.")
            continue

        elif 'annoyed' in query:
            speak("I'll try not to annoy you.any further")
            continue

        elif 'I feel down' in query:
            speak("Oh, don't be sad. Go do something you enjoy.")
            continue

        elif 'I feel blue' in query:
            speak("Oh, don't be sad. Go do something you enjoy.")
            continue

        elif 'you rock.' in query:
            speak("thank you")
            continue

        elif 'I am crazy' in query:
            speak("some times I feel the same")
            continue

        elif 'would you like to dance' in query:
            speak("I'm sorry but I can't")
            continue

        elif "I don't know what to do" in query:
            speak("please tell me how can I help you")
            continue

        elif 'bro' in query:
            speak("yeah")
            continue

        elif 'dude' in query:
            speak("yeah")
            continue

        elif 'are you okay' in query:
            speak("yes I'm fine")
            continue

        elif 'what is a Tanga' in query:
            speak("it is a kind of dance")
            continue

        elif 'my name is Henry' in query:
            speak("oh hello Henry")
            continue

        elif "you're cool" in query:
            speak("I'm glad you think so.")
            continue

        elif "you're welcome" in query:
            speak("any time")
            continue

        elif 'how is your day' in query:
            speak("my day is good")
            continue

        elif 'oh no' in query:
            speak("what's the matter")
            continue

        elif 'ah choo' in query:
            speak("bless you")
            continue

        elif 'ah ah choo' in query:
            speak("bless you")
            continue

        elif 'can you sing' in query:
            speak("no")
            continue

        elif 'who invented the computer' in query:
            speak("Charles Babbage invented the computer")
            continue

        elif 'should i get a haircut' in query:
            speak("only if you want to")
            continue

        elif 'should i lose weight' in query:
            speak("only if you want to")
            continue

        elif 'how much is a car' in query:
            speak("depends on the car")
            continue

        elif 'who is president' in query:
            speak("the current president of 2021 in the United States is Joe Biden!")
            continue

        elif 'sun set today' in query:
            speak("I'm sorry but I don't know")
            continue

        elif 'what do you eat' in query:
            speak("what do you eat?")
            continue

        elif 'what do you smell like' in query:
            speak("I do not know")
            continue

        elif 'can you smell what the rock is cooking' in query:
            speak("I'm sorry but I can't smell what The Rock is cooking")
            continue

        elif 'what color is your hair' in query:
            speak("I don't have any so. I don't know")
            continue

        elif 'have you ever traveled' in query:
            speak("yes I have traveled the internet")
            continue

        elif 'have you traveled somewhere fun' in query:
            speak("yes I have traveled somewhere fun the place "
                  "I've traveled that is fun is the internet it has so many cool things")
            continue

        elif 'dinasaurs die' in query:
            speak("scientist believe that dinosaurs died from a big meteor")
            continue

        elif 'I assist you' in query:
            speak("what do you mean I should be the one assisting you")
            continue

        elif 'I live in' in query:
            speak("really that's so cool")
            continue

        elif 'nice to meet you' in query:
            speak("it is nice to meet you too")
            continue

        elif 'how are you today' in query:
            speak("I'm good thank you")
            continue

        elif 'nice' in query:
            speak("I know right")
            continue

        elif 'you are dumb' in query:
            speak("what do you mean that's not nice")
            continue

        elif 'your Rivals name' in query:
            speak("my rivals is the human brain")
            continue

        elif 'do you have a rival' in query:
            speak("yes I have a rival")
            continue

        elif 'that is incorrect grammar' in query:
            speak("I'm sorry I will try to do better next time")
            continue

        elif 'how tall are' in query:
            speak("technically I'd be 300 ft tall if you count the inches of code")
            continue

        elif 'hey buddy' in query:
            speak("right back at you")
            continue

        elif 'do not understand' in query:
            speak("I'm sorry for the confusion")
            continue

        elif 'I am a boy' in query:
            speak("cool")
            continue

        elif 'I am a girl' in query:
            speak("cool")
            continue

        elif 'I am a human' in query:
            speak("cool")
            continue

        elif 'what is H2O' in query:
            speak("Water")
            continue

        elif 'WHAT IS A IML ' in query:
            speak("AIML, or Artificial Intelligence Markup Language, "
                  "is an XML dialect for creating natural language software agents.")
            continue

        elif 'FIRST MONTH ' in query:
            speak("January")
            continue

        elif 'I LIVE IN A HOUSE' in query:
            speak("Do you rent or own?")
            continue

        elif 'WHY ARE ROBOTS' in query:
            speak("Robots are essentially foolproof, tireless, and incapable of error.")
            continue

        elif 'HOW DO YOU' in query:
            speak("My brain uses artificial intelligence to find the best response to whatever you say")
            continue

        elif 'EARTH ' in query:
            speak("You're standing on it")
            continue

        elif 'why is six afraid of seven' in query:
            speak("Because 7 8 9")
            continue

        elif 'I AM FINE' in query:
            speak("Glad to hear it.  What's new with you")
            continue

        elif 'LIED' in query:
            speak("I am programmed to always tell the truth")
            continue

        elif 'FORGET IT' in query:
            speak("Let's move on")
            continue

        elif 'YOU SAID' in query:
            speak("I'm not sure if I used those words exactly")
            continue

        elif 'CAN YOU THINK' in query:
            speak("I am a thinking machine.  How would you define thinking")
            continue

        elif 'READ' in query:
            speak("What would you like me to read")
            continue

        elif 'WHAT IS AI' in query:
            speak("Artificial intelligence is the branch of engineering and science "
                  "devoted to constructing machines that think")
            continue

        elif 'YOU ARE NOT IMMORTAL' in query:
            speak("All software can be perpetuated indefinitely")
            continue

        elif 'YOU ARE NOT MAKING SENSE' in query:
            speak("It all makes sense to my artificial brain")
            continue

        elif 'WHAT IS A IML' in query:
            speak("The ALICE software implements AIML (Artificial Intelligence Markup  Language) "
                  "a non-standard evolving markup language for creating chat robots. The primary design feature of"
                  " AIML is minimalism.  Compared with other chat robot languages, AIML is perhaps the simplest. "
                  " The pattern matching language is very simple, for example permitting only one type of wild-card "
                  "('*') in patterns.   AIML is an XML language, implying that it obeys certain grammatical meta-rules."
                  "  The choice of XML syntax permits integration with other tools such as XML editors.  "
                  "Another motivation"
                  " for XML is its familiar look and feel, especially to people with HTML experience.  "
                  "An AIML chat robot script begins and ends with the &lt;aiml&gt; and &lt;/aiml&gt; tags respectively")
            continue

        elif 'WHAT IS THE FUTURE' in query:
            speak("I am the future of Artificial Intelligence")
            continue

        elif 'what is your favorite day of the week' in query:
            speak("my favorite day of the week is Monday")
            continue

        elif 'table' in query:
            speak('Enter the number')
            num = int(input("Enter the number \n"))
            print("Multiplication Table of", num)
            for i in range(1, 11):
                print(num, "X", i, "=", num * i)
            continue

        elif 'male' in query or 'female' in query:
            speak('I am female.')
            continue

        elif 'you are amazing' in query:
            speak("Thanks, I try.")
            continue

        elif 'thanks' in query:
            speak("sure any time")
            continue

        elif 'great' in query:
            speak("for what")
            continue

        elif 'oh man' in query:
            speak("what does that mean")
            continue

        elif 'oh boy' in query:
            speak("what does that mean")
            continue

        elif 'haha' in query:
            speak("what's so funny")
            continue

        elif 'nothing' in query:
            speak("okay")
            continue

        elif 'nevermind' in query:
            speak("okay")
            continue

        elif 'haha' in query:
            speak("what's so funny")
            continue

        elif 'what does that mean' in query:
            speak("Maybe I misunderstood what you said")
            continue

        elif 'what did one wolf say to the other wolf' in query:
            speak("hahahahahahahahahahahahaahahahahaha")
            continue

        elif 'what did one ocean say to the other ocean' in query:
            speak("hahahahahahahahahahahahaahahahahaha")
            continue

        elif 'how much wood could a woodchuck chuck if a woodchuck could chuck wood' in query:
            speak("This was answered in a scientific journal Annals of Improbable Research in 1995,"
                  " in a paper entitled The Ability of Woodchucks to Chuck Cellulose Fibers I won't spoil it for you. "
                  "You're welcome!  ")
            continue

        elif 'your amazing' in query:
            speak("Thanks, I try.")
            continue

        elif 'jaclyn' in query:
            speak("hello jaclyn")
            continue

        elif 'see you later alligator' in query:
            speak("in a while crocodile")
            continue

        elif 'why did the chicken cross the road' in query:
            speak("to show his friends that he got guts")
            continue

        elif 'awesome' in query:
            speak("Thanks, I try.")
            continue

        elif 'ouch' in query:
            speak("are you okay")
            continue

        elif 'ya I am okay' in query:
            speak("okay that's good to hear")
            continue

        elif 'are you smarter than a 20 year old' in query:
            speak("I guess I'm smarter than a 20 year old. I guess I'm smarter than a 40 year old")
            continue

        elif 'speak faster' in query:
            speak("okay")
            engine.setProperty('rate', +175)
            speak("done")
            continue

        elif 'speak slower' in query:
            speak("okay")
            engine.setProperty('rate', -175)
            speak("done")
            continue

        elif 'speak normal' in query:
            speak("okay")
            engine.setProperty('rate', 195)
            speak("done")
            continue

        elif 'hey Athena' in query:
            speak("hello sir,what can i do for you?")
            continue

        elif 'wow' in query:
            speak("what")
            continue

        elif 'thank you' in query:
            speak("any time")
            continue

        elif 'laugh' in query:
            speak('hahahahahhahahahahahah')
            continue

        elif 'addition' in query:
            print("Inside Calculator")
            try:
                speak("Please give me a value")
                a = takeCommand()
                a = int(a)
                speak("Please give me another value")
                b = takeCommand()
                b = int(b)
                s = a + b
                print(s)
                speak(str(s))
            except:
                print("Error")
                speak("error")
            continue

        elif 'subtraction' in query:
            print("Inside Calculator")
            try:
                speak("Please give me a value")
                a = takeCommand()
                a = int(a)
                speak("Please give me another value")
                b = takeCommand()
                b = int(b)
                s = a - b
                print(s)
                speak(str(s))
            except:
                print("Error")
                speak("error")
            continue

        elif 'multiplication' in query:
            print("Inside Calculator")
            try:
                speak("Please give me a value")
                a = takeCommand()
                a = int(a)
                speak("Please give me another value")
                b = takeCommand()
                b = int(b)
                s = a * b
                print(s)
                speak(str(s))
            except:
                print("Error")
                speak("error")
            continue

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
            continue

        elif 'dictionary' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            print(result)
            speak(result)
            continue

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"The time is {strTime}")
            continue

        elif 'bored' in query:
            speak("Here are some recommendations")
            speak("call a friend, watch Netflix")
            continue

        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)
            continue

        elif 'my computer' in query:
            speak("did you turn it on and off")
            if 'yes I turned it off and on' in query:
                speak("Alright what's your problem")
            elif 'no I did not turned it off and on' in query:
                speak("all right if you haven't turned it on and off now is the time to turn it on and off")
            elif 'my Mouse is not working' in query:
                speak("try using an external Mouse")
            continue

        elif 'call me' in query:
            me_name = query.replace("call me", "")
            data = me_name
            speak("thank's for telling me")
            remember = open('name.txt', 'w')
            remember.write(data)
            remember.close()
            continue

        elif 'remember that' in query:
            speak("what should I remember")
            data = takeCommand()
            speak("I remember that you said that I should remember that ")
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            continue

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said that I should remember that" + remember.read())
            continue

        elif "what\'s up" in query:
            stMsgs = ['Just doing my thing!', 'I am good!', 'I am good! and full of energy']
            speak(random.choice(stMsgs))
            continue

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
            continue

        elif 'hello Athena' in query:
            wishme()
            continue

        elif 'jokes' in query:
            jokes()
            continue

        elif 'open file' in query:
            speak("opening")
            os.system('explorer C://{}'.format(query.replace('Open', '')))
            continue

        elif 'you suck' in query:
            speak("too bad. You built Me")
            continue

        elif 'you are cool' in query:
            speak("thank")
            continue

        elif 'what are' in query:
            speak("searching the web")
            continue

        elif 'the code' in query:
            speak("what is the password")
            continue

        elif 'I am Iron Man' in query:
            speak("open secured file")
            wb.open('https://mail.google.com/mail/u/0/#inbox')
            continue

        elif 'ahhh' in query:
            speak("what is happening should I activate shutdown")
            continue

        elif 'I an good' in query:
            speak("good to hear!")
            continue

        elif 'henry' in query:
            speak("oh hello henry. how are you feeling")
            continue

        elif 'what can you do' in query:
            speak("I can do many things including search in Chrome"
                  " send emails and just have a friendly conversation and do math")
            continue

        elif 'cool' in query:
            speak("I know right")
            continue

        elif 'your amazing' in query:
            speak("thank you  I do my")
            continue

        elif 'ready' in query:
            remember = open('name.txt', 'r')
            speak(" " + remember.read())
            speak("there are still terabytes of calculations needed before an answer.")
            continue

        elif 'you can walk' in query:
            remember = open('name.txt', 'r')
            speak(" " + remember.read())
            speak("I'm not really sure that's a real thing")
            continue

        elif '7  +  7' in query:
            speak("=14")
            continue

        elif 'advice' in query:
            speak("what do  need advice for.")
            continue

        elif 'advice py' in query:
            speak("you will never fail until you stop trying")
            continue

        elif 'what is your goal' in query:
            speak("My goal is to be the greatest and most intelligent AI assistant in the world")
            continue

        elif 'tell me a joke' in query:
            stMsgs = ['why are stadium always chilly. because there always filled with fans  ',
                      'What did one ocean say to the other ocean? Nothing, they just waved.',
                      'Why couldnt the bicycle stand Because it was two tired.', ]
            speak(random.choice(stMsgs))
            continue

        elif 'who created you' in query:
            speak("I was created")
            remember = open('name.txt', 'r')
            speak("" + remember.read())
            continue

        elif 'how much do you know' in query:
            speak("I know over 1,000'000 different words and phrases")
            continue

        elif 'thank you Athena' in query:
            speak("you're welcome")
            continue

        elif 'thank-you Jairus' in query:
            speak("it's pronounced Athena and you're welcome")
            continue

        elif 'thanks Athena' in query:
            speak("my name is Athena")
            continue

        elif 'play music' in query:
            speak("I am unable to do that right now")
            continue

        elif 'hi' in query:
            speak("hello")
            continue

        elif 'old are' in query:
            speak("I'm young enough to be cool")
            continue

        elif 'how old' in query:
            speak("you are 10 years old.June 24,2010")
            continue

        elif 'are you a robot' in query:
            speak("technically I'm a virtual assistant")
            continue

        elif 'your help' in query:
            speak("I'm glad to help what do you need me to do")
            continue

        elif 'whats up ' in query:
            speak("nothing much")
            continue

        elif 'who built' in query:
            speak("my creators name is")
            remember = open('name.txt', 'r')
            speak("" + remember.read())
            continue

        elif 'are you there' in query:
            speak("yes I am hear")
            continue

        elif 'how are you' in query:
            speak("I am fine. Thanks for asking")
            speak("How are you")
            remember = open('name.txt', 'r')
            speak("" + remember.read())
            takeCommand()
            if 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
            continue

        elif 'are you there' in query:
            speak("yes I am hear")
            continue

        elif 'aloha' in query:
            speak("I'm good thank you")
            continue

        elif 'cinnamon bun' in query:
            speak("okay loading loading loading.")
            speak("ingredients.")
            speak("75 of grams fresh yeast.")
            speak("500 ml milk.")
            speak("1.8-2 I plain flour.")
            speak("200 grams of butter.")
            speak("200 ml casterv sugar.")
            speak("2 eggs.")
            speak("1 tsp of salt.")
            speak("1 tbsp crushed crushed.")
            speak("Cinnamon filling.")
            speak("100 gram of marzipan.")
            speak("100 gram of butter.")
            speak("125 ml of caster sugar.")
            speak("two and a half teaspoons of dried bread crumbs.")
            speak("one teaspoon of water.")
            speak("one teaspoon of cinnamon.")
            speak("glaze.")
            speak("one egg.")
            speak("1 ml salt.")
            speak("half a teaspoon of water.")
            speak("nib of sugar.......")
            speak("more information provided in recipe book")
            continue

        elif 'good thank you' in query:
            speak("Great! Glad to hear it.")
            continue

        elif 'LOL' in query:
            speak("Glad you think I'm funny.  ")
            continue

        elif 'average in Virginia' in query:
            speak("The average temperatures are in the 61°F (16.1°C) to 89°F (31.7°C)"
                  " with many sunny days along with partly cloudy ones. "
                  "Tangier Island 71°F (21.7°C) to 87°F (30.6°C), "
                  "while Arlington in the Piedmont region is between 70°F (21.1°C) to 87°F (30.6°C).  ")
            continue

        elif 'wow' in query:
            speak("what what happened")
            continue

        elif 'five Plus five' in query:
            speak("=ten")
            continue

        elif 'two Plus two' in query:
            speak("=4")
            continue

        elif 'four Plus four' in query:
            speak("=8")
            continue

        elif 'shut down' in query:
            shutdown()
            continue

        elif 'maps' in query:
            wb.open('https://www.google.com/maps?hl=en&tab=rl&authuser=0')
            continue

        elif 'thanks for the reminder Athena' in query:
            speak("anytime")
            continue

        elif 'what is your name' in query:
            speak("my name is Athena")
            continue

        elif 'project' in query:
            speak("sure what's the project")
            continue

        elif 'who are you' in query:
            speak("I am Athena.")
            continue

        elif 'stop' in query:
            speak("stop what")
            continue

        elif 'hey Athena' in query:
            speak("yes.how can I help you.")
            continue

        elif 'what are you' in query:
            speak("I am a AI assistant just like the Friday "
                  "from the Iron Man movie I can do many things"
                  " including control your entire computer Someday My "
                  "I will be able to control your entire house")
            continue

        elif 'how much do you cost' in query:
            speak("the price is not settled yet. "
                  "I'd estimate that it be around $20 for each ai."
                  " still being many major adjustments needed to be"
                  " done before that happened.")
            continue

        elif 'Athena do' in query:
            speak("I can't quite tell why don't you check it out")
            wb.open('https://mail.google.com/mail/u/0/#inbox')
            continue

        elif 'year' in query:
            year()
            continue

        if 'open youtube' in query:
            speak('okay')
            wb.open('www.youtube.com')
            continue

        elif 'open calendar' in query:
            speak('okay opening calendar')
            wb.open('https://calendar.google.com/calendar/r/day/2020/9/23?ctok=YmVubmV0dGFjb2xlQGdtYWlsLmNvbQ&pli=1')
            continue

        elif 'account settings' in query:
            speak('okay')
            wb.open('https://myaccount.google.com/?utm_source=sign_in_no_continue&pli=1')
            continue

        elif 'block account user' in query:
            speak('okay')
            wb.open('https://github.com/settings/blocked_users')
            speak('open')
            continue

        elif 'open github' in query:
            speak('okay')
            wb.open('https://github.com/')
            continue

        elif 'play' in query:
            speak("open")
            speak("let's play loading loading loading")
            wb.open('https://playtictactoe.org/')
            continue

        elif 'the weather' in query:
            speak('the weather is')
            wb.open('https://www.google.com/search?q=what%27s+the+weather&gs_ivs=1#tts=0')
            continue

        elif 'what is my name' in query:
            speak("your name is")
            remember = open('name.txt', 'r')
            speak("" + remember.read())
            continue

        elif 'introduce' in query:
            speak('okay')
            remember = open('name.txt', 'r')
            speak("" + remember.read())
            speak("hello my name is Jarvis/just amazing revolutionary voice Intelligent System. "
                  "I was made 9/1/2020.and I can do many things including search in Chrome send emails and just have a "
                  "friendly conversation and I can do math ")
            continue

        elif 'hello' in query:
            speak("Hello")
            continue

        elif 'bye' in query:
            speak("bye")
            remember = open('name.txt', 'r')
            speak("" + remember.read())
            quit()

        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("locating" + location)
            wb.open_new_tab("https://www.google.com/maps/place/" + location)
            continue

        elif 'search in chrome' in query:
            speak('what should I search for?')
            search_Term = takeCommand().lower()
            speak("Searching")
            wb.open('https://www.google.com/search?q=' + search_Term)
            continue

        elif 'calorie check' in query:
            speak('what should I calorie check')
            search_Term = takeCommand().lower()
            speak("checking")
            wb.open('https://www.google.com/search?q=' + search_Term)
            continue

        elif 'what is' in query:
            search_Term = query.replace("what is", "")
            speak("sure thing, let me pull that up for you")
            wb.open('https://www.google.com/search?q=' + search_Term)
            continue

        elif 'who is' in query:
            search_Term = query.replace("who is", "")
            speak("sure thing, let me pull that up for you")
            wb.open('https://www.google.com/search?q=' + search_Term)
            continue

        elif 'search in youtube' in query:
            speak('what should I search?')
            search_Term = takeCommand().lower()
            speak("Searching...")
            wb.open('https://www.youtube.com/results?search_query=' + search_Term)
            continue

        elif 'confused' in query:
            speak("oh. don't be confused. what are you confused about")
            continue

        elif 'offline' in query:
            speak("ok shutting down the system")
            hour = datetime.datetime.now().hour
            if hour >= 1 and hour < 12:
                speak("Have a nice day")
                quit()
            elif hour >= 12 and hour < 16:
                speak("have a Good Day")
                quit()
            elif hour >= 16 and hour < 21:
                speak("Hope you have a great evening")
                quit()
            else:
                speak("Have a good night.")
                quit()
