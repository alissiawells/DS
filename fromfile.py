# -*- coding: utf-8 -*-
import vk_api
import re
import time

def auth_handler():
    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True
    return key, remember_device

def main():
    login, password = '', ''
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler  
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    tools = vk_api.VkTools(vk_session)

    id = []
    dom = []
    with open('filewithlinks.txt', 'r') as f:
        links = f.readlines()
        for link in links:
            link = re.sub('https?:\/\/vk\.com\/[publicevnt]*', '', link).strip()
            if link.isdigit():
                link = str(-1*link)
                wall = tools.get_all('wall.get', 100, {'owner_id': str(link)})
            else:
                wall = tools.get_all('wall.get', 100, {'domain': link})
            print(wall['count'])
            with open('%s.txt' % link, 'a') as f: 
                for post in wall['items']:
                    f.write(post['text'])
            time.sleep(0.5)

if __name__ == '__main__':
    main()
