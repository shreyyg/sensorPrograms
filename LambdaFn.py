import botocore
import boto3
import datetime


s3 = boto3.client('s3')

errOcccur = False


#mydic = {u'Records': [{u'eventVersion': u'2.0', u'eventTime': u'2017-04-06T14:23:21.182Z', u'requestParameters': {u'sourceIPAddress': u'35.167.67.93'}, u's3': {u'configurationId': u'36abe657-34aa-4005-919c-88312dcc88a2', u'object': {u'eTag': u'b49b51d8890e9c9c10d7e71567a81c10', u'sequencer': u'0058E64F5921E8F0C6', u'key': u'2017/04/06/14/sample-1-2017-04-06-14-18-19-bce45f27-a3eb-46b8-a873-174e3e35b27c', u'size': 38}, u'bucket': {u'arn': u'arn:aws:s3:::example32317', u'name': u'example32317', u'ownerIdentity': {u'principalId': u'AKVW7J3JIEY7F'}}, u's3SchemaVersion': u'1.0'}, u'responseElements': {u'x-amz-id-2': u'9JeZCug+0zfovQUuPFtNgbkbV4/0WIlj0nUvE3ufelYJJwRiKJMDmB1K9//uuX0AyLXwh+hMSM0=', u'x-amz-request-id': u'5B525E1E6B94D998'}, u'awsRegion': u'us-west-2', u'eventName': u'ObjectCreated:Put', u'userIdentity': {u'principalId': u'AWS:AROAIJBGNTXJWAPARENCQ:AWSFirehoseToS3'}, u'eventSource': u'aws:s3'}]}
#bucket = mydic['Records'][0]['s3']['bucket']['name']
#key =  mydic['Records'][0]['s3']['object']['key']
bucket = 'example32317'
key = 'Final-2017-04-0616:29:26.225439'


try:
	
   #s3.download_file(bucket, 'sample-1-2017-03-30-14-10-11-84009d5b-d0e4-4b80-8fd6-769e8a1c0aee','test2.txt')
   # List all objects within a S3 bucket path
	response = s3.get_object(
		Bucket = bucket,
		Key = key
	)
	data = response["Body"].read()
	print data
	dataArr =  data.split(',')

	dataArr = dataArr[0:len(dataArr)-1]
	dataFin = []
	for x in dataArr:
	  dataFin.append(int(x))

	output = [0] * len(dataFin)
	for i in xrange(len(dataFin)):
		if (dataFin[i] >= 97):
			output[i] = 1


	dataUpload = ''.join((str(x) + ',') for x in output)
	body = dataUpload[0:len(dataUpload)-1]

	dt = datetime.datetime.now()
	date = dt.date()
	time = dt.time()
	filename= 'Final-' + str(date) + str(time)
	
	response  = s3.put_object(
	 	Body = body,
	 	Bucket = bucket,
	 	Key = filename,
	 	)


	

	# # Loop through each file
	# for filename in response['Contents']:
	# 	print filename
	# 	name = filename['Key'].rsplit('/', 1)
	# 	print name

except botocore.exceptions.ClientError as err:
	errorCode = int(err.response['Error']['Code'])
	errOcccur = True
	

print errOcccur
print response