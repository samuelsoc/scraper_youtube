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
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

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
dt = {'name': cname,
      'vistas':countViz,
      'fecha':fecha1,
      'likes':likes,
      'dislikes':dislike,
      'duracion':duracion}

print("Nombre video:{}, tiene {}, desde {}, {} Me gusta y {} No me gusta, duracion: {}".format(cname,countViz,fecha1,likes,dislike,duracion))
time.sleep(3)
# cerrar driver
driver.close()
