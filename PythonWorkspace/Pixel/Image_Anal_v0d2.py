# https://www.tutorialspoint.com/matplotlib/matplotlib_3d_surface_plot.htm
# https://stackoverflow.com/questions/9170838/surface-plots-in-matplotlib


import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


import cv2
# from PIL import Image


def main():
    img_file = 'F:\MiguelGIT\PythonWorkspace\sem_30x30.png' # 2D grayscale image file
    thres = 1 # threshold value for z value scale-down

    # Load image file 
    img2 = cv2.imread(img_file, cv2.IMREAD_COLOR)
    wx, hy, rgb = img2.shape
    # print('wx:', wx, 'hy:', hy, 'rgb:', rgb)

    xx = np.arange(wx)
    yy = np.arange(hy)
    zz = []
    for x in range(wx):
        for y in range(hy):
            zz.append(img2[x, y][0]/thres)
    # print(xx, yy, zz)

    X, Y = np.meshgrid(xx, yy)
    Z = np.asarray(zz, dtype=np.uint8).reshape((hy, wx))
    # Z = f(X, Y)

    # Plotting 3D graph
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', \
                           edgecolor='none', antialiased=True, \
                           linewidth=0)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_zlim(0, 200)
    ax.set_title('3D surface plot for '+img_file, fontsize=20)

    # set view angles to get better plot
    ax.azim = 70   # z rotation (default=270)
    ax.elev = 50     # x rotation (default=0)
    ax.dist = 10    # zoom (define perspective)

    fig.colorbar(surf, shrink=0.5, aspect=15, pad = -0.05)
    plt.tight_layout()
    plt.savefig('3D_'+img_file)
    plt.show()


# main 함수 로딩부
if __name__ == '__main__':
    main()
