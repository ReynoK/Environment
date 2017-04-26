# -*- coding:utf-8 -*-
import sys
from workflow import Workflow, ICON_WEB, web
from urllib import quote

def main(wf):   
    if len(wf.args):
        query = wf.args[0]
    else:
        exit(0) 
    encode_query = quote(query.encode('utf8'))     #alfred-workflow 仅支持utf8编码

    url = r"http://s.search.bilibili.com/main/suggest?suggest_type=accurate&highlight=&special_acc_num=1&term=%s"%encode_query
    r=web.get(url)
    r = r.json()

    try:
        tags = r['tag']
    except KeyError,e:
        wf.add_item(title=query,
            subtitle='search',
            arg=query,
            valid=True,
            icon=ICON_WEB)
    else:
        for index,tag in tags.items():
            wf.add_item(title=tag['value'],
                     subtitle='search',
                     arg=tag['value'],
                     valid=True,
                     icon='icon.png')

     # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == "__main__":
     wf = Workflow()
     sys.exit(wf.run(main))

   