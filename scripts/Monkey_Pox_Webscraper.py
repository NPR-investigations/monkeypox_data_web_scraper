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

class BaseWebscraper():
    def __init__(self,url, scraper_type, data_directory):
        self.url = url
        self.parent_directory = pathlib.Path(data_directory)  

        if scraper_type == "requests":      
            self.soup = self._make_request_soup()
        if scraper_type == "selenium":
            self.soup = self._make_selenium_soup()
        

    def _make_request_soup(self):
        r = requests.get(self.url)
        self.html = r.content
        soup = BeautifulSoup(self.html, 'html.parser')        
        return(soup)

    def _make_selenium_soup(self):

        chrome_options = Options()
        #chrome_options.add_argument(f'--proxy-server=188.138.11.39')
        driver = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=chrome_options
                )
        driver.get(self.url)
        self.html = driver.page_source        
        soup = BeautifulSoup(self.html, 'html.parser')        
        return(soup)
        

    def _get_table(self, table_element):
        ls_table_tr = table_element.find_all("tr")
        rows = []
        for tr in ls_table_tr:
            row = []
            count = 0
            for child in tr.children:
                if count == 0:
                    result = child.text.replace('\n', '')
                    if result != "":
                        row.append(result)
                else: 

                    try:
                        row.append(child.text.replace('\n', ''))
                    except:
                        continue

            count = count + 1
            if len(row) > 0:
                rows.append(row)
        df = pd.DataFrame(rows[1:], columns = rows[0])
        self.df_table = df
        return(self.df_table)

    def _tag_visible(self,element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'table']:
            return False
        if isinstance(element, Comment):
            return False
        return True


    def _text_from_html(self):
    
        texts = self.soup.findAll(text=True)
        visible_texts = filter(self._tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)

    def _save_file(self, save_folder):
        self.file_path = self.parent_directory.joinpath(save_folder)
        self.file_path.mkdir(parents=True, exist_ok=True)
        

    def _save_csv(self,df,name, save_folder):
        self._save_file(save_folder)
        full_name = name + ".csv"        
        file_path_final = self.file_path.joinpath(full_name)
        df.to_csv(file_path_final, index = False)

    def _save_txt(self,text,name, save_folder):
        self._save_file(save_folder)
        full_name = name + ".txt"        
        file_path_final = self.file_path.joinpath(full_name)
        

        with open(file_path_final, 'w', encoding='utf-8') as f:
            f.write(text)
            
class monkeyPoxWebsites():
    doses_by_state_url = "https://aspr.hhs.gov/SNS/Pages/JYNNEOS-Distribution.aspx"
    cases_by_state_url = "https://www.cdc.gov/poxvirus/monkeypox/response/2022/us-map.html"


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
        self._save_txt(text_data, name+"_text_" +"_current", save_folder)  # always up to date file
        self._save_txt(text_data, name+"_text_"+ f"_{today_formated}", save_folder + "/daily"+f"/{today_formated}") # folders for specific days



doses_by_state = scrapeDosesByState(monkeyPoxWebsites.doses_by_state_url,"requests","../data/data_directory/")
doses_by_state.scrape("doses_by_state", "doses_by_state_data")
