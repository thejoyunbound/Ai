from django.shortcuts import render
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import time

# Create your views here.

def crawling(request):
    search = request.GET.get('word')
    if search == None:
        contents = {'result':None}
    else:
        driver = webdriver.Chrome('C:\work\www1\chromedriver.exe')
        url = "https://www.google.co.kr/imghp?hl=ko&ogbl"
        driver.get(url)
        elem = driver.find_element(By.NAME, 'q')
        search_img = search
        elem.send_keys(search_img)
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(1)
        images = driver.find_elements(By.CSS_SELECTOR,'.rg_i.Q4LuWd')
        cnt = 1
        for image in images:
            image.click()
            driver.implicitly_wait(1)
            try:
                img_url = driver.find_element(By.CSS_SELECTOR, '.n3VNCb').get_attribute('src')
                urlretrieve(img_url,search+str(cnt)+'.jpg')
                cnt += 1
            except:
                pass
        contents = {
            'result':cnt
        }
        driver.close()

    return render(request,'crawling.html',contents)