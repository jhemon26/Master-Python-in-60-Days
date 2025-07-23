greetings = input("Please type your message: ")

if greetings.strip().lower() == "hello":
    print("Hello there, how are you?")
    name = input("What is your name? :")
    print (f"have a good day {name}")
elif greetings == "hi":
    print ("Welcome to this Website :) ")

else:
    print("I am your helping chat Bot. How can I help you?")