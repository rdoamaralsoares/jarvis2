import requests
from datetime import datetime as dt
import simplejson as json

class API_Interaction:
    def __init__(self, active=True):
        self.timestamp = dt.now()
        self.active = active

    def notify_detection(self):

        if self.active:
            url = "<<<< API URL to notify Alexa >>>>"

            parameters = {
                "trigger": "<< Trigger >>",
                "token": "<< Token >>",
                "response": "json"
            }


            headers = {
                "User-Agent": "Python 3.9",
                "Accept": "*/*",
                "Accept-Encoding": "utf-8",
                "Connection": "keep-alive"
            }
            try:
                response = requests.request("GET", url, headers=headers, params=parameters, timeout=3)
                print(response.text)
                return True
            except:
                return False

    def send_know_founded(self, user):
        if self.active:
            agora = dt.now()
            if (agora - self.timestamp).total_seconds() > 30.0:
                print("==>Notificou")
                self.timestamp = dt.now()

                self.notify_detection()

                payload = json.dumps(user)
                print("==>Payload:", payload)

                url = "<<<< API URL to send data of user founded>>>>"

                headers = {
                    'x-api-key': '<<API Key>>',
                    'Content-Type': 'application/json'
                }
                try:
                    response = requests.request("POST", url, headers=headers, data=payload, timeout=3)
                    print("==>sended know", response)
                    return True
                except:
                    return False
            else:
                print("==> Nao Notificou")



    def send_unknow_founded(self, face, infos):
        if self.active:
            agora = dt.now()
            if (agora - self.timestamp).total_seconds() > 30.0:
                print("==> Notificou")
                self.timestamp = dt.now()

                self.notify_detection()

                unknow = {
                    "index": "temp",
                    "knowuser": False,
                    "name":  "Unknow",
                    "alias": "unknow",
                    "email": "unknow@unknow.com",
                    "mobilenumber": "unknow",
                    "companyname": "unknow",
                    "face": face,
                    "type": "unknow",
                    "status": "inactive",
                    "infos": infos
                }

                payload = json.dumps(unknow)
                url = "<<UR to notify that there is an user not founded in front of camera>>"

                headers = {
                    'x-api-key': '<<API KEY>>',
                    'Content-Type': 'application/json'
                }
                try:
                    response = requests.request("POST", url, headers=headers, data=payload, timeout=5)
                    print("==>Send unknow", response.text)
                    return True
                except:
                    return False
            else:
                print("==> Não notificou")