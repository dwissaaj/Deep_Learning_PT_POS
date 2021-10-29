import pandas as pd
import openpyxl
import re
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer(strip_handles=True)
import unicodedata
df = pd.read_excel("pos indo aji.xlsx")

df['text'] = df['text'].fillna('').apply(str)
df['text'] = df['text'].replace({'"':'',
                                 '\d+':'',
                                 ':':'',
                                 ';':'',
                                 '#':'',
                                 '@':'',
                                 '_':'',
                                 ',': '',
                                 "'": '',
                                  }, regex=True)

df['text'] = df['text'].str.replace(r'[https]+[?://]+[^\s<>"]+|www\.[^\s<>"]+[?()]+[(??)]+[)*]+[(\xa0]+[-&gt...]', "",regex=True)

df['text'] = df['text'].replace('\n','', regex=True)

df['text'] = df['text'].replace({'\.':'','(/)':'','\(':'','\)':''},regex=True)
df['text'] = df['text'].replace('[\.:"]','',regex =True)

df['text'] = df['text'].fillna('').apply(str)
df['text'] = re.sub("\s\s+", " ", df['text'])
#df['text'] = "".join(c for c in s if unicodedata.category(c) not in ["No", "Lo"])
