#!/usr/bin/env python
import sys


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

triangle = 0.0
hashing = list


sameHashValue = 0

edge_list = []
(key, values) = (None, None)
count = 0
adj_list = []
total_triangle = 0
for i in range(4039):
    adj_list.append([])

partition = 10

for line in sys.stdin:
    # fileOne.write(line)
    values = line.strip().split(", ")
    v1 = values[0]
    v2 = values[1]
    if key != v1:
        if count == 0:
            key = v1
            edge_list.append(v2)
            (u, v) = v2.split(" ")
            u = int(u)
            v = int(v)
            adj_list[u].append(v)
            adj_list[v].append(u)
            count += 1
        else:

            #print("Edge: "+str(edge_list))

            for i in range(len(edge_list)):
                (u, v) = edge_list[i].split(" ")
                u = int(u)
                v = int(v)
                setOne = {v}
                setTwo = {u}

                # Edge iterator algorithm for counting triangle
                for x in adj_list[u]:
                    setOne.add(x)
                for x in adj_list[v]:
                    setTwo.add(x)
                
                for x in setOne.intersection(setTwo):
                    if u < v < x:
                        if hashValue(hashing, x) == hashValue(hashing, u) == hashValue(hashing, v):
                            total_triangle += float(1)/(partition-1)
                        else:
                            total_triangle += 1
                        # print("Triangle: "+str(u)+str(v)+str(x)+" Total: "+str(total_triangle))
                        # fileOne.write("Triangle: "+str(u)+str(v)+str(x)+" Total: "+str(total_triangle)+"\n")


           
            del edge_list[:]
            del adj_list[:]

           
            for i in range(4039):
                adj_list.append([])
            count = 1
            edge_list.append(v2)
            (u, v) = v2.split(" ")
            u = int(u)
            v = int(v)
            adj_list[u].append(v)
            adj_list[v].append(u)
            key = v1
            # print(total_triangle)

    else:
        edge_list.append(v2)
        (u, v) = v2.split(" ")
        u = int(u)
        v = int(v)
        adj_list[u].append(v)
        adj_list[v].append(u)
        count += 1

if key:
    # edge_list.append(v2)
    # (u, v) = v2.split(" ")
    # u = int(u)
    # v = int(v)
    # adj_list[u].append(v)
    # adj_list[v].append(u)
    #print("Edge: " + str(edge_list))

    for i in range(len(edge_list)):
        (u, v) = edge_list[i].split(" ")
        u = int(u)
        v = int(v)
        setOne = {v}
        setTwo = {u}

        # Edge iterator algorithm for counting triangle
        for x in adj_list[u]:
            setOne.add(x)
        for x in adj_list[v]:
            setTwo.add(x)


        for x in setOne.intersection(setTwo):
            if u < v < x:
                if hashValue(hashing, x) == hashValue(hashing, u) == hashValue(hashing, v):
                    total_triangle += float(1) / (partition-1)
                else:
                    total_triangle += 1
                # print("Triangle: " + str(u) + str(v) + str(x)+" Total: "+str(total_triangle))
                # fileOne.write("Triangle: " + str(u) + str(v) + str(x) + " Total: " + str(total_triangle)+"\n")

print(total_triangle)

