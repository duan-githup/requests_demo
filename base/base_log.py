from loguru import logger

class GetLogging:
    """
    日志配置
    """
    loggers = None

    @classmethod
    def get_log(cls):
        # 如果 logger为空
        if cls.loggers is None:
            # 错误日志
            logger.add(
                "./log_file/ERROR/{time:YYYY-MM-DD}.log",
                # 只记录ERROR等级BUG
                filter=lambda x: True if x["level"].name == "ERROR" else False,
                rotation="00:00", retention=7, level='ERROR', encoding='utf-8'
            )
            # 成功日志
            logger.add(
                "./log_file/SUCCESS/{time:YYYY-MM-DD}.log",
                # 只记录SUCCESS等级BUG
                filter=lambda x: True if x["level"].name == "SUCCESS" else False,
                rotation="00:00", retention=7, level='SUCCESS', encoding='utf-8',
            )
            # Default日志
            logger.add(
                "./log_file/Default/{time:YYYY-MM-DD}.log",
                rotation="00:00", retention=7, level='DEBUG', encoding='utf-8'
            )
            cls.loggers = logger

        return cls.loggers





if __name__ == '__main__':
    log = GetLogging().get_log()
    log.info("is info")
    log.debug("is debug")
    log.warning("is warning")
    log.error("is critical")
    log.critical("is critical")
    log.success("is success")

