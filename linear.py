from argparse import ArgumentParser
import numpy as np
from frankx import Affine, LinearMotion, Robot

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

    # Define and move forwards
    smooth_car_all = load_wp("/home/mirmi/dmp_learndata/frankxrepro.txt")
    print(smooth_car_all)
    c1_smooth = np.array(smooth_car_all).tolist()
    for xyz in c1_smooth:
        motion_forward = LinearMotion(Affine(xyz[0], xyz[1], xyz[2]))
        robot.move(motion_forward)

