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

    headers = {
        'Connection':'keep-alive',
        'Host':'dd-search.jd.com',
        'Referer':'https://www.jd.com/',
        'User-Agent':r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

    }

    url = r"https://dd-search.jd.com/?ver=2&key=%s"%encode_query
    r=web.get(url,headers=headers)
    r = r.json()

    for row in r:
        if 'keyword' in row:
            wf.add_item(title=row['keyword'],
                subtitle='search',
                arg=query,
                valid=True
                )
   
    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == "__main__":
     wf = Workflow()
     sys.exit(wf.run(main))


   
