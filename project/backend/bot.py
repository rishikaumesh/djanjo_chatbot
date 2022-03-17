def bot_response(message):
    if message=="hello": 
        return "Hello human being"
    elif message=="goodbye": 
        return "Short circuit excecuted"
    elif message=="do you even work":
        return "Yes i do work"
    elif message.startswith("weather in"): #anything that starts with weather in, it will respond this
        return "I do not know the weather yet"
    elif "boring" in message: #is bring is there in the message, it will return back the message
        return "Am i boring to you "
    else:
        return "Cannot comprehend"