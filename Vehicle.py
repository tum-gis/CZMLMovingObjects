import json
from .Color import Color

defaultColor = Color(255,255,255,255)
defaultOutlineColor = Color(255,0,0,128)

class Vehicle:
	def __init__(self,id, position={}, point={}):
		self.id = id
		self.position = position.getPositionDict()
		self.point = point.getPointDict()
		self.dict = {"id":self.id, "position":self.position, "point":self.point }
	def getVehicleDict(self):
		return self.dict
	def setVehicleDict(self, key, value):
		self.dict[key] = value
		return self.dict
	class Position:
		def __init__(self, cartesian, epoch, interpolationAlgorithm = 'LAGRANGE', interpolationDegree = 1):
			self.cartesian = cartesian
			self.epoch = epoch
			self.interpolationAlgorithm = interpolationAlgorithm
			self.interpolationDegree = interpolationDegree
			self.positionDict = {
				"interpolationAlgorithm":self.interpolationAlgorithm
				,"interpolationDegree":self.interpolationDegree
				,"epoch":self.epoch 
				,"cartesian":self.cartesian
				}
		def getPositionDict(self):
			return self.positionDict 
		def setPositionDict(self, key, value):
				self.positionDict[key] = value
				return self.positionDict
	class Point:
		def __init__(self, color = defaultColor, outlineColor = defaultOutlineColor, outlineWidth = 3, pixelSize = 15):
			self.color = color.getColorDict()
			self.outlineColor = outlineColor.getColorDict()
			self.outlineWidth = outlineWidth
			self.pixelSize = pixelSize
			self.pointDict = {
				"color": self.color
				,"outlineColor": self.outlineColor
				,"outlineWidth": self.outlineWidth
				,"pixelSize": self.pixelSize
			}
		def getPointDict(self):
			return self.pointDict
		def setPointDict(self, key, value):
			self.PointDict[key] = value
			return self.pointDict