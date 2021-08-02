import requests,api
from base.base_log import GetLogging
log = GetLogging.get_log()

class TimingTaskApi:

    def __init__(self):
        # 获取接口资源
        self.url_add = api.host + "/cloud/task/saveOrUpdateTask"
        self.url_del = api.host + "/cloud/task/deleteTask"
        log.success("————————————————————> 初始化获取【定时任务】接口资源")

    def timing_t_task_add(self, token, planId, taskId, taskHardwareId, taskName, timedExecuteType, beginDate, endDate,
                          weeks, executeTime, continueTime, taskPriority, taskMediaFileId, playMode, taskVolume,
                          taskType):
        log.success("添加定时任务")
        # 发送请求参数
        data = {
            "planId": planId,
            "taskId": taskId,
            "taskHardwareId": taskHardwareId,
            "taskName": taskName,
            "timedExecuteType": timedExecuteType,
            "beginDate": beginDate,
            "endDate": endDate,
            "weeks": weeks,
            "executeTime": executeTime,
            "continueTime": continueTime,
            "taskPriority": taskPriority,
            "taskMediaFileId": taskMediaFileId,
            "playMode": playMode,
            "taskVolume": taskVolume,
            "taskType": taskType
        }
        # 返回响应对象
        response = requests.post(self.url_add, data=data, headers=token)
        log.success("获取【添加定时任务】请求对象:{}".format(response))
        return response

    def timing_t_task_put(self, token, weeks, timedExecuteType, continueTime, taskHardwareId, playMode, executeTime,
                          taskType, endDate, beginDate, taskName, taskPriority, taskVolume, taskMediaFileId, planId,
                          taskId):
        log.success("修改定时任务")
        # 发送请求参数
        data = {
            "weeks": weeks,
            "timedExecuteType": timedExecuteType,
            "continueTime": continueTime,
            "taskHardwareId": taskHardwareId,
            "playMode": playMode,
            "executeTime": executeTime,
            "taskType": taskType,
            "endDate": endDate,
            "beginDate": beginDate,
            "taskName": taskName,
            "taskPriority": taskPriority,
            "taskVolume": taskVolume,
            "taskMediaFileId": taskMediaFileId,
            "planId": planId,
            "taskId": taskId
        }
        # 返回响应对象
        response = requests.post(self.url_add, data=data, headers=token)
        log.success("获取【修改定时任务】请求对象:{}".format(response))
        return response

    def timing_t_task_del(self, token, taskIds):
        log.success("删除定时任务")
        # 发送请求参数
        data = {
            "taskIds": taskIds
        }
        # 返回响应对象
        response = requests.post(self.url_del, data=data, headers=token)
        log.success("获取【删除定时任务】请求对象:{}".format(response))
        return response


if __name__ == '__main__':
    t = TimingTask_T_Api()
