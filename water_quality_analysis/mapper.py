import sys
(id, station_name, parameter, value) = (None, None, None, 454)
count = 0
for line in sys.stdin:
   # print(line)
    words = line.strip().split(",")
    count = 0
    for word in words:
        count = count+1
        if count == 1:
            id = word
        elif count == 4:
            station_name = word
        elif count == 15:
            parameter = word
        elif count==16:
            if parameter=='pH':
             #value = float(word)
             print(id+" "+station_name+","+word)
            else:
                break
    #print(id + station_name)


