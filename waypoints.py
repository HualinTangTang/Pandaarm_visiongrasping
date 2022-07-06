from argparse import ArgumentParser
import numpy as np
from frankx import Affine, JointMotion, Robot, Waypoint, WaypointMotion

def load_wp(path):
    data = np.genfromtxt(path, dtype=[float, float, float])
    car_pos = np.array(data)
    return car_pos

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host', default='192.168.3.101', help='FCI IP of the robot')
    args = parser.parse_args()

    # Connect to the robot
    robot = Robot(args.host, repeat_on_error=False)
    robot.set_default_behavior()
    robot.recover_from_errors()

    # Reduce the acceleration and velocity dynamic
    robot.set_dynamic_rel(0.05)
    # Move to the initial place
    #motion_to_start = WaypointMotion([
        #Waypoint(Affine(0.308805, -0.025446, 0.499386))])
    #robot.move(motion_to_start)

    c1_diff = np.array(diff_car).tolist()
    for xyz in c1_diff:
        x1 = xyz[0]
        y1 = xyz[1]
        z1 = xyz[2]
        #print("reading data")
        # Define and move forwards
        motion_reach = WaypointMotion([Waypoint(Affine(x1, y1, z1))])
    # You can try to block the robot now.
        robot.move(motion_reach)




    #joint_motion = JointMotion([0.292562, -0.697312, -0.0370223, -2.32467, -0.0478819, 1.74481, 0.913898 ])
    #robot.move(joint_motion)

