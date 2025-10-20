import csv
import math
from treelib import Node, Tree

def count_items(lista,calc_probability=False):
    d = {}
    for elem in lista:
        key = elem[-1]
        if d.get(key) is None:
            d[key] = 0
        d[key]+=1
    if calc_probability:
        for key in d:
            d[key]=d[key]/len(lista)
    return d

def enthropy(prob_dikt):
    ent = 0
    for key in prob_dikt:
        ent += prob_dikt[key] * math.log(prob_dikt[key],2)
    return -ent

def split(table, idx):
    d = {}
    for passager in table:
        key = passager[idx]
        if d.get(key) is None:
            d[key] = []
        d[key].append(passager)
    return d

def conditional_enthropy(table, idx):
    splitted = split(table, idx)
    s = len(table)
    # print(s)
    cond_ent = 0
    for key in splitted:
        podzbior = splitted[key]
        sj = len(podzbior)
        # print(sj)
        ent = enthropy(count_items(podzbior,True))
        # print(ent)
        cond_ent += sj*ent/s
    return cond_ent

def gain(table, idx):
    cond_ent = conditional_enthropy(table,idx)
    ent = enthropy(count_items(table,True))
    return ent - cond_ent


def ID3():
    return

with open('titanic-homework.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    table = []
    for row in spamreader:
        if row[0]==('PassengerId'):
            continue
        table.append(row)
    pro = count_items(table, True)
    print(pro)
    ent = enthropy(pro)
    print(ent)
    cond_ent = conditional_enthropy(table,1)
    print(cond_ent)
    print(gain(table,1))

