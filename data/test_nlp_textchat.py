#-*- coding: UTF-8 -*-
import apiutil
import json

app_key = 'xxx'
app_id = 'xxx'

if __name__ == '__main__':
    str_question = '你好吗?'
    ai_obj = apiutil.AiPlat(app_id, app_key)

    print('----------------------SEND REQ----------------------')
    rsp = ai_obj.getNlpTextchat(str_question)
    if rsp['ret'] == 0:
        print(rsp['data']['answer'])
        print('----------------------API SUCC----------------------')
    else:
        print(json.dumps(rsp,  ensure_ascii=False, sort_keys=False, indent=4))
        print('----------------------API FAIL----------------------')

