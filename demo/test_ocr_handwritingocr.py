#-*- coding: UTF-8 -*-
import sys
sys.path.append('../txai') 
import apiutil
import json

app_key = 'xxx'
app_id = 'xxx'

if __name__ == '__main__':
    with open('../data/handwritingocr.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print('----------------------SEND REQ----------------------')
    rsp = ai_obj.getOcrHandwritingocr(image_data)

    if rsp['ret'] == 0:
        for i in rsp['data']['item_list']:
            print(i['itemstring'])
        print('----------------------API SUCC----------------------')
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
        print('----------------------API FAIL----------------------')