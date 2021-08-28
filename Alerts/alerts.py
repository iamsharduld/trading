import requests #dependency

url = "https://discord.com/api/webhooks/881320164296106004/qj9oRgC72gpH7hI9ZQAOPmGKNk7H-oPMkZ6ZKMSAEWQEnP29RVfED8BiigIAK3GnWRzU" #webhook url, from here: https://i.imgur.com/f9XnAew.png

#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "username" : "Crypto",
    "content" : "Buy BTC"
}

#leave this out if you dont want an embed
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
# data["embeds"] = [
#     {
#         "description" : "text in embed",
#         "title" : "embed title"
#     }
# ]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
