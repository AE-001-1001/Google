import random as r


statements = ["hi", "hello", "hey", "howdy", "hey there", 
              "whats up", "how are you", "hows it going"]
# make random choices from the list statements
questions = r.choices(["Good , How are you doing?", "Nothing Much , What are you up to?", 
            " I am doing good,How are you?", "I'm chillin, What about you?"])
# make a questions biased towards what the user said
# for example if the user said "how are you" then the bot should respond with "I'm good, how are you?"
# if the user said "what are you doing" then the bot should respond with "I'm chill , what about you?"
