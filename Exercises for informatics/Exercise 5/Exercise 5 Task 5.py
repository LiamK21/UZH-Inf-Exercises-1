def hamming(a, b):
    d = 0
    if a == b:
        return "a"
    else:
        for index, char in enumerate(a):
            if char == b[index]:
                pass
            else:
                d += 1
        return (a, b, d)


def hamming_dist(signal_1, signal_2):
    sensor_1_data = []
    hamming_amount = []
    for i in signal_1["data"]:
        sensor_1_data.append(i)
    if len(sensor_1_data) == len(signal_2):
        if len(sensor_1_data) > 0 and len(signal_2) > 0:
            pass
        else:
            return "Empty signal on at least one of the sensors"
    else:
        return "Empty signal on at least one of the sensors"
    for index, value in enumerate(sensor_1_data):
        if len(sensor_1_data[index]) > len(signal_2[index]) or len(sensor_1_data[index]) < len(signal_2[index]):
            return "Sensor defect detected"
        else:
            hamming_amount.append(hamming(sensor_1_data[index], signal_2[index]))
    while hamming_amount.__contains__("a"):
        hamming_amount.remove("a")
    return hamming_amount


signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001011", "11110000", "01000011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
