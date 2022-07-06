from argparse import ArgumentParser
from time import sleep
import numpy as np

from frankx import Affine, Robot


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', default='192.168.3.101', help='FCI IP of the robot')
    args = parser.parse_args()

    robot = Robot(args.host)
    robot.set_default_behavior()
    pose_all = []
    OTEE_all = []
    joints_all = []
    Elbow_all = []


    while True:
        state = robot.read_once()
        pose_all.append(robot.current_pose())
        OTEE_all.append(state.O_T_EE)
        joints_all.append(state.q)
        Elbow_all.append(state.elbow)

        np.savetxt("/home/mirmi/teachingdata/newpose.txt", pose_all, fmt='%s')
        np.savetxt("/home/mirmi/teachingdata/OTEE.txt", OTEE_all, fmt='%s')
        np.savetxt("/home/mirmi/teachingdata/joints.txt", joints_all, fmt='%s')
        np.savetxt("/home/mirmi/teachingdata/elbow.txt", Elbow_all, fmt='%s')

        print('\nPose: ', robot.current_pose())
        print('O_TT_E: ', state.O_T_EE)
        print('Joints: ', state.q)
        print('Elbow: ', state.elbow)
        sleep(0.05)
