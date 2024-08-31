import json

with open('messages.json', 'r', encoding='cp850') as file:
    data = json.load(file)

messages_btc = dict()
messages = range(len(data['messages']))
for i in messages:
    try:
        text = data['messages'][i]['text'][0].lower()
    except IndexError:
        text = data['messages'][i]['text'].lower()
    except AttributeError:
        text = data['messages'][i]['text']
    if 'btc' in text:
        messages_btc[i] = data['messages'][i]

with open('messages_btc.json', 'w') as outfile:
    json.dump(messages_btc, outfile, indent=4)
