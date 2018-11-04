#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import algo

def main() :
        if (len(sys.argv) > 2) :
                file = open(sys.argv[1], "r")
                lines = file.read().rstrip()
                tab = lines.split("\n")
        if (len(sys.argv) < 3 or len(sys.argv) > 4):
                print("Usage: ./302separation.py <file> <node1> <node2>")
                print("./302separation.py <file> <distance>")
                return(84)
        peoples = []
        for i in range(0, len(tab), 1) :
                duo = tab[i].split(" is ")
                data = {
                        'name' : duo[0],
                        'friends' : [tab[i].split(" with ")[1]]
                }
                peoples.append(data)
        tmp = peoples[:]
        for i in range(0, len(tmp)) :
                for j in range(i + 1, len(tmp)) :
                        if (tmp[i]["name"] == tmp[j]["name"]) :
                                peoples[i]["friends"] = tmp[i]["friends"] + tmp[j]["friends"]
                                peoples[i]["name"] = tmp[i]["name"]
        result = []
        i = 0
        same = False
        for item in peoples:
                for truc in result :
                        if item["name"] == truc["name"] :
                                same = True
                if (same == False) :
                        result.append(item)
                same = False             
        names = getNames(tab)
        if (len(sys.argv) == 4) :
                printSeparation(sys.argv, names, result)
        else :
                for item in names :
                        print(item)
                print('')
                matrix = algo.createMatrix(names, result)
                for item in matrix :
                        print(*item, sep=' ')
                print('')
                network = algo.createNetwork(names, matrix, int(sys.argv[2]))
                for item in network :
                        print(*item, sep=' ')
        return (0)

def checkName(name, tab) :
        if name in tab :
                return True
        return False

def printSeparation(argv, names, result) :
        first = argv[2]
        second = argv[3]
        if (checkName(first, names) is True and checkName(second, names) is True) :
                if (first == second) :
                        print("degree of separation between ", sys.argv[2], " and ", sys.argv[3], ": 0", sep="")
                else :
                        matrix = algo.createMatrix(names, result)
                        network = algo.connectOne(names, matrix, first, second)
                        sepa = network[names.index(first)][names.index(second)]
                        print("degree of separation between ", sys.argv[2], " and ", sys.argv[3], ": ", sepa, sep="")
                return
        else :
                print("degree of separation between ", sys.argv[2], " and ", sys.argv[3], ": -1", sep="")

def getNames(tab) :
        names = []
        for i in range(0, len(tab), 1) :
                duo = tab[i].split(" is ")
                names.append(duo[0])
                names.append(tab[i].split(" with ")[1])
        names = list(set(names))
        names.sort()
        return names

try :
        if (main() == 84) :
                exit(84)
except :
        exit(84)
