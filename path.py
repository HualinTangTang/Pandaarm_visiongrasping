from argparse import ArgumentParser
import numpy as np
from frankx import Affine, PathMotion, Robot

def load_wp(path):
    data = np.genfromtxt(path, dtype=[float, float, float])
    car_pos = np.array(data)
    return car_pos

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', default='192.168.3.101', help='FCI IP of the robot')
    args = parser.parse_args()

    # Connect to the robot
    robot = Robot(args.host)
    robot.set_default_behavior()
    robot.recover_from_errors()

    # Reduce the acceleration and velocity dynamic
    robot.set_dynamic_rel(0.15)

    # Upload the txt trajectory
    smooth_car_all = load_wp("/home/mirmi/dmp_learndata/frankxrepro.txt")
    len_car = len(smooth_car_all)
    #for i in range(0,len_car):
        #car_now = np.array(smooth_car_all)[i]
        #motion = PathMotion([
            #Affine(car_now[0], car_now[1], car_now[2]),
        #], blend_max_distance=0.05)
    motion = PathMotion([
            Affine(0.308805, -0.025446, 0.499386),
            Affine(0.308784, -0.025163, 0.499251),
            Affine(0.308764, -0.024890, 0.499121),
            Affine(0.308745, -0.024625, 0.498994),
            Affine(0.308726, -0.024368, 0.498871),
            Affine(0.308708, -0.024117, 0.498751),
        ])
    robot.move(motion)

