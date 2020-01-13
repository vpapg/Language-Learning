#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:07:48 2019

@author: vpapg
"""

from random import choice

words = {}
# words dictionary
# words = {word_sing_1 : [article_1, [word_plur_1]],
#          word_sing_2 : [article_2, [word_plur_2]], ...}
#
# HOW TO CALL THEM:
#
# words[word_sing_1] = [article_1, [word_plur_1]]
#
# words[word_sing_1][0] = article_1
#
# words[word_sing_1][1] = [word_plur_1] which is a list
#
# words[word_sing_1][1][0] = word_plur_1[0] which is the first string in the list
#
#
#
# Examples for the last two:
#
# if word_plur_1 = 'Autos', then words['Auto'][1] = ['Autos'], words['Auto'][1][0] = 'Autos'
#
# if word_plur_1 = ['Couchs','Couches', 'Couchen], then words['Couch'][1] = ['Couchs','Couches', 'Couchen], and words['Couch'][1][0] = 'Couchs', and words['Couch'][1][1] = 'Couches', etc.


with open("sing-plural.tsv") as f:
    for line in f:
        
        # strip removes the \n character
        # split creates a list with items that in the initial line are separated with \t
        current = line.strip().split('\t')
        
        # current[0] is the article (der/die/das)
        # current[1] is the word(s) in singular
        # current[2] is the word(s) in plural
        # words -> there can be alternative words in some cases, separated with '/'
        
        # separating alternative words
        cur = current[1].split('/')
        
        # for each aternative word in current[1] OR for just current[1]
        for i in range(len(cur)):
            # populate the words dictionary
            if cur[i] not in words:
                # plural is a list of the plural forms of all the alternative words
                # it can also contain only one word if there are no alternatives
                plural = current[2].split('/')
                words[cur[i]] = [current[0], plural]


def give_article(word_dict):
    # it keeps asking until the dictionary is empty.
    # in every correct answer, the examined word is removed from the dictionary.
    
    # a copy of the dictionary
    wd = dict(word_dict)
    
    while len(wd)>0:
        
        # randomly choose a word from the dictionary
        word = choice(list(wd))
        
        # show this text and store the answer in i
        i = input('The article of ' + word + ' is: ')
        
        # if i == correct article
        if wd[word][0] == i:
            print('Correct!')
            del wd[word] # that's why we use a copy
        else:
            print('Wrong! The correct article is', wd[word][0])


def give_plural(word_dict):
    wd = dict(word_dict)
    
    while len(wd)>0:
        word = choice(list(wd))
        i = input('The plural of ' + wd[word][0] + ' ' + word + ' is: ')
        if i in wd[word][1]:
            print('Correct!')
            del wd[word]
        else:
            print('Wrong! The plural is die ' + wd[word][1][0], end="")
            if len(wd[word][1]) > 1:
                for i in range(1,len(wd[word][1])):
                    print(', ' + wd[word][1][i], end="")
            print()


inp = -1
while inp == -1:
    inp = input("Type '0' to play with articles, or '1' to play with plurals: ")
    if inp == '0':
        give_article(words)
    elif inp == '1':
        give_plural(words)
    else:
        print('Wrong input!')
        inp = -1