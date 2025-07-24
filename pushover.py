
import requests

def send_notification(msg):
    PUSHOVER_USER_KEY = "uhh1qebmuqbuxustn2yf5tt33ushia"
    PUSHOVER_APP_TOKEN = "az1s9o1wzen36xht9yhx9qm92tb9zh"

    requests.post("https://api.pushover.net/1/messages.json", data={
        "token": PUSHOVER_APP_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "message": msg
    })
