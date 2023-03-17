import json

class Vehicle:
	def __init__(self,id, position={}):
		self.id = id
		self.position = position.getPositionDict()
		self.dict = {"id":self.id, "position":self.position }
	def getVehicleDict(self):
		return self.dict
	def setVehicleDict(self, key, value):
		self.dict[key] = value
		return self.dict
	class Position:
		def __init__(self, cartesian, interpolationAlgorithm = 'LAGRANGE', interpolationDegree = 1, epoch = '2012-08-04T16:00:00Z'):
			self.cartesian = cartesian
			self.interpolationAlgorithm = interpolationAlgorithm
			self.interpolationDegree = interpolationDegree
			self.epoch = epoch
			self.PositionDict = {
				"interpolationAlgorithm":self.interpolationAlgorithm
				, "interpolationDegree":self.interpolationDegree
				, "epoch":self.epoch 
				, "cartesian":self.cartesian
				}
		def getPositionDict(self):
			return self.PositionDict 
		def setPositionDict(self, key, value):
				self.PositionDict[key] = value
				return self.PositionDict
