import threespace_api as ts_api
import time
import math
import thread

from threading import Thread

numDevices = 2
lenInterval = 11

dng_device = None
wl_device = None
wl_devices = []

concatData = []
threads = []

mutex = thread.allocate_lock()

class threadFunction(Thread):
	def __init__(self, param):
		Thread.__init__(self)
		self.param = param

	def run(self):
		mutex.acquire()
		concatData.append(getData(self.param))
		mutex.release()


def begin():
	"""NEED TO PAIR DEVICES FIRST
	will read temp from paired devices for given time
	then write data to an array
	uses thread for each sensor"""
	device_list = ts_api.getComPorts(filter=ts_api.TSS_FIND_DNG)
	print device_list

	com_port = device_list[0]
	dng_device = ts_api.TSDongle(com_port=com_port)


	for i in xrange(numDevices):
		wl_devices.append(dng_device[i])

	for device in wl_devices:
		newThread = threadFunction(device)
		threads.append(newThread)
		newThread.start()

	for thread in threads:
		thread.join()

	return concatData


def getData(wl_device):

	wl_device.setStreamingTiming(interval=1000000, duration=100000000, delay=0)
	wl_device.setStreamingSlots(slot0='getTemperatureF')
	wl_device.startStreaming()
	wl_device.startRecordingData()

	time.sleep(lenInterval)

	wl_device.stopRecordingData()
	wl_device.stopStreaming()

	data = wl_device.stream_data

	wl_device.close()    


	finalFormData  = [0] * len(data)
	for i in xrange(0,len(data)):
		finalFormData[i] =  math.ceil(data[i][1])

	return finalFormData


