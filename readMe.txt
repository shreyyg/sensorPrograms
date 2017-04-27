getFileFromS3.py - downloads all processed-data files from specified bucket and stores the data locally. Currently makes a stem plot with the data

getSensorData.py - accesses connected dongle and reads specific data fields from paired sensors. Stores data into a data array.

LambdaFn.py - lambda function currently on AWS. Is triggered whenever a file with rawdata is uploaded to specified bucket on AWS. Takes data from file, processes  it and writes binary data to new file in bucket.

pairing_wireless_devices.py - taken from ThreeSpace. Pairs sensors with dongle

putRecordInBucket.py - takes raw data from sensors as input. Writes data to a file then uploads the file to specified bucket on AWS.