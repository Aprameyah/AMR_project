#!/usr/bin/python2.7

import rospy
from tf.transformations import quaternion_from_euler
import actionlib
from move_base_msgs.msg import MoveBaseGoal, MoveBaseAction


def movebase_client():
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 15.0
    goal.target_pose.pose.position.y = -8
    goal.target_pose.pose.orientation.w = 1.0
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()


if __name__ == '__main__':
    try:
        rospy.init_node('custom_bot_goal_action_client')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
