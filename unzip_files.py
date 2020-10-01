def unzip(file_path):
	"""Unzip .zip file"""
	! unzip file_path


def unzip_gz(file_path, target_dir):
	"""Unzip .gz file and move to the target dir."""
	! gunzip file_path
	# mv names*.csv target_dir


def unzip_tar_gz(file_path, target_dir):
	"""Unzip the .tar.gz file to the target dir."""
	! tar -xvf file_path -C target_dir
	# ! tar -zxvf file_path -C target_dir  # alternatively


from zipfile import ZipFile 
def unzip_zipfile(zip_path):
	"""Extract all the contents of zip file in current dir"""
with ZipFile(zip_path, "r") as zipObj:
	zipObj.extractall()
