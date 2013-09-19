#-------------------------------------------------------------------------------
# Name:        /units/base.py
# Purpose:
#
# Author:      viren
#
# Created:     19/09/2013
# Copyright:   (c) viren 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Base:
	health = Int()
	position = []

	attack_power = Int()
	max_health = Int()

	def take_damage(self, points):
		self.health -= points

	def attack():
		return attack_power

	def rest():
		health += max_health

	def move(direction):
		pass

	def feel():
		pass
