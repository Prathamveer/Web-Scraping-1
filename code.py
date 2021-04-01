from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["v_mag", "proper_name","bayer_designation","distance","spectral_class","mass","radius","luminosity"]
    data=[]
    for i in range(0, 437):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("tr", attrs={"class", "stars"}):
            td_tags = tr_tags.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index ==0:
                    temp_list.append(td_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tags.contents[0])
                    except:
                        temp_list.append("")
            data.append(temp_list)
        with open("scrapping.csv","w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerow(data)

scrape()


