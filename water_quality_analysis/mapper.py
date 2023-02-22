import sys
import re
(id, station_name, parameter, value) = (None, None, None, 154656)
count = 0
for line in sys.stdin:
    words = line.strip().split(",")
    for word in words:
        count = count+1
        if count == 1:
            id = word
        elif count == 2:
            station_name = word
        elif count == 3:
            parameter = word
        elif count==4:
            if parameter=='pH':
             value = float(word)
             print(id+station_name+" "+value)
            else:
                break



