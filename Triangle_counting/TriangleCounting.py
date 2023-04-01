#!/usr/bin/env python
import sys

#Hashing for 1-partition
def modularHash(node, tableSize):
    return node % tableSize
nodes = []
for i in range(4039):
    nodes.append(i)

list1 = []
list = []
for i in range(9):
    list.append([])
list.append(list1)
for i in range(len(nodes)):
    index = modularHash(nodes[i], 10)
    list[index].append(nodes[i])



def hashValue(vertex_list, vertex):
    for i in range(len(vertex_list)):
        if vertex_list[i].count(vertex) >= 1:
            return i
    return -1

for line in sys.stdin:
        (u, v) = line.strip().split(" ")
        # print(u+" "+v)
        u = int(u)
        v = int(v)
        # print(u, v)
        indexU = hashValue(list, u)
        indexV = hashValue(list, v)
        # print(str(indexU)+" "+str(indexV))
        partition = 10
        for i in range(partition-1):
            j = i+1
            while j <= partition-1:
                setOne = {i, j}
                setTwo = {indexU, indexV}
                if setTwo.issubset(setOne):
                    print(str(i)+str(j)+", "+str(u)+" "+str(v))
                    # fileOne.write(str(i)+" "+str(j)+". "+str(u)+" "+str(v)+"\n")
                    # print(str(setTwo)+" "+str(setOne))
                j+=1

        if indexU!=indexV :
            # print(str(indexU) + " " + str(indexV))
            for i in range(partition-2):
                j = i+1
                while j <= partition - 2:
                    k = j+1
                    while k <= partition - 1:
                        setOne = {i, j, k}
                        setTwo = {indexU, indexV}
                        if setTwo.issubset(setOne):
                            print(str(i) + str(j) + str(k) + ", " + str(u) + " " + str(v))
                            # fileOne.write(str(i) + " " + str(j) + " " + str(k) + ". " + str(u) + " " + str(v)+"\n")
                            # print(str(setTwo) + " " + str(setOne))
                        k += 1

                    j += 1


