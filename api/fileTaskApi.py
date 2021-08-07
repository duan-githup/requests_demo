import requests, api
from base.base_log import GetLogging

log = GetLogging.get_log()


class FileTaskApi:
    def __init__(self):
        # 接口资源
        self.url_add = api.host + "/cloud/task/playByTerminalFile"
        self.url_del = api.host + "/cloud/task/stopRealtimeTask"
        log.success("——————————————————————————> 初始化【文件广播】接口资源")

    def file_add(self, token,hardwareIds,mediaFileIds,taskPriority,playMode,volume,taskName):
        log.success("添加文件广播任务")
        data = {
            "hardwareIds": hardwareIds,
            "mediaFileIds": mediaFileIds,
            "taskPriority": taskPriority,
            "playMode": playMode,
            "volume": volume,
            "taskName": taskName
        }
        response = requests.post(url=self.url_add, data=data, headers=token)
        # print(response.status_code)
        # print(response.text)
        return response

    def file_del(self, token, taskIds, taskType):
        log.success("删除文件广播任务")
        data = {
            "taskIds": taskIds,
            "taskType": taskType
        }
        response = requests.post(url=self.url_del, data=data, headers=token)
        return response


if __name__ == '__main__':
    from api.entranceApi import EntranceApi
    t = EntranceApi().ent_token().getToken()
    f = FileTaskApi()
    f.file_add(t)
