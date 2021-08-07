# 查询硬件终端
sql_hardware = 'select hardware_id from t_terminal where terminal_name LIKE "%音柱%" or terminal_name LIKE "%音箱%";'

# 查询音频文件数据
sql_media = 'select media_file_id from t_media_file where file_type = 0 LIMIT 0,10;'

# 通过任务名称查询ID
sql_taskId = 'select task_id from t_task where task_name="{}"'

# 查询定时方案ID
sql_timing_projeckID = "select plan_id from t_plan where plan_name='{}';"