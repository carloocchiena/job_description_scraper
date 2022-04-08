from collections import Counter
from functools import reduce
import operator

import matplotlib.pyplot as plt
from openpyxl import Workbook
import pandas as pd

from functions import scraper
from stopwords import stopwords_overall

# empty list initiations
word_list = []
clean_list = []
removed = []

# scraper the urls list for the text of each article
with open("urls_list.txt", mode="r", encoding="utf-8") as text:
    for line in text:
        try:
            scraper(line)
        except Exception as e:
            print(f"An error occurred: {e}")

# read the text
with open("raw_text.txt", mode="r", encoding="utf-8") as text:
    for word in text:
        word_list.append(word.split())

# clean the text
for item in reduce(operator.concat, word_list):
  clean_list.append(item.lower())

for word in clean_list[:]:
    if word.lower() in stopwords_overall:
      clean_list.remove(word)
      removed.append(word)

# rank the text
final = (Counter(clean_list))

# create the dataframe
df = pd.DataFrame(data=final, index=[0])

df = (df.T)

# print(df)

df.to_excel('dict1.xlsx')

df.plot()

print("Task done")
