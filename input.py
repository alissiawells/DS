# -*- coding: utf-8 -*-
import vk_api
import re
import time

def main():
    vk_session = vk_api.VkApi(token='')

    tools = vk_api.VkTools(vk_session)

    domain = str(input())
    wall = tools.get_all('wall.get', 100, {'domain': domain})
    with open('%s.txt' % domain, 'a') as f: 
        for post in wall['items']:
            f.write(post['text'])
    # time.sleep(0.5)

if __name__ == '__main__':
    main()
