'''
Instructions:
1. Update the list of URLs you'd like to scrape into 'urls_list.txt'
2. Delete 'raw_text.txt' and 'dict1.xlsx'.
3. Run the script (CTRL+ENTER)
4. Download the dict1.xlsx and use it as you like!
'''
from collections import Counter
from functools import reduce
import math
import operator

from nltk import tokenize
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

# rank the text with a straight counter function
final = (Counter(clean_list))

# create the dataframe
df = pd.DataFrame(data=final, index=[0])
df = (df.T)
df.columns = ['Frequency']

# print(df)

df.to_excel('dict1.xlsx')

print("Counter rank done")

# rank the text with a TF-IDF function
# TF-IDF stands for “Term Frequency — Inverse Document Frequency”

with open("raw_text.txt", mode="r", encoding="utf-8") as text:
  doc = text.read().lower()

def check_sent(word, sentences): 
  final = [all([w in x for w in word]) for x in sentences] 
  sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
  return int(len(sent_len))

def get_top_n(dict_elem, n):
  result = dict(sorted(dict_elem.items(), key = operator.itemgetter(1), reverse = True)[:n]) 
  return result

def kw_sentiment(doc):
  
  total_sentences = tokenize.sent_tokenize(doc)
  
  doc = doc.replace(",", "").replace(".","")
  
  words = doc.split()
  
  for word in reversed(words):
      if word in stopwords_overall:
          words.remove(word)
      
  total_word_length = len(words)
  
  total_sent_len = len(total_sentences)

  tf_score = dict(Counter(words))
  
  idf_score = dict(Counter(words))
      
  for k,v in idf_score.items():
      if v > 1:
          idf_score[k] =  check_sent(k, total_sentences)
      else:
          idf_score[k] = 1
    
  # dividing by total_word_length for each dictionary element
  tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
  
  # performing a log and divide
  idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())
  
  tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}

  end_result = get_top_n(tf_idf_score, 10)
    
  print("TF-IDF rank done")
  [print(key,':',value) for key, value in end_result.items()]
    
  return end_result

if __name__ == "__main__":
  kw_sentiment(doc)

kw_sentiment(doc)
