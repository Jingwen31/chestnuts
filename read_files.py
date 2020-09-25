import pandas as pandas


def read_tsv(file_path, columns->list):
	"""
	Read tsv file into pandas dataframe.

	Parameters:
	-----------
	columns: a list of column names.
	"""
	df = pd.read_csv(file_path, delimiter="\t", header=None, names=columns)
	return df