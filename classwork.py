def question(str):
    words = str.split(" ")
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].upper()
        else:
            words[i] = words[i].capitalize()
    

question("this is my machine learning class")

# list comprehension
def question2(str):
    print(" ".join([word.upper() if i % 2 == 0 else word.capitalize() for i, word in enumerate(str.split())]))

question2("this is my machine learning training class")
