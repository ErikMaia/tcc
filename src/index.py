from typing import List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

import pandas as pd

def get_fin_table(table:WebElement):
    data = pd.DataFrame()
    rows = table.find_elements(By.TAG_NAME, "tr")
    print(f"Número de linhas: {len(rows)}")
    for row in rows:
        # print(row.text)
        values = row.find_elements(By.TAG_NAME,"td")
        number_of_cell = len(values)
        print(number_of_cell)
        if number_of_cell > 0:
            data[values[0].text + " financeiro"] = values[-2].text
            data[values[0].text + " contabil"] = values[-1].text
    return data

def show_exemples(table:WebElement):
    data = pd.DataFrame()
    rows = table.find_elements(By.TAG_NAME, "tr")
    print(f"Número de linhas: {len(rows)}")
    for row in rows:
        # print(row.text)
        values = row.find_elements(By.TAG_NAME,"td")
        number_of_cell = len(values)
        print(number_of_cell)
        string = "\n"
        for value in values:
            string += "|" +value.text
        print(string + "|")
    return data

def get_last_table(table:WebElement):
    data = pd.DataFrame()
    rows = table.find_elements(By.TAG_NAME, "tr")
    print(f"Número de linhas: {len(rows)}")
    for row in rows:
        # print(row.text)
        values = row.find_elements(By.TAG_NAME,"td")
        number_of_cell = len(values)
        print(number_of_cell)
        if number_of_cell > 1:
            print(f"[{values[1].text}]: {values[-1].text}")
            data[values[1].text] = values[-1].text
    return data

def get_first_table(table:WebElement):
        
    data = pd.DataFrame()
    rows:list = table.find_elements(By.TAG_NAME, "td")

    for i in range(int(len(rows)/2)-1):
        # print(f"interação {i} = [{rows[i*2].text}]:{rows[i*2+1].text}")
        data[rows[i*2].text] = rows[i*2+1].text
    data.head()
    return data

    
def get_data_by_url(url:str):
    driver = webdriver.Firefox()
    driver.get(url)
    tables = driver.find_elements(By.TAG_NAME, "table")
    # get_first_table(tables[0])
    for i, table in enumerate(tables[2:33]):
        print(f"tabela {i+2}")
        show_exemples(table)
        
    # for i in range(9,14):
    #     print(f"Tabela {i}")
    #     get_fin_table(tables[-i])
    # for i in range(4,8):
    #     print('tabela: ' + str(i))
    #     get_last_table(tables[-i])
    driver.close()
    
if __name__ == "__main__":
    get_data_by_url("https://fnet.bmfbovespa.com.br/fnet/publico/exibirDocumento?id=718970&cvm=true")