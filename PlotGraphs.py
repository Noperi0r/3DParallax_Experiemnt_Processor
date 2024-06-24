import numpy as np 
from matplotlib import pyplot as plt

def NormalDistribution():
    # NORMAL DISTRIBUTION 
    mu = 0 
    sigma = 1 # Standard Deviation TODO 

    data = np.random.normal(mu, sigma, 10) # 10 random samples

    #plt.hist(data, bins=30, density=True, alpha=0.6, color='b')
    x = np.linspace(-5, 5, 100) # Uniform num arrays from -5 to 5 
    pdf = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-(x-mu)**2 / (2 * sigma**2))
    plt.plot(x, pdf, 'r-', lw=2)
    plt.title("Normal Distribution")
    plt.xlabel("value")
    plt.ylabel("Density")
    plt.show() 
    
def PointPlot(coordinates: list):
     # coordinates는 (longitude, latitude) 형태의 튜플을 요소로 갖는 리스트
    lons, lats = zip(*coordinates)  # 각각의 좌표를 분리하여 리스트로 반환

    plt.figure(figsize=(8, 6))
    plt.scatter(lons, lats, color='blue', marker='o', s=30)  # 점으로 좌표를 표시
    plt.xlabel('Longitude')  # x축 레이블
    plt.ylabel('Latitude')   # y축 레이블
    plt.title('Coordinates Plot')  # 그래프 제목
    plt.grid(True)  # 격자 표시

    plt.axhline(0, color='black', linewidth=0.5)  # x축
    plt.axvline(0, color='black', linewidth=0.5)  # y축

    plt.xlim(-180, 180)  # x축 범위 설정
    plt.ylim(-90, 90)    # y축 범위 설정

    plt.show()