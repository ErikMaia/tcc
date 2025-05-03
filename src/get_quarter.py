import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_quarter():
    quarter = pd.read_csv("assets/trimestre.csv", index_col=0)
    df = pd.DataFrame()
    driver = webdriver.Firefox()
    for col in range(len(quarter)):
        ticker = quarter["name"].tolist()[col]
        url = quarter['url'].tolist()[col]
        t = pd.DataFrame({"ticker": [ticker]})
        driver.get(url)
        tables = driver.find_elements(By.TAG_NAME,"table")
        for table_number, table in enumerate(tables):
            temp = pd.DataFrame()
            match table_number:
                case 0:
                    rows = table.find_elements(By.TAG_NAME,"tr")
                    for row in rows:
                        # print(f"{number_row}: {row.text}")
                        data = row.find_elements(By.TAG_NAME,"td")
                        if len(data) > 2:
                            temp[data[0].text] = [data[1].text]
                            temp[data[2].text] = [data[3].text]
                case _:
                    rows = table.find_elements(By.TAG_NAME,"tr")
                    print(f"Table {table_number}: {len(rows)}")
                    for row in rows:
                        # print(f"{number_row}: {row.text}")
                        cells = row.find_elements(By.TAG_NAME,"td")
                        index = ""
                        for cell in cells:
                            try:
                                cell_value = float(cell.text.replace(",",".").replace(".","").replace("%",""))
                                if index !="":
                                    temp[index] = [cell_value]
                                    t = pd.concat([t,temp],axis="columns")
                            except:
                                index = cell.text
            t = pd.concat([t,temp],axis="columns")
            print(f"Table {table_number}: {t.head()}")
        #     print(f"Tabela {table_number}: {table.text}")
        # rows = driver.find_elements(By.TAG_NAME,"tr")
        # for row in rows[-17:-7]:
        #     # print(f"{number_row}: {row.text}")
        #     data = row.find_elements(By.TAG_NAME,"td")
        #     if len(data) > 2:
        #         temp = pd.DataFrame({data[-2].text : [data[-1].text]})
        #         t = pd.concat([t,temp],axis="columns")
        # table = table[-2]
        # rows = table.find_elements(By.TAG_NAME,"tr")
        # for row in rows:
        #     data = row.find_elements(By.TAG_NAME,"td")
        #     if len(data) > 2:
        #         temp = pd.DataFrame({f"finaceiro: {data[-3].text}": [data[-1].text],f"contabil: {data[-3].text}": [data[-2].text]})
        #         t = pd.concat([temp,t],axis="columns")
        driver.close()
        df = pd.concat([df,t],axis="index")
        df.to_csv("assets/trimestre_data.csv")
    print(df.to_string())
    driver.get()
    
if __name__ == "__main__":
    get_quarter()