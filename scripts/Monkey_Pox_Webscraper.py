from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import time
from datetime import date
import json
from tqdm import tqdm
import requests
import pathlib

from BaseWebScraperClass import BaseWebscraper
from MonkeyPoxDataWebsitesClass import monkeyPoxWebsites

class scrapeDosesByState(BaseWebscraper):
    def __init__(self, url, scraper_type, data_directory):
        super().__init__(url,scraper_type, data_directory)
    def scrape(self,name,save_folder):
        # Isolate Element        
        table_element = self.soup.find("table")
        # Get data
        doses_data = self._get_table(table_element)
        text_data = self._text_from_html()
        # Save data   
        today = date.today()
        today_formated = today.strftime("%Y-%m-%d")     
        ## Save csv --------------------               
        self._save_csv(doses_data, name+ "_table" +"_current", save_folder) # always up to date file
        self._save_csv(doses_data, name+"_table" + f"_{today_formated}", save_folder + "/daily"+f"/{today_formated}") # folders for specific days
        ## Save txt --------------------
        self._save_txt(text_data, name+"_text" +"_current", save_folder)  # always up to date file
        self._save_txt(text_data, name+"_text"+ f"_{today_formated}", save_folder + "/daily"+f"/{today_formated}") # folders for specific days


class scrapeCasesByStateCSV(BaseWebscraper):
    def __init__(self, url, scraper_type, data_directory):
        super().__init__(url,scraper_type, data_directory)
    def scrape(self,name,save_folder):        
        # Get data
        cases_data = self._get_csv()
     
        # Save data   
        today = date.today()
        today_formated = today.strftime("%Y-%m-%d")     
        ## Save csv --------------------               
        self._save_csv(cases_data, name+ "_table" +"_current", save_folder) # always up to date file
        self._save_csv(cases_data, name+"_table" + f"_{today_formated}", save_folder + "/daily"+f"/{today_formated}") # folders for specific days
    

class scrapeCasesByStateText(BaseWebscraper):
    def __init__(self, url, scraper_type, data_directory):
        super().__init__(url,scraper_type, data_directory)
    def scrape(self,name,save_folder):        
        # Get data
        text_data = self._text_from_html()
     
        # Save data   
        today = date.today()
        today_formated = today.strftime("%Y-%m-%d")     
                     
        ## Save txt --------------------
        self._save_txt(text_data, name+"_text" +"_current", save_folder)  # always up to date file
        self._save_txt(text_data, name+"_text"+ f"_{today_formated}", save_folder + "/daily"+f"/{today_formated}") # folders for specific days

        
        



# Doses by State --------------------
doses_by_state = scrapeDosesByState(monkeyPoxWebsites.doses_by_state_url,"requests","./data/")
doses_by_state.scrape("doses_by_state", "doses_by_state_data")

# Cases by State -------------------
cases_by_state_csv = scrapeCasesByStateCSV(monkeyPoxWebsites.cases_by_state_csv_url,"requests","../data/data_directory/")
cases_by_state_csv.scrape("cases_by_state", "cases_by_state_data")

cases_by_state_txt = scrapeCasesByStateText(monkeyPoxWebsites.cases_by_state_text_url,"selenium","../data/data_directory/")
cases_by_state_txt.scrape("cases_by_state", "cases_by_state_data")

