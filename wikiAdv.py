import wikipedia

while True:
        question = input("Q: ")  # type: str
        wikipedia.set_lang("ar")
        print (wikipedia.summary(question, sentences=2))