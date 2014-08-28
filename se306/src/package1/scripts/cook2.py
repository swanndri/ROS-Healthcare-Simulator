#!/usr/bin/python

import rospy
import node

class Cook(node.Robot):
	
	def __init__(self, name):
		super(Cook, self).__init__(name)

	def _scheduler_event_callback(self, msg):
		if msg.data.split()[1].startswith(self.__class__.__name__):
			self.jobs.put(tuple(msg.data.split()))

if __name__ == '__main__':
	rospy.init_node('robot_2')
	cook = Cook('robot_2')