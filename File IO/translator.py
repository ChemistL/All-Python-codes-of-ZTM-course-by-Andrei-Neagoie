# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:49:36 2020

@author: saura
"""
from translate import Translator

translator= Translator(to_lang="ja")
try: 
with open('translate.txt', mode = 'r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    with open('./test-ja.txt', mode = 'w') as my_file2

print(translation)
