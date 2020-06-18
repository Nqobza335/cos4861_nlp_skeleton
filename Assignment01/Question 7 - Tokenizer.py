# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:46:45 2020

@author: Olorato
"""

sent1 = "I can't do this. I won't do that."

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer("[\w']+")

#Run the below section to test the above
tokenizer.tokenize(sent1)
