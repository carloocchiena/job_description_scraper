from collections import Counter
from functools import reduce
import operator

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

import pandas as pd
from openpyxl import Workbook

custom = ["!","'","£","$","%","&","(",")","?","^","*","+","/","-", "©", "·", "•", "|"] 
 # add further words to be excluded
stopwords_overall = stopwords.words('italian')  + stopwords.words('english') + custom

job_list = []
clean_list = []
removed = []

with open("job description.txt", mode="r", encoding="utf-8") as text:
    for word in text:
        job_list.append(word.split())

for item in reduce(operator.concat, job_list):
  clean_list.append(item)

for word in clean_list[:]:
    if word.lower() in stopwords_overall:
      clean_list.remove(word)
      removed.append(word)

final = (Counter(clean_list))

df = pd.DataFrame(data=final, index=[0])

df = (df.T)

# print(df)

df.to_excel('dict1.xlsx')

print("Task done")
