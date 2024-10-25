import pandas as pd
import numpy as np

urls = pd.read_csv("assets/url.csv").T
for url in urls:
    print(url)