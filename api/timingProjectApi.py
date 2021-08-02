import requests, api

from base.base_log import GetLogging
log = GetLogging.get_log()

class TimingProject:
    def __init__(self):
        # 获取接口资源
        self.url_add = api.host + "/cloud/plan/saveOrUpdatePlan"
        self.url_state = api.host + "/cloud/plan/enablePlanOrNot"
        self.url_del = api.host + "/cloud/plan/delPlan"
        log.success("——————————————————————————> 初始化【定时方案】接口资源")

    def timing_project_add(self, token, planId, planName, beginDate, endDate, holidayJson):
        log.success("添加定时方案")
        # 发送请求参数
        data = {
            "planId": planId,
            "planName": planName,
            "beginDate": beginDate,
            "endDate": endDate,
            "holidayJson": holidayJson
        }
        # 获取响应结果
        response = requests.post(self.url_add, data=data, headers=token)
        log.success("获取【添加定时任务】请求对象:{}".format(response))
        return response

    def timing_project_put(self, token, planId, planName, beginDate, endDate, holidayJson):
        log.success("修改定时方案")
        # 发送请求参数
        data = {
            "planId": planId,
            "planName": planName,
            "beginDate": beginDate,
            "endDate": endDate,
            "holidayJson": holidayJson
        }
        # 返回响应结果
        response = requests.post(self.url_add, data=data, headers=token)
        log.success("获取【修改定时方案】请求对象:{}".format(response))
        return response

    def timing_project_state(self, token, planId, enableState):
        log.success("修改定时方案状态")
        # 发送接口资源
        data = {
            "planId": planId,
            "enableState": enableState
        }
        # 返回响应结果
        response = requests.post(url=self.url_state, data=data, headers=token)
        log.success("获取【修改定时方案方案】请求对象:{}".format(response))
        return response

    def timing_project_del(self, token, planIds):
        log.success("删除定时方案")
        # 发送请求参数
        data = {
            "planIds": planIds
        }
        response = requests.post(url=self.url_del, data=data, headers=token)
        log.success("获取【删除定时方案方案】请求对象:{}".format(response))
        return response


