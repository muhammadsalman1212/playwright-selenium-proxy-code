import csv
import time
import random
import pandas as pd
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(proxy={
        'server': 'portal.anyip.io:1080:1080',
        'username': 'user_17fc81',
        'password': 'a7b233'
    }, headless=False)



    page = browser.new_page()
    #kineticproxies.com:4137:proxyuser:cUjGf7zh69Ug
    #portal.anyip.io:1080:user_17fc81,type_residential,country_ES,asn_57269:a7b233

    page.goto('https://www.whatismyip.com/', timeout=0)

    time.sleep(10000000)



