import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

dfs = []
def get_mount(mount:pd.DataFrame):
    columns = mount.columns
    df = pd.DataFrame()
    size = len(mount)
    if size == 0:
        return pd.DataFrame()
    if mount.empty:
        return pd.DataFrame()
    driver = webdriver.Firefox()
    for col in range(size):
        print(mount.head())
        ticker = mount["name"].tolist()[col]
        t = pd.DataFrame({"ticker": [ticker]})
        urls = mount['url'].tolist()
        driver.get(urls[col])
        rows = driver.find_elements(By.TAG_NAME,"tr")[11:-4]
        for row in rows:
            # print(f"{number_row}: {row.text}")
            data = row.find_elements(By.TAG_NAME,"td")
            temp = pd.DataFrame({data[-2].text : [data[-1].text]})
            t = pd.concat([t,temp],axis="columns")
        df = pd.concat([df,t],axis="index")
        df.to_csv("assets/mes_data.csv")
    print(df.to_string())
    dfs.append(df)
    driver.close()
    # driver.get()
    
if __name__ == "__main__":
    mount = pd.read_csv("assets/mes.csv", index_col=0)
    size = mount.shape[0]
    threads = []
    number_of_browser = 4
    for i in range(0,size, size//number_of_browser):
        print(f"Thread {i} - {i+size//number_of_browser}")
        t = threading.Thread(target=get_mount, args=(mount.iloc[i:i+size//number_of_browser].copy(deep=True),))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    
    mount_data = pd.concat(dfs,axis="index")
    mount_data = mount_data.reset_index(drop=True)
    mount_data.to_csv("assets/mes_data.csv")
    mount_data.loc[mount_data.isna()] = 0
    mount_data.to_csv("assets/mes_data.csv")