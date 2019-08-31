# -*- coding:utf-8 -*-
'''
    Created on: 2019-07-29
    description: 
    @auther: weew12
'''
import collections


'''
   命名元组 
   classname : Card
   keyWords: rank、 suit
   相当于定义了一个含有关键字的类 
'''
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        '''初始化一副撲克 四种花色 每种13张'''
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]
    def __len__(self):
        '''此方法提供获取长度'''
        return len(self._cards)
    
    def __getitem__(self, position):
        '''此方法提供了使用位置参数索引'''
        return self._cards[position]

deck = FrenchDeck()    
# # __getitem__()

# print(deck[0])
# print(deck[-1])

# 随机抽取
# from random import choice
# getCard = choice(deck)
# print(getCard)

# 分片
# print(deck[:3])
# print(deck[12::13])

# # __len__()
# print(len(deck))



