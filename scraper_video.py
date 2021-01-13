#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autor: samuelrg
"""
#%%
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

#chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_argument("disable-infobars")
#chromeOptions.add_argument("--headless") # activar para evitar

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)



time.sleep(1.5)

# url video
urlvideo = "https://www.youtube.com/watch?v=r-WXVFWbOUs"
# Entrar al video
#driver.get(urlvideo)
driver.get(urlvideo)
time.sleep(3)

#extraer info del video
print("Recolectando metadata del video")
meta = []

cname = driver.find_element_by_css_selector("yt-formatted-string.ytd-video-primary-info-renderer:nth-child(1)").text
countViz =driver.find_element_by_css_selector(".view-count").text
fecha1 = driver.find_element_by_css_selector("yt-formatted-string.ytd-video-primary-info-renderer:nth-child(2)").text
likes = driver.find_element_by_css_selector("ytd-toggle-button-renderer.style-scope:nth-child(1) > a:nth-child(1) > yt-formatted-string:nth-child(2)").text
dislike = driver.find_element_by_css_selector("ytd-toggle-button-renderer.style-scope:nth-child(2) > a:nth-child(1) > yt-formatted-string:nth-child(2)").text
duracion  =  driver.find_element_by_css_selector(".ytp-time-duration").text
des = driver.find_element_by_css_selector(".content").text
#ncomen = driver.find_element_by_css_selector(".count-text").text corregir si no tiene comentarios o estan desactivados

dt = {'name': cname,
      'descripcion':des,
      'vistas':countViz,
      'fecha':fecha1,
      'likes':likes,
      'dislikes':dislike,
      'duracion':duracion}

print("Nombre video:{}, Descripcion: {}. Tiene {}, desde {}, {} Me gusta y {} No me gusta, duracion: {}. ".format(cname,des,countViz,fecha1,likes,dislike,duracion))
time.sleep(3)
# cerrar driver
driver.close()
