import numpy as np
import time
from tqdm import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get smooth trajectory from DMP learning
    data_new = np.genfromtxt("/home/mirmi/dmp_learndata/2repro_total.txt", dtype=[float, float, float])
    data_new_list = list(data_new)

    x_position1 = []
    y_position1 = []
    z_position1 = []

    for i in data_new_list:
        x_position1.append(i[0])
    print(x_position1)

    for j in data_new_list:
        y_position1.append(j[1])

    for k in data_new_list:
        z_position1.append(k[2])

    data_len1 = len(x_position1)
    interval = 100

    x_position_inter = x_position1[0:data_len1:interval]
    y_position_inter = y_position1[0:data_len1:interval]
    z_position_inter = z_position1[0:data_len1:interval]
    data_len2 = len(x_position_inter)
    t = np.linspace(0, 1.5 * np.pi, data_len2)
    y_demo_new = np.zeros((3, data_len2))
    # y_demo = np.zeros((2, data_len))
    y_demo_new[0,:] = x_position_inter[:]
    y_demo_new[1,:] = y_position_inter[:]
    y_demo_new[2,:] = z_position_inter[:]


    for i in tqdm(y_demo_new[0,:]):
        f = open('/home/mirmi/dmp_learndata/2smooth_reprox.txt', 'a')
        f.write(str(i) + '\n')
        f.close()

    for i in tqdm(y_demo_new[1,:]):
        f = open('/home/mirmi/dmp_learndata/2smooth_reproy.txt', 'a')
        f.write(str(i) + '\n')
        f.close()

    for i in tqdm(y_demo_new[2,:]):
        f = open('/home/mirmi/dmp_learndata/2smooth_reproz.txt', 'a')
        f.write(str(i) + '\n')
        f.close()

