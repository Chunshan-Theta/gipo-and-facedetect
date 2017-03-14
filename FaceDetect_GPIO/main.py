#!/usr/bin/env python 2.7
# -*- coding: utf-8 -*-
import time
import numpy as np
import cv2 #2.4.10
import cv2.cv as cv
from video import create_capture
from common import clock, draw_str
import datetime as dt
import GpioSet as g
import json



class PicData:
	def __init__(self,pic,cascade,PostOn=0):		
		gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
		gray = cv2.equalizeHist(gray)
		self.SourcePic = pic
		self.GrayPic = gray
		self.Cascade = cascade		
		self.rects = self.detect(self.GrayPic, self.Cascade)
		self.DrawPic=self.draw_rects(self.SourcePic,self.rects, (0, 255, 0))
		self.PeopleNum = len(self.rects)
		self.RightNow = str(dt.datetime.now())
		self.RightNowShame = str(self.RightNow[:4]+self.RightNow[5:7]+self.RightNow[8:10]+self.RightNow[11:13]+self.RightNow[14:16]+self.RightNow[17:19])		
		if PostOn:
			self.PostData()


	def detect(self,img, cascade):
		rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
		if len(rects) == 0:
		    return []
		rects[:,2:] += rects[:,:2]
		return rects

	def draw_rects(self,img, rects, color):
		for x1, y1, x2, y2 in rects:
		    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
		return img

	def PostData(self):
		#import requests as rq
		#r = rq.post("http://"+HostIP+"/pi/SQLAPI.php",data={"action":"InsertSql","PeopleNum":self.PeopleNum,"Time":self.RightNowShame})
		print "you should't run this"
if __name__ == '__main__':

	import sys, getopt
	
	args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
	try: video_src = video_src[0]
	except: video_src = 0
	args = dict(args)
	cascade_fn = args.get('--cascade', "./haarcascade_frontalface_alt.xml")

	cascade = cv2.CascadeClassifier(cascade_fn)
	
	import requests as rq
	#Note-(WebServer address) :edit web-server IP address
	WebServerAddress="http://192.168.1.189/web_GPIO/"
	r = str(rq.get(WebServerAddress+"RJ.php").content)
	#print r
	
	cam = create_capture(video_src, fallback='synth:bg=../cpp/lena.jpg:noise=0.05')

	GpioConfig = json.loads(r)
	GPIOPIN = g.GpioSet(GpioConfig,1)
	G_Set = GPIOPIN.Set
	G_Devices = GPIOPIN.Devices
	G_Pins = GPIOPIN.Pins
	G_state = 0 
	
	# Note—(Rule of turn on)	
	TurnOnRange_4 = 4 #多於此數則點亮四顆燈	
	TurnOnRange_3 = 3 #多於此數則點亮三顆燈 
	TurnOnRange_2 = 2 #多於此數則點亮兩顆燈
	TurnOnRange_1 = 1 #多於此數則點亮一顆燈
	SleepTime =1 # 網路版與本機板反映延遲時間(秒)	
	# save document
	DocumentContent = "INSERT INTO,config\n"
	DocumentContent += "PinId,DeviceName,Time,state,note\n"
while True:
		ret, img = cam.read()
		vis = PicData(img,cascade)
		#print type(img)
		#print type(vis)
		cv2.imshow('facedetect', vis.DrawPic)
		print vis.PeopleNum
		if vis.PeopleNum >= TurnOnRange_4 and G_state != 4:
			LightNum = 4
			# ************************** gpio function begin
			
			if len(G_Set) <= LightNum:
				LightNum = len(G_Set)
			for i in range(len(G_Set)):#local
				if i < LightNum:
					G_Set[i].on() #開啟本機電源
					print G_Devices[i]+" on (local)"					
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,local,\n"
				else:
					G_Set[i].off() #關閉本機電源
					print G_Devices[i]+" off (local)"
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,local,\n"
				
				
			time.sleep(SleepTime)	
			for i in range(len(G_Set)):#online
				if i <= LightNum:
					r = rq.get(WebServerAddress+"GpioAjaxOn.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,Network,\n"
				else:
					r = rq.get(WebServerAddress+"GpioAjaxOff.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,Network,\n"
			# ************************** gpio function end
			G_state = 4
		elif vis.PeopleNum >= TurnOnRange_3 and vis.PeopleNum < TurnOnRange_4 and G_state != 3:
			LightNum = 3
			# ************************** gpio function begin
			
			if len(G_Set) <= LightNum:
				LightNum = len(G_Set)
			for i in range(len(G_Set)):#local
				if i < LightNum:
					G_Set[i].on() #開啟本機電源
					print G_Devices[i]+" on (local)"					
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,local,\n"
				else:
					G_Set[i].off() #關閉本機電源
					print G_Devices[i]+" off (local)"
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,local,\n"
				
				
			time.sleep(SleepTime)	
			for i in range(len(G_Set)):#online
				if i <= LightNum:
					r = rq.get(WebServerAddress+"GpioAjaxOn.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,Network,\n"
				else:
					r = rq.get(WebServerAddress+"GpioAjaxOff.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,Network,\n"
			# ************************** gpio function end	
			G_state = 3
		elif vis.PeopleNum >= TurnOnRange_2 and vis.PeopleNum < TurnOnRange_3 and G_state != 2:
			LightNum = 2
			# ************************** gpio function begin
			
			if len(G_Set) <= LightNum:
				LightNum = len(G_Set)
			for i in range(len(G_Set)):#local
				if i < LightNum:
					G_Set[i].on() #開啟本機電源
					print G_Devices[i]+" on (local)"					
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,local,\n"
				else:
					G_Set[i].off() #關閉本機電源
					print G_Devices[i]+" off (local)"
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,local,\n"
				
				
			time.sleep(SleepTime)	
			for i in range(len(G_Set)):#online
				if i <= LightNum:
					r = rq.get(WebServerAddress+"GpioAjaxOn.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,Network,\n"
				else:
					r = rq.get(WebServerAddress+"GpioAjaxOff.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,Network,\n"
			# ************************** gpio function end
			G_state = 2
		elif vis.PeopleNum >= TurnOnRange_1 and vis.PeopleNum < TurnOnRange_2 and G_state != 1:
			LightNum = 1
			
			# ************************** gpio function begin
			
			if len(G_Set) <= LightNum:
				LightNum = len(G_Set)
			for i in range(len(G_Set)):#local
				if i < LightNum:
					G_Set[i].on() #開啟本機電源
					print G_Devices[i]+" on (local)"					
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,local,\n"
				else:
					G_Set[i].off() #關閉本機電源
					print G_Devices[i]+" off (local)"
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,local,\n"
				
				
			time.sleep(SleepTime)	
			for i in range(len(G_Set)):#online
				if i <= LightNum:
					r = rq.get(WebServerAddress+"GpioAjaxOn.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",on,Network,\n"
				else:
					r = rq.get(WebServerAddress+"GpioAjaxOff.php?n="+str(G_Pins[i])) #開啟網路電源
					print G_Devices[i]+" on (Network)"				
					# update document 
					DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,Network,\n"
			# ************************** gpio function end
				
			G_state = 1

		elif vis.PeopleNum == 0 and G_state != 0:			
			for i in range(len(G_Set)):
				G_Set[i].off() 	#關閉本機電源			
				r = rq.get(WebServerAddress+"GpioAjaxOff.php?n="+str(G_Pins[i]))#關閉網路電源
				print G_Devices[i]+" off"
				# update document 
				DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,Network,\n"
				DocumentContent +=str(G_Pins[i])+","+G_Devices[i]+","+str(dt.datetime.now())+",off,local,\n"
				
			G_state = 0
			
		else:
			print "GPIO works"	
		
		if 0xFF & cv2.waitKey(5) == 27:
			for i in range(len(G_Set)):
				G_Set[i].clean()
				r = rq.get(WebServerAddress+"GpioAjaxOff.php?n="+str(G_Pins[i]))#關閉網路電源

			w = open("output_"+str(dt.datetime.now())+".txt",'w')
			w.writelines(DocumentContent)
			w.close()
			print "end"
			break
		time.sleep(0)
	cv2.destroyAllWindows()
