import botocore
import boto3
import matplotlib.pyplot as plt
import numpy as np

s3_resource = boto3.resource('s3')
s3 = boto3.client('s3')
ans = np.array([])
output = np.array([])
interval = 2

def begin():
	"""will download all processed data files from indicated
	bucket and display data in files on a graph"""
	try:

		bucket = 'example32317'
		response1 = s3.list_objects(
			Bucket=bucket)
		for obj in response1["Contents"]:
			key = obj["Key"]
			
			if (key[0:5] == 'Final'):
				print key
				response = s3.get_object(
					Bucket = bucket,
					Key = key
				)

				data = response["Body"].read()
				dataArr =  data.split(',')

				dataArr = dataArr[0:len(dataArr)-1]
				dataFin = []
				for x in dataArr:
				  dataFin.append(int(x))

				output = np.append(output,dataFin)
				print output

				[dc,date,time] = key.split('%')
				[hr,mint,sec] = time.split(':')

				print time,mint
				for i in xrange(0,len(output)):
					newTime = int(mint) + i*interval
					newTime = hr +':'+ str(newTime) + '.'+ sec
					ans = np.append(ans,newTime)

		plt.stem(range(len(output)), output)
		plt.xticks(range(len(output)), ans, fontsize = 4)
		plt.xlabel('Time')
		plt.ylabel('Temp')
		plt.title('Temp for '+ date)
		plt.show()
 
	except:
		print("Error")
	