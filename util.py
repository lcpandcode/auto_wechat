# -*- coding: UTF-8 -*-
#工具类
import json
#json标准化工具：返回前端数据标准化
#if 出错：status:0;data:错误信息；     if 正常 status:1;data: 处理结果
def json_get(is_success,data):
    result = {}
    if is_success :
        result['status'] = '1'
    else :
        result['status'] = '0'
    result['data'] = data
    return json.dumps(result)
