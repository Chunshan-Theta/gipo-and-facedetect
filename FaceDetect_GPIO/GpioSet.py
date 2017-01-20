# -*- coding: utf-8 -*-
# GpioSet.py	
# - control a set of GPIO.
# - using Json config to create that.
import GPIO24 as gpio
import json

class GpioSet:
	def __init__(self,JsonData,Alert=0):
		self.Set,self.Devices,self.Costs,self.Pins = self.SetCreat(JsonData,Alert)
		
		
	def SetCreat(self,JsonData,Alert):
		PinSet = []
		PinSetPin = []
		PinSetDevice = []
		PinSetCost = []
		for d in JsonData:
			#pin = GpioForLights("PinNum",1)
			#PinSet.append(d['pin'])
			if d['Device'] != "null":
				PinSet.append(gpio.GpioForLights(d['pin'],Alert))
				PinSetPin.append(d['pin'])
				PinSetDevice.append(d['Device'])
				PinSetCost.append(d['Cost'])
		#for i in PinSet:
		#	print "PinSet"+i
	
		return PinSet,PinSetDevice,PinSetCost,PinSetPin



#JsonData = json.loads('[{"id":"0","pin":"7","GPIO":"4","Cost":"20","Device":"風扇"},{"id":"1","pin":"11","GPIO":"17","Cost":"20","Device":"監視器"},{"id":"2","pin":"12","GPIO":"18","Cost":"20","Device":"電燈"}]')
#mainarray = GpioSet(JsonData).Set
#for i in mainarray:
#	i.on()
#for i in mainarray:
#	i.clean()


#for d in JsonData:
#	print d['pin']
#	print d['Device']
