import sys

(name, water_quality) = (None, None)
(station_name, ph_value) = (None, 545)
count = 0
sum = 0
for line in sys.stdin:
    (key, val) = line.split(", ")
    if name!=key:
        if(count>0):
            averag_pH_value = sum/count
            if(averag_pH_value>8):
                print(key+" Base water")
            elif averag_pH_value<6:
                print(key+" Acidic water")
        count = 0
        (name, ph_value) = (key, float(val))
        count = count+1
        sum+=ph_value
    else:
        count+=1
        sum+=float(val)

