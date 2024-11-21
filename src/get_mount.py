import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_mount():
    mount = pd.read_csv("assets/mes.csv")
    df = pd.DataFrame()
    for col in range(len(mount)):
        driver = webdriver.Firefox()
        t = pd.DataFrame({"ticker": [mount["name"][col]]})
        driver.get(mount['url'][col])
        rows = driver.find_elements(By.TAG_NAME,"tr")[11:-4]
        for row in rows:
            # print(f"{number_row}: {row.text}")
            data = row.find_elements(By.TAG_NAME,"td")
            temp = pd.DataFrame({data[-2].text : [data[-1].text]})
            t = pd.concat([t,temp],axis="columns")
        driver.close()
        df = pd.concat([df,t],axis="index")
        df.to_csv("assets/mes_data.csv")
    print(df.to_string())
    # driver.get()
    
if __name__ == "__main__":
    get_mount()