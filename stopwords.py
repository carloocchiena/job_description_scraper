import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')


# create our custom stopwords list
symbols = ["!","'","£","$","%","&","(",")","?","^","*","+","/","-", "©", "·", "•", "|", "-", "–"]

cookie = ["cookie", "navigazione", "sito", "consenso", "navigazione", "accetta", "rifiuta", "gestisci", "utilizziamo", "funzionali", "tecnici", "informativa", "preferenze"]

stopwords_overall = stopwords.words('italian')  + stopwords.words('english') + symbols + cookie
