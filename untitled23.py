# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nak8eo96HLaaRCuVnIVMFDKa2yAO4WHV
"""

def buy(shopping_bag):
    item = input('상품명: ')
    if item =="":
        return False
    else:
      a = input('수량은? ')
      print(f'장바구니에 {item} {a}개(가) 담겼습니다.')
      shopping_bag[item] = a
      return True

def show(shopping_bag):
    print(f'장바구니 보기: {shopping_bag}')

def find(shopping_bag):
    r = input('검색하고자 하는 상품은? ')
    if r in shopping_bag:
        print(f'{r}은(는) {shopping_bag[r]}개 담겨 있습니다.')
    else:
        print(f'{r}은(는) 장바구니에 없습니다.')

shopping_bag = {}
while True:
  if buy(shopping_bag) == False:
      break
show(shopping_bag)
find(shopping_bag)