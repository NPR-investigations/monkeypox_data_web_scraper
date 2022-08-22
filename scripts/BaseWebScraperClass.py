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
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=chrome_options
                )
        driver.get(self.url)
        self.html = driver.page_source        
        soup = BeautifulSoup(self.html, 'html.parser')        
        return(soup)

    def _get_csv(self):
        df_csv = pd.read_csv(self.url)
        return(df_csv)
        

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
        

        


      
    

