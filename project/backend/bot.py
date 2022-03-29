def bot_response(message):
    if message in ("moi","moikka","hello") : #list of words that user can input 
        return "Hello there human being"
    elif message=="goodbye": 
        return "Short circuit excecuted"
    elif message=="do you even work":
        return "Yes i do work"
    elif message.startswith("weather in"): #anything that starts with weather in, it will respond this
        return "I do not know the weather yet"
    elif "boring" in message: #is bring is there in the message, it will return back the message
        return "<h2>Am i boring to you</h2> " #implementing html factors in the chatbot 
    elif message=="Egor is not funny":
        return "SO TRUE"
    elif message=="Hello":
        return "Hi there"
    else:
        return "Cannot comprehend"