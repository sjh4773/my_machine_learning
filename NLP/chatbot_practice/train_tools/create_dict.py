# 챗봇에서 사용하는 사전 파일 생성

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from utils.Preprocess import Preprocess
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
import pickle

# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
    with open(filename, 'rt', encoding='UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:] # 헤더 제거
    return data

# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data('C:/Users/SeoJiHun/chatbot/train_tools/corpus.txt')

# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])
    
# 사전에 사용될 word2index 생성
# 사전의 첫 번째 인덱스에는 OOV 사용


tokenizer = Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()

