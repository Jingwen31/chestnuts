import boto3
import botocore


def download_file_from_s3_awscli(s3_uri->str, file_path->str):
	! aws s3 cp s3_uri file_path


def download_file_from_s3(bucket_name->str, s3_key->str, file_name->str):
	"""
	Download file from S3 using boto3.

	Parameters:
	-----------
	bucket_name: the name of the S3 bucket.
	s3_key: the name of the object starting from the folder inside the bucket.
	file_name: the filename to be saved locally.
	"""
	s3 = boto3.resource("s3")
	try:
		s3.Bucket(bucket_name).download_file(s3_key, file_name)
	except botocore.exceptions.ClientError as e:
    	if e.response['Error']['Code'] == "404":
        	print("The object does not exist.")
    	else:
    		raise


def download_file_from_s3_alter(bucket_name->str, s3_key->str, file_name->str):
	"""
	The alternative way to use boto3 to download file from s3.

	Parameters:
	-----------
	bucket_name: the name of the S3 bucket.
	s3_key: the name of the object starting from the folder inside the bucket.
	file_name: the filename to be saved locally.
	"""
	s3 = boto3.client("s3")
	s3.download_file(bucket_name, s3_key, file_name)


def download_directory_from_s3(bucket_name->str, remote_directory_name>str):
	"""
	Download the directory from S3.
	"""
	s3 = boto3.resource("s3")
	bucket = s3.Bucket(bucket_name)
	for obj in bucket.objects.filter(Prefix=REMOTE_DIRECTORY_NAME):
		fn = Path(obj.key)
		if not fn.parent.exists():
			fn.parent.mkdir(parents=True)
		try:
			bucket.download_file(str(fn), str(fn))
		except:
			print("Failed to download file named" + fn)





