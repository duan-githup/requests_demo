from api.fileTaskApi import FileTaskApi
from api.textTaskApi import TextTask
from api.timingProjectApi import TimingProject
from api.timingTaskApi import TimingTaskApi
from api.tokenApi import GetToken


class EntranceApi:

    def ent_token(self):
        """token对象"""
        return GetToken()

    def ent_file_task(self):
        """文件广播任务"""
        return FileTaskApi()

    def ent_text(self):
        """文字转语音"""
        return TextTask()

    def ent_project_task(self):
        """定时方案"""
        return TimingProject()

    def ent_timing_task(self):
        """定时任务"""
        return TimingTaskApi()

