import traceback
from webbrowser import get
from bs4 import BeautifulSoup
import requests
from requests import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from time import sleep
import pandas as pd
import winsound
from tools import user_agent, check_response, flattened_list, lightning_scraping, get_ua


website_url = "https://www.trustpilot.com/categories/car_dealer?page=6"
selenium = True
team = "Greece"

if selenium:
    opt = Options()
    path = Service("c:\\users\\chromedriver.exe")
    selenium_arguments = ["window-size=1400,900", '--silent', '--no-sandbox', 'disable-notifications', '--disable-dev-shm-usage', '--disable-gpu']
    opt.add_experimental_option("detach", True)
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.headless = True
    for arg in selenium_arguments:
        opt.add_argument(arg)
    

    driver = webdriver.Chrome(service=path, options=opt)   
    

    dealers_name = []
    total_reviews = []
    star_logo = []
    dealers_trustscores = []
    review_links = []


    url_lists = []
    for num in range(1, 7):
        url = f"https://www.trustpilot.com/categories/car_dealer?page={num}"
        url_lists.append(url)


    def automation(urls):       
        driver.maximize_window()
        driver.get(urls)

        datas = WebDriverWait(driver, 10).until((EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[name=business-unit-card]'))))
        
        for data in datas:
            try:
                name = data.find_element(By.TAG_NAME, 'p').text.strip()
                rev_links = (data.get_attribute('href'))
            except NoSuchElementException:
                name = "N/A"
                rev_links = "N/A"
            

            dealers_reviews = data.find_elements(By.TAG_NAME, 'p')

            try:
                tots_reviews = dealers_reviews[-1].text.strip().split("|")[-1]
            except NoSuchElementException:
                tots_reviews = "N/A"
            

            dealers_ratings_data = data.find_elements(By.CLASS_NAME, 'styles_rating__2FRLX')

            for deal in dealers_ratings_data:
                try:
                    sta_logo = deal.find_element(By.TAG_NAME, 'img').get_attribute('src')
                except NoSuchElementException:
                    sta_logo = "N/A"
               
                # star_text = deal.find_element(By.TAG_NAME, 'img').get_attribute('alt')

                try:
                    deals_trustscores = deal.find_element(By.CLASS_NAME, 'styles_desktop__3N0-b').text.strip()
                except NoSuchElementException:
                    deals_trustscores = "N/A"
                
                return name, rev_links, tots_reviews, sta_logo, deals_trustscores
        

    for link in url_lists:
        trust_datas = automation(link)

        dealers_name.append(trust_datas[0])
        review_links.append(trust_datas[1])
        total_reviews.append(trust_datas[2])
        star_logo.append(trust_datas[3])
        dealers_trustscores.append(trust_datas[4])

            
               

    # print(automation())
        
    # sleep(5)
    # lightning_scraping(automation, url_lists)
    print(len(dealers_name))
    print(len(total_reviews))
    print(len(star_logo))
    print(len(dealers_trustscores))
    print(len(review_links))

    winsound.PlaySound('notification.mp3', winsound.SND_FILENAME)

    d = {"Dealer's Name": dealers_name,
         "Trustscores": dealers_trustscores,
         "Stars": star_logo,
         "Total Reviews": total_reviews,
         "Review Links": review_links

    }
    df = pd.DataFrame(data=d)
    df.to_json("Trustpilot Car dealer database.json", indent=4)
    df.to_excel("Trustpilot Car dealer database.xlsx", index=False)
    
else:


    def beautiful_soup():
        pass
        

    print(beautiful_soup())
    

    
    # print(check_response(website_url))


