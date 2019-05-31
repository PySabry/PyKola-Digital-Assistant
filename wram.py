import wolframalpha

question = input("Q: ")
app_id = "Your wolframalpha app id"
client = wolframalpha.Client(app_id)

res = client.query(question)
answer = next(res.results).text

print (answer)