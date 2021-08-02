# 导包
import requests, api
from base.base_log import GetLogging

log = GetLogging.get_log()

class GetToken:

    def __init__(self):
        # 获取接口资源
        self.url = api.host + "/cloud/userLogin/login"
        log.success("————————————————————> 初始化获取【登录】接口资源")

    def getToken(self,username="admin",password="MTIzNDU2",captcha="TEST"):
        log.success("用户登录获取token")
        # 请求参数
        data = {
            "username":username,
            "password":password,
            "captcha":captcha
        }
        # 响应结果
        response = requests.post(url=self.url,data=data)

        token = {"Authorization": "Cloudbc " + response.headers["token"]}
        return token


if __name__ == '__main__':
    GetToken().getToken("admin","MTIzNDU2","TEST")