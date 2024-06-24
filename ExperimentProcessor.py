import numpy as np 
from matplotlib import pyplot as plt
import os, os.path
from PlotGraphs import *

# TestData_n.txt
# Find if it's test for 2d or 3d searching for the first line of txt file 

datum = [] # n files 

DIR = './Data'
files = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]
print(files)

for i in range(len(files)):
    data = {"dim": "", "trueVector": [], "inputVector": [], "time": [], "longitude": [], "latitude": [], "angle": []} # per file 
    with open("Data/" + files[i], 'r') as f:
        for line in f:
            lineStripped = line.strip()
            if lineStripped == "3D" or lineStripped == "2D":
                data["dim"] = lineStripped
                continue
            elems = lineStripped.split('/')
            
            valueList = elems[0].strip("()").split(",")
            value = tuple(map(float, valueList))
            data["trueVector"].append(value) 
            
            valueList = elems[1].strip("()").split(",")
            value = tuple(map(float, valueList))
            data["inputVector"].append(value)
            
            value = float(elems[2])
            data["time"].append(value) 
            
            value = float(elems[3])
            data["longitude"].append(value)
            
            value = float(elems[4])
            data["latitude"].append(value)
            
            value = float(elems[5])
            data["angle"].append(value) 
            
        datum.append(data)

print(datum)

# ANGLE NORMAL DISTRIBUTION 
angles_3D, angles_2D = [], []
for i in range(len(datum)):
    if datum[i]['dim'] == '3D':
        for j in range(len(datum[i]['angle'])):
            angles_3D.append(datum[i]['angle'][j])
    elif datum[i]['dim'] == '2D':
        for j in range(len(datum[i]['angle'])):
            angles_2D.append(datum[i]['angle'][j])
        
angleMu_3D = np.sum(angles_3D) / len(angles_3D)
angleStd_3D = np.std(angles_3D)

angleMu_2D = np.sum(angles_2D) / len(angles_2D)
angleStd_2D = np.std(angles_2D)

# LONGITUDE - LATITTUDE 
rotation_3D, rotation_2D = [], [] # (경도 가로, 위도 세로) tuple as element

for i in range(len(datum)):
    if datum[i]['dim'] == '3D':
        for j in range(len(datum[i]['longitude'])):
            rotation_3D.append((datum[i]['longitude'][j], datum[i]['latitude'][j]))

    elif datum[i]['dim'] == '2D':
        for j in range(len(datum[i]['longitude'])):
            rotation_2D.append((datum[i]['longitude'][j], datum[i]['latitude'][j]))
            
# TIME NORMAL DISTRIBUTION
timeDiff_3D, timeDiff_2D = [], [] 

for i in range(len(datum)):
    if datum[i]['dim'] == '3D':
        for j in range(len(datum[i]['time'])):
            if j == 0:
                timeDiff_3D.append(datum[i]['time'][j])
                continue
            timeDiff_3D.append(datum[i]['time'][j] - datum[i]['time'][j-1])
            
    if datum[i]['dim'] == '2D':
        for j in range(len(datum[i]['time'])):
            if j == 0:
                timeDiff_2D.append(datum[i]['time'][j])
                continue
            timeDiff_2D.append(datum[i]['time'][j] - datum[i]['time'][j-1])
            
timeMu_3D = np.sum(timeDiff_3D) / len(timeDiff_3D)
timeStd_3D = np.std(timeDiff_3D)

timeMu_2D = np.sum(timeDiff_2D) / len(timeDiff_2D)
timeStd_2D = np.std(timeDiff_2D)
    
#NormalDistribution()

coordinates = [ # Test coordinates
    (126.978, 37.566),  # 서울의 위도, 경도
    (139.6917, 35.6895),  # 도쿄의 위도, 경도
    (2.3522, 48.8566)  # 파리의 위도, 경도
]
PointPlot(coordinates)