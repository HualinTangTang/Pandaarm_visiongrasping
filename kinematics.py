from argparse import ArgumentParser
import numpy as np
from frankx import Affine, Kinematics, NullSpaceHandling

def load_wp(path):
    data = np.genfromtxt(path, dtype=[float,float,float])
    car_pos = np.array(data)
    return car_pos

if __name__ == '__main__':
    # Joint configuration
    q = [0.292562, -0.697312, -0.0370223, -2.32467, -0.0478819, 1.74481, 0.913898 ]
    # Forward kinematic
    x = Affine(Kinematics.forward(q))
    print('Current end effector position: ', x)

    car_pos_smooth = load_wp("/home/mirmi/dmp_learndata/frankxrepro.txt")
    c_smooth = np.array(car_pos_smooth).tolist()
    num_car = len(np.array(car_pos_smooth))
    new_qm = []
    for xyz in c_smooth:
        x1 = xyz[0]
        y1 = xyz[1]
        z1 = xyz[2]

    # Define new target position
        x_new = Affine(x1, y1, z1) * x

    # Franka has 7 DoFs, so what to do with the remaining Null space?
        null_space = NullSpaceHandling(2, 1.4) # Set elbow joint to 1.4

    # Inverse kinematic with target, initial joint angles, and Null space configuration
    # python .vector是pose，包含三位欧拉角
        q_new = Kinematics.inverse(x_new.vector(), q, null_space)
        new_qm.append(q_new)

        print('New position: ', x_new)
        print('New joints: ', q_new)
    np.savetxt("/home/mirmi/dmp_learndata/newq_frankxrepro.txt", new_qm, fmt='%f')
