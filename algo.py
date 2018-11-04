#!/usr/bin/env python3                                                                              
# -*- coding: utf-8 -*-                                                                             

import sys

def createMatrix(names, friend) :
    friends = []
    for item in friend :
        network = []
        for f in item['friends'] :
            network.append(f)
        friends.append(network)
    matrix = []
    i = 0
    while i < len(names) :
        memset = []
        y = 0
        while y < len(names) :
            memset.append(0)
            y+=1;
        matrix.append(memset)
        i+=1;
    i = 0
    for item in friends :
        for f in item :
            matrix[names.index(f)][names.index(friend[i]["name"])] = 1
            matrix[names.index(friend[i]["name"])][names.index(f)] = 1
        i+=1
    return(matrix)


def countWeight(matrix, w, y, x) :
    i = 0
    for item in matrix :
        if (matrix[y][i] != w) :
            i+=1
            continue
        i+=1
        if (item[x] == 1) :
            return (w + 1)
    return (0)

def createNetwork(names, matrix, limit) :
    w = 1
    while (w < limit) :
        for item in matrix :
            i = 0
            for f in item :
                if (matrix.index(item) == i or (f <= w and f != 0)) :
                    i+=1
                    continue
                item[i] = countWeight(matrix, w, matrix.index(item), i)
                i+=1
        w+=1
    return(matrix)

def connectOne(names, matrix, first, second) :
    w = 1
    while (matrix[names.index(first)][names.index(second)] == 0) :
        for item in matrix :
            i = 0
            for f in item :
                if (matrix.index(item) == i or (f <= w and f != 0)) :
                    i+=1
                    continue
                item[i] = countWeight(matrix, w, matrix.index(item), i)
                i+=1
        w+=1
    return(matrix)
