#!/usr/bin/env python3
import rospy
from bruce_slam.utils.io import *
from bruce_slam.feature_extraction_vertical import FeatureExtractionVertical

if __name__ == "__main__":

    #init the ros node
    rospy.init_node("feature_extraction_vertical_node", log_level=rospy.INFO)

    #call class constructor
    node = FeatureExtractionVertical()
    node.init_node()

    #get args
    parser = common_parser()
    args, _ = parser.parse_known_args()

    #log and spin
    if not args.file:
        loginfo("Start online sonar feature extraction...")
        while not rospy.is_shutdown():
            node.extract_features()
        rospy.spin()
    else:
        loginfo("Start offline sonar feature extraction...")
        offline(args)