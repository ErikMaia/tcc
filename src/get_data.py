from typing import List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import threading
import yfinance

import pandas as pd

def get_fin_table(table:WebElement)->pd.DataFrame:
    data_fragment = {}
    rows = table.find_elements(By.CSS_SELECTOR, "tr")
    
    for row in rows:
        values = row.find_elements(By.CSS_SELECTOR,"td")
        number_of_cell = len(values)
        if number_of_cell > 0:
            data_fragment[f"{values[0].text.replace(" ", "")}_financeiro"] = [float(values[-2].text.replace(".","").replace(",",".")) if values[-2].text != "" else 0]
            data_fragment[f"{values[0].text.replace(" ", "")}_contabil"] = [float(values[-1].text.replace(".","").replace(",",".")) if values[-1].text != "" else 0]
    data = pd.DataFrame(data=data_fragment)
    # print(data)
    return data

# Calculos para cra: soma, desvio padrão, número de contador. 
def get_investments_data(table:WebElement)->pd.DataFrame:
    rows = table.find_elements(By.CSS_SELECTOR,"tr")
    counter = len(rows)
    investiments = table.find_elements(By.CSS_SELECTOR,"th")
    match len(investiments):
        case 0:
            investiment = "qualquer"
            
        case 1:
            investiment = investiments[0].text
        
        case 2:
            investiment = investiments[0].text
    
    s = 0
    if(counter <= 2):
        return pd.DataFrame()
    
    data_fragmente = {}
    _sum = 0.0
    count = 0
    for row in rows:
        values = row.find_elements(By.CSS_SELECTOR,"td")
        if (len(values) > 0 and "R" not in values[-1].text and values[-1].text != ''):
            try:
                sum_std = values[-1].text.replace(".","").replace(",",".").replace('%','')
                _sum = float(sum_std) + _sum 
            except:
                print(f"Erro de converção em {values[-1].text}")
            finally:
                count = 1 + count
                


    mean = _sum / count
    for row in rows:
        values = row.find_elements(By.TAG_NAME,"td")
        if (len(values) > 0 and "R" not in values[-1].text and values[-1].text != ''):
            try:
                monetary_value = float(values[-1].text.replace(",",".").replace(".","").replace("%",""))
                s += monetary_value - mean if monetary_value > mean else mean - monetary_value
            except:
                print(f"Erro em {values[-1].text}")

    data_fragmente[f"{investiment} sum"] = [_sum]
    data_fragmente[f"{investiment} mean"] = [_sum/count]
    data_fragmente[f"{investiment} count"] = [count]
    data_fragmente[f"{investiment} stdr"] = [s/count]
    data = pd.DataFrame(data=data_fragmente)
    # print(data)
    return data

def get_last_table(table:WebElement):
    data_fragment = {}
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        values = row.find_elements(By.TAG_NAME,"td")
        number_of_cell = len(values)
        if number_of_cell > 1 and values[-1].text != '':
            data_fragment[values[1].text] = [float(values[-1].text.replace(",",".").replace(".","").replace('%',''))]
    data_set = pd.DataFrame(data=data_fragment)
    return data_set


def get_first_table(table:WebElement):
        
    data_fragment = {}
    rows:List[WebElement] = table.find_elements(By.TAG_NAME, "td")

    for i in range(int(len(rows)/2)-1):
        data_fragment[rows[i*2].text.replace(" ","").replace('\n','')] = [rows[i*2+1].text.replace(" ","")]
    return pd.DataFrame(data=data_fragment)

    
def get_data_by_url(url:str)->pd.DataFrame:
    driver = webdriver.Firefox()
    driver.get(url)
    tables = driver.find_elements(By.TAG_NAME, "table")
    data = [get_first_table(tables[0])]
    # for i, table in enumerate(tables[2:33]):
    #     data.append(get_investments_data(table))
    for i in range(9,14):
        data.append(get_fin_table(tables[-i]))
    for i in range(4,8):
        data.append(get_last_table(tables[-i]))
    driver.close()
    df = pd.concat(data, axis="columns")
    return df
    
    
def main():
    urls = pd.read_csv('assets/trimestre.csv')
    df = pd.DataFrame()
    for i, url in enumerate(urls['url']):
        new_data = get_data_by_url(url)
        df = pd.concat([df,new_data])
        df[df.isna()] = 0
        df.to_csv('/home/erik/Área de trabalho/tcc/assets/dados1.csv',index=False)
        # data.append(new_data)
        # print(f"Tabela {i+1}-{len(urls)}: OK")
    # df = pd.concat(data, keys=range(len(data)),verify_integrity=False, ignore_index=True, join="inner")
    # df.to_csv('/home/erik/Área de trabalho/tcc/assets/dados.csv',index=False)

        
if __name__ == "__main__":
    main()
    # get_url()