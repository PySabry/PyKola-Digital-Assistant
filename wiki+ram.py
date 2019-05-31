import wikipedia
import wolframalpha

while True:
    question = input("Q: ")

    try:
        # wolframalpha
        app_id = "your wolframalpha app id"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print(answer)
    except:
        # wikipedia
        print(wikipedia.summary(question))
