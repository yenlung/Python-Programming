# coding: utf-8
from random import randint, choices, sample
st = '''
我
我的
眼睛
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止
'''
words = st.split('\n')
def poem():
    n = randint(2, 7) # 決定有幾句

    for i in range(n):
        m = randint(2, 5) # 決定每句的長度
        sentence = sample(words, m)
        print(" ".join(sentence))
poem()
