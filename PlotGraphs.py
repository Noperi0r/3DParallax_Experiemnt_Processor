import numpy as np 
from matplotlib import pyplot as plt

def NormalDistribution(mu3D, std3D, mu2D, std2D):
    #plt.hist(data, bins=30, density=True, alpha=0.6, color='b')
    x = np.linspace(-100, 100, 1000) # Uniform num arrays from -5 to 5 
    
    pdf3D = (1/(std3D * np.sqrt(2*np.pi))) * np.exp(-(x-mu3D)**2 / (2 * std3D**2))
    pdf2D = (1/(std2D * np.sqrt(2*np.pi))) * np.exp(-(x-mu2D)**2 / (2 * std2D**2))
    
    plt.plot(x, pdf3D, 'b-', lw=2, label="3D Test Normal Distribution")
    plt.plot(x, pdf2D, 'r-', lw=2, label="2D Test Normal Distribution")
    
    plt.title("Angle Difference Normal Distribution")
    plt.xlabel("Angle difference")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.show() 
    
def PointPlot(coordinates3D, coordinates2D):
    """Plot tuple (x,y) grid point onto x-y plane 
    
    Args:
        coordinates (list): list containing tuple (longitude, latitude) as elements.
    """
    # coordinates는 (longitude, latitude) 형태의 튜플을 요소로 갖는 리스트
    lons3D, lats3D = zip(*coordinates3D)  # 각각의 좌표를 분리하여 리스트로 반환
    lons2D, lats2D = zip(*coordinates2D)

    plt.figure(figsize=(8, 6))
    
    plt.scatter(lons3D, lats3D, color='blue', marker='o', s=30, label='3D Experiment')  # 점으로 좌표를 표시
    plt.scatter(lons2D, lats2D, color='red', marker='o', s=30, label='2D Experiment')  # 점으로 좌표를 표시

    plt.xlabel('Longitude')  # x축 레이블
    plt.ylabel('Latitude')   # y축 레이블
    plt.title('Coordinates Plot')  # 그래프 제목
    plt.grid(True)  # 격자 표시

    plt.axhline(0, color='black', linewidth=0.5)  # x축
    plt.axvline(0, color='black', linewidth=0.5)  # y축

    plt.xlim(-50, 50)  # x축 범위 설정
    plt.ylim(-30, 30)    # y축 범위 설정

    plt.legend()    

    plt.show()