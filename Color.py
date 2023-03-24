import json

class Color:
		def __init__(self, red=255, green=255, blue=255, alpha=255):
			self.red = red
			self.green = green
			self.blue = blue
			self.alpha = alpha
			self.colorDict = {
				"rgba": [self.red, self.green, self.blue, self.alpha]
			}
		def getColorDict(self):
			return self.colorDict
		def setColorDict(self, key, value):
			self.colorDict[key] = value
			return self.colorDict