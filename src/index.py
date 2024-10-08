from typing import List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


import pandas as pd

type_of_investiment = ""

def get_fin_table(table:WebElement)->pd.DataFrame:
    data_fragment = {}
    rows = table.find_elements(By.TAG_NAME, "tr")
    print(f"Número de linhas: {len(rows)}")
    for row in rows:
        # print(row.text)
        values = row.find_elements(By.TAG_NAME,"td")
        number_of_cell = len(values)
        print(number_of_cell)
        if number_of_cell > 0:
            data_fragment[f"{values[0].text} financeiro"] = [values[-2].text]
            data_fragment["{values[0].text}  contabil"] = [values[-1].text]
            data = pd.DataFrame(data=data_fragment)
            # print(data.head().to_string())
    return data

def show_exemples(table:WebElement):
    data = pd.DataFrame()
    rows = table.find_elements(By.TAG_NAME, "tr")
    # print(f"Número de linhas: {len(rows)}")
    for row in rows:
        # print(row.text)
        values = row.find_elements(By.TAG_NAME,"td")
        number_of_cell = len(values)
        # print(number_of_cell)
        string = "\n"
        for value in values:
            string += "|" + value.text
        print(string + "|")
    return data


# Calculos para cra: soma, desvio padrão, número de contador. 
def get_investiments_data(table:WebElement)->pd.DataFrame:
    rows = table.find_elements(By.CSS_SELECTOR,"tr")
    counter = len(rows)
    investiments = table.find_elements(By.CSS_SELECTOR,"th")
    for i, investiment in enumerate(investiments):
        print(f"[{i}]: {investiment.text}")
    s = 0
    if(counter <= 2):
        print(table.text)
        return pd.DataFrame()
    
    data_fragmente = {}
    sum = 0.0
    for row in rows:
        values = row.find_elements(By.CSS_SELECTOR,"td")
        print(row.text + str(len(values)))
        if (len(values) > 0 and "R" not in values[-1].text and values[-1].text != ''):
            sum_std = values[-1].text.replace(".","").replace(",",".")
            print(sum_std)
            sum = float(sum_std) + sum 


    mean = sum / len(rows)
    for row in rows:
        values = row.find_elements(By.TAG_NAME,"td")
        if (len(values) > 0 and "R" not in values[-1].text and values[-1].text != ''):
            print(values[-1].text)
            monetary_value = float(values[-1].text.replace(",",".").replace(".",""))
            s += monetary_value - mean if monetary_value > mean else mean - monetary_value
    data_fragmente["cra_sum"] = [sum]
    # data_fragmente["cra_"]
    data = pd.DataFrame(data=data_fragmente)
    print(data.head().to_string())
    return data

def get_last_table(table:WebElement):
    data_fragment = {}
    rows = table.find_elements(By.TAG_NAME, "tr")
    print(f"Número de linhas: {len(rows)}")
    for row in rows:
        # print(row.text)
        values = row.find_elements(By.TAG_NAME,"td")
        number_of_cell = len(values)
        # print(number_of_cell)
        if number_of_cell > 1:
            # print(f"[{values[1].text}]: {values[-1].text}")
            data_fragment[values[1].text] = [values[-1].text]
            # data[values[1].text] = values[-1].text
            print(data_fragment)
    data_set = pd.DataFrame(data=data_fragment)
    print(data_set.head().to_string())
    return data_set


def get_first_table(table:WebElement):
        
    data_fragment = {}
    rows:List[WebElement] = table.find_elements(By.TAG_NAME, "td")

    for i in range(int(len(rows)/2)-1):
        # print(f"interação {i} = [{rows[i*2].text}]:{rows[i*2+1].text}")
        data_fragment[rows[i*2].text] = [rows[i*2+1].text]
    return pd.DataFrame(data=data_fragment)

    
def get_data_by_url(url:str)->pd.DataFrame:
    driver = webdriver.Firefox()
    driver.get(url)
    tables = driver.find_elements(By.TAG_NAME, "table")
    data = pd.DataFrame()
    # data = get_first_table(tables[0])
    for i, table in enumerate(tables[2:33]):
        # print(f"\n\n\ntabela {i+2}\n {table.text}")
        data = pd.concat([data,get_investiments_data(table)], axis=0)
        
    # for i in range(9,14):
    #     # print(f"Tabela {i}")
    #     data = pd.concat([data,get_fin_table(tables[-i])], axis=1)
    # for i in range(4,8):
    #     # print('tabela: ' + str(i))
    #     data = pd.concat([data, get_last_table(tables[-i])], axis=1)
    driver.close()
    print(data.loc[:1].to_string())
    return data
    
    
def main():
    urls = pd.read_csv('assets/url.csv')
    
    for url in urls['url'][2:3]:
        print(url)
        get_data_by_url(url)
        
if __name__ == "__main__":
    main()
    # get_data_by_url("https://fnet.bmfbovespa.com.br/fnet/publico/exibirDocumento?id=718970&cvm=true")