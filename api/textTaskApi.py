import requests,api
class TextTask:
    def __init__(self):
        self.url = api.host + "/cloud/task/playTxtAudio"

    def text_add(self,token):
        data = {
            "hardwareIds":"010172021316,010172021322",
            "txtContent":"广州音桥电子科技有限公司欢迎你",
            "volume":"50",
            "speechData":'{"voiceId":2,"priority":5,"speed":50,"tone":50,"playCount":1}'
        }
        response = requests.post(url=self.url,data=data,headers=token)
        print(response.text)
        print(response.status_code)
        return response


if __name__ == '__main__':
    from api.entranceApi import EntranceApi
    token = EntranceApi().ent_token().getToken()
    TextTask().text_add(token)
