import google.generativeai as palm

def init(key):
    palm.configure(api_key=key)
    return palm.chat(messages='Hello', temperature=1)


def reply(response, prompt):
    return response.reply(prompt)
