customer_feedback = {"positive" : ["wow!", "great!"],
                     "neutral" : ["okay", "alright"],
                     "negative" : ["sucks", "bad"]}

def add_feedback(sentiment, feedback):
    try:
        customer_feedback[sentiment].append(feedback)
    except KeyError:
        print(f"{sentiment} sentiment does not exist.")

def display_count(sentiment):
    try:
        count = len(customer_feedback[sentiment])
        print(f"There are {count} counts of {sentiment} feedback.")
    except KeyError:
        print(f"{sentiment} sentiment does not exist.")

def display_feedback(sentiment):
    try:
        for feedback in customer_feedback[sentiment]:
            print(feedback)
    except KeyError:
        print(f"{sentiment} sentiment does not exist.")

while True:
    action = input("[A]dd feedback, display [c]ount, display [f]eedback, or [q]uit?")
    if action.lower() == 'a':
        sentiment = input("Is your feed back 'positive', 'neutral', or 'negative'?")
        feedback = input("What is your feedback?")
        add_feedback(sentiment.lower(), feedback)
    elif action.lower() == 'c':
        sentiment = input("Is your feed back 'positive', 'neutral', or 'negative'?")
        display_count(sentiment.lower())
    elif action.lower() == 'f':
        sentiment = input("Is your feed back 'positive', 'neutral', or 'negative'?")
        display_feedback(sentiment.lower())
    elif action.lower() == 'q':
        print("Thanks for using the program!")
        break
    else:
        print(f"{action} is not a valid action.")
