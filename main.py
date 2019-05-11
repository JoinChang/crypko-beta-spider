from selenium import webdriver
import time
import re
import urllib.request
import json
import os
from selenium.webdriver.chrome.options import Options

def main():
   # crypkoImage()
    crypkoJson(1, 712045)

def crypkoJson(a, b):
    num_dl = 0
    num_all = 0
    num_skip = 0
    for inumber in range(a, b):
		num_all = num_all + 1;
        number = str(inumber)
        if os.access("source/" + number + ".json", os.F_OK):
            print(number + ": Skip");
            num_skip = num_skip + 1;
        else:
            '''
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get("https://api.crypko.ai/crypkos/" + number + "/detail")
            # print(driver.page_source)
            content = re.findall(r'<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">(.+)</pre></body></html>',driver.page_source)
            with open('source/' + number + '.json','w') as file_obj:
                for element in content:
                    json.dump(element, file_obj)
                    # print("数据: " +  element)
                    print(number)
            file_obj.close()
            driver.close()
'''
            try:
                response = urllib.request.urlopen("https://api.crypko.ai/crypkos/" + number + "/detail", timeout=10)
                obj = json.loads(response.read())
                with open('source/' + number + '.json', 'w') as file_obj:
                    json.dump(obj, file_obj)
                    print(number + ": Done")
                    num_dl = num_dl + 1;
            except:
                print("Warning: Timeout")
                crypkoJson(inumber, b)
                return
    print("OverAll: " + str(num_all) + " / Skip: " + str(num_skip) + " / Download: " + str(num_dl))

def crypkoImage():
    for number in range(10,20):
        number = str(number)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        link = "https://crypko.ai/#/card/" + number
        driver.get(link)
        time.sleep(5)
        print(driver.page_source)
        content = re.findall(r'<img class="progressive-image-main" src="(.+)" style="" />',driver.page_source)
        driver.close()
        del content[1]
        print('编号: ' + number)
        for element in content:
            print('图片地址: ' + element)
            urllib.request.urlretrieve(element, 'source/' + number + '.jpg')


if __name__ == '__main__':
    main()