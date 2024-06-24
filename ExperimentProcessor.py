import numpy as np 
from matplotlib import pyplot as plt
import os, os.path

# TestData_n.txt
# Find if it's test for 2d or 3d searching for the first line of txt file 

datas = [] # n files 

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
            
        datas.append(data)

print(datas)

angleLen = 0
angleSum = 0
for i in range(datas):
    angleLen += len(datas['angle'])
    for j in range(len(datas['angle'])):
        angleSum += datas["angle"][j]

mu = angleSum / angleLen # Average value 
sigma = 1 # Standard Deviation TODO 

data = np.random.normal(mu, sigma, 10)

#plt.hist(data, bins=30, density=True, alpha=0.6, color='b')

x = np.linspace(-5, 5, 100)
pdf = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-(x-mu)**2 / (2 * sigma**2))
plt.plot(x, pdf, 'r-', lw=2)

plt.title("Normal Distribution")
plt.xlabel("value")
plt.ylabel("Density")
plt.show() 
