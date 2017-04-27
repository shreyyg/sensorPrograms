import botocore
import boto3



client = boto3.client('firehose')
patientName = 'sample'

#data= ''.join((str(x) + ',') for x in [0x61, 0x64, 0x67,0x6f,0x5e, 0x5f, 0x5d, 0x62, 0x63, 0x64, 0x65])


def begin(unModData):
	"""pass in unmodified data array
	will write the data to indicated bucket in cloud"""
	
	data= ''.join((str(x) + ',') for x in unModData)
	response = client.put_record(
	    DeliveryStreamName= patientName,
	    Record={
	        'Data': data
	    }
	)

	return response
