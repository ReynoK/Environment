# -*- coding:utf-8 -*-
import sys
from workflow import Workflow, ICON_WEB, web
from urllib import quote
import webbrowser
def main():
    url = 'https://github.com/login/oauth/authorize?client_id={client_id}&scope={scope}'.format(client_id='8834cac826faabc16135', scope='repo')
    webbrowser.open(url)


if __name__ == '__main__':
    main()
