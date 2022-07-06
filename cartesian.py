from argparse import ArgumentParser
import numpy as np
from frankx import Affine, JointMotion, Robot, Waypoint, WaypointMotion

def load_wp(path):
    data = np.genfromtxt(path, dtype=[float,float,float,float,float,float,float])  # load joint values from .txt file into data
    q_pos = np.array(data)
    return q_pos


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', default='192.168.3.101', help='FCI IP of the robot')
    args = parser.parse_args()

    # Connect to the robot
    robot = Robot(args.host, repeat_on_error=False)
    robot.set_default_behavior()
    robot.recover_from_errors()

    # Reduce the acceleration and velocity dynamic
    robot.set_dynamic_rel(0.2)
    ## move to the initial point
    robot.move(JointMotion([0, -np.pi/4, 0, -3 * np.pi/4, 0, np.pi/2, np.pi/4]))

    q_pos_all = load_wp("/home/mirmi/dmp_learndata/newq_frankxrepro.txt")
    num_q = len(q_pos_all)
    # print('num_q is:',num_q)
    print('q_pos_all is:', q_pos_all[1])

    # follow the given trajectory
    for i in range(0,num_q,20):
        q_pos_now = np.array(q_pos_all)[i]
        joint_motion_now = JointMotion(q_pos_now)
        if i % 500 == 0:
            print('Now moving to the joint postion:', q_pos_now)
        robot.set_dynamic_rel(0.6)
        robot.move(joint_motion_now)

    # follow a sinusoidal/cosinoidal path​

    ## Define and move forwards
    # motion_down = WaypointMotion([
        # Waypoint(Affine(0.0, 0.0, -0.12), -0.2, Waypoint.Relative),
        # Waypoint(Affine(0.08, 0.0, 0.0), 0.0, Waypoint.Relative),
        # Waypoint(Affine(0.0, 0.1, 0.0, 0.0), 0.0, Waypoint.Relative),
    # ])

    # You can try to block the robot now.
    # robot.move(motion_down)

    # return back to the initial pos
    robot.move(JointMotion([0, -np.pi/4, 0, -3 * np.pi/4, 0, np.pi/2, np.pi/4]))













