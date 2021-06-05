import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import json

file_tag_names = open("tag_names.json")
tag_names = json.load(file_tag_names)

url = tag_names["bongard_problems_solutions"]
url_root = tag_names["root"]
source = urllib.request.urlopen(url).read()

soup = BeautifulSoup(source, 'html.parser')
table = soup.find_all("table", id="table2")[0]
tr_table = table.find_all("tr")

col_url = []
col_id = []
col_left = []
col_right = []
name_cols = []

for ix_line, tr in enumerate(tr_table):
    if ix_line <= 100:
        if ix_line == 0:
            for c in tr.find_all("font"):
                name_cols.append(c.text)
        else:
            for i, c in enumerate(tr.find_all("font")):
                if i == 0:
                    col_url.append((url_root+c.find("a").get("href")).replace(".htm", ".gif"))
                    col_id.append(" ".join(c.text.replace("\n", " ").split()))
                elif i == 1:
                    col_left.append(" ".join(c.text.replace("\n", " ").split()))
                else:
                    col_right.append(" ".join(c.text.replace("\n", " ").split()))
    else: break


df = pd.DataFrame()
df["URL"] = pd.Series(col_url)
df[name_cols[0]] = pd.Series(col_id)
df[name_cols[1]] = pd.Series(col_left)
df[name_cols[2]] = pd.Series(col_right)
df.to_excel("BP_collection.xlsx")
