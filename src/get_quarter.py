import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_mount():
    mount = pd.read_csv("assets/trimestre.csv")
    df = pd.DataFrame()
    for col in range(len(mount)):
        driver = webdriver.Firefox()
        t = pd.DataFrame({"ticker": [mount["name"][col]]})
        driver.get(mount['url'][col])
        tables = driver.find_elements(By.TAG_NAME,"table")
        for table_number, table in enumerate(tables):
            print(f"Tabela {table_number}: {table.text}")
    #     rows = driver.find_elements(By.TAG_NAME,"tr")
    #     for row in rows[-17:-7]:
    #         # print(f"{number_row}: {row.text}")
    #         data = row.find_elements(By.TAG_NAME,"td")
    #         if len(data) > 2:
    #             temp = pd.DataFrame({data[-2].text : [data[-1].text]})
    #             t = pd.concat([t,temp],axis="columns")
    #     table = table[-2]
    #     rows = table.find_elements(By.TAG_NAME,"tr")
    #     for row in rows:
    #         data = row.find_elements(By.TAG_NAME,"td")
    #         if len(data) > 2:
    #             temp = pd.DataFrame({f"finaceiro: {data[-3].text}": [data[-1].text],f"contabil: {data[-3].text}": [data[-2].text]})
    #             t = pd.concat([temp,t],axis="columns")
    #     driver.close()
    #     df = pd.concat([df,t],axis="index")
    #     df.to_csv("assets/trimestre_data.csv")
    # print(df.to_string())
    # driver.get()
    
if __name__ == "__main__":
    get_mount()