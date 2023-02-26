import sys

(name, water_quality) = (None, None)
(station_name, ph_value) = (None, 545)
count = 0
sum = 0.0
for line in sys.stdin:
    (key, val) = line.strip().split(",")
    #print(key, val, name==key)
    if name != key:
        if count > 0:
            average_pH_value = sum / count

            if average_pH_value > 8 or average_pH_value < 6:
                water_quality = "Bad"
                # print(key + " " + str(averag_pH_value))
            # elif average_pH_value < 6:
            #     water_quality = "Bad"
            #     # print(key + " " + str(averag_pH_value))
            else:
                water_quality = "Good"
            print(name + " Water quality is " + water_quality)
            count = 1
            if val=='':
                val="0"
            (name, ph_value) = (key, float(val))
            sum = ph_value
           # print(name+" Water quality is"+water_quality)
        elif count == 0:
            # print(count)
            count = 1
            (name, ph_value) = (key, float(val))
            sum += ph_value
    else:
        count += 1
        if val == '':
            val = "0"
        sum += float(val)
if name:
    average_pH_value = sum / count
    if average_pH_value > 8 or average_pH_value < 6:
        water_quality = "Bad"
    else:
        water_quality = "Good"
    print(name+ " Water quality is " + water_quality)
    # print(name, str(average_pH_value))
