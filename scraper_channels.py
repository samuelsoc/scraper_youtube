#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autor: samuelrg
"""
#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import os
import time
import datetime
from webdriver_manager.chrome import ChromeDriverManager

import random
import pandas as pd
#%%

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-setuid-sandbox")
chromeOptions.add_argument("--remote-debugging-port=9222")  # this
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("--headless") # activar para evitar


driver = webdriver.Chrome(chrome_options=chromeOptions)

# Open pag
canal ="BancoEstado"
urlcanal = "https://www.youtube.com/c/"+canal+"/videos"
infocanal = "https://www.youtube.com/c/"+canal+"/about"
infocanal
# Esta es la url info canal
driver.get(infocanal)
time.sleep(3)

#extraer info del canal
print("Recolectando metadata del canal")
meta = []

cname = driver.find_element_by_css_selector("ytd-channel-name.ytd-c4-tabbed-header-renderer > div:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(1)").text
suscript =driver.find_element_by_css_selector("#subscriber-count").text
fecha1 = driver.find_element_by_css_selector("span.yt-formatted-string:nth-child(2)").text
visits = driver.find_element_by_css_selector("yt-formatted-string.ytd-channel-about-metadata-renderer:nth-child(3)").text
dt = {'name': cname,
      'suscriptores':suscript,
      'inicio_canal':fecha1,
      'visualizaciones':visits}

print("Nombre Canal:{}, tiene {}, desde {}, y {}".format(cname,suscript,fecha1,visits))
time.sleep(3)
# ir a lista de videos
print("Recorriendo todos los videos... ")
driver.get(urlcanal)

def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1.5)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

scroll_to_bottom(driver)

# extraer links de videos
print("Recolectando links de videos")
links1 = driver.find_elements_by_css_selector("a.ytd-grid-video-renderer")
links2 = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),links1)))

links = pd.DataFrame(links2, columns=['links'])
links.to_csv("/home/samuelrg/scrapIG/youtube/"+canal+'_listadovideos.csv')
print("{} links recolectados".format(len(links2)))
print("Se cerrará en 5 segundos")

time.sleep(5)
# cerrar driver
driver.close()
