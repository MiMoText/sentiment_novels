# Script for adding header to sentiment files, add year, title and text
# For working with this Script, you need both the plain text files and the metadatatable of the roman18 repo
# which can be found here:
# https://github.com/MiMoText/roman18/tree/master/plain/files
# https://github.com/MiMoText/roman18/blob/master/XML-TEI/xml-tei_metadata.tsv
# Please set the parameters file_path and metadatafile to the according folder / file on your computer
import glob
from os.path import join
import pandas as pd
import os.path

# Parameters
file_path = join("..", "..", "..", "roman18", "plain", "files", "*.txt")

# last part of savepath has to be adjusted to "mimotext" (instead of "testheader")
save_path = join("..", "..", "sentiments", "toolchain_18th_century", "texts", "mimotext")
metadatafile = join("..", "..", "..", "roman18", "XML-TEI", "xml-tei_metadata.tsv")

# Functions
def read_metadata(metadatafile):
	# read metadata file to get year and title
	
	with open(metadatafile, "r", encoding ="utf8") as infile:
		metadata = pd.read_csv(infile, sep="\t")
	
	print(metadata.columns.to_list())
	return metadata

def read_file(txt):
	# read plain texts
	with open(txt, "r", encoding="utf8") as infile:
		text = infile.read()

	return text 
	
	
def add_metadata(metadata, text, name, missing_data):
	# get title and year for each file from metadata-table

	# remove leading whitespace from text
	text = text.lstrip()
	sentimenttext = ""
	# get year
	try:
		year = metadata.loc[metadata["filename"] == name, "firsted-yr"].values[0]
		if pd.isna(year):
			year = "0000"
			missing_data["{}".format(name)]["year"] = "x"
	except IndexError:
		print("year not found in metadatatable")
		missing_data["{}".format(name)]["year"] = "x"
		year = "0000"

	# get title
	try:
		title = metadata.loc[metadata["filename"] == name, "title"].values[0]
	except IndexError:
		print("title not found in metadatatable")
		missing_data["{}".format(name)]["title"] = "x"
		title = "No_title_found"

	# get bgrf:
	try:
		bgrf = metadata.loc[metadata["filename"] == name, "bgrf"].values[0]
	except IndexError:
		print("bgrf not found in metadatatable")
		missing_data["{}".format(name)]["bgrf"] = "x"
		bgrf = "No_bgrf_found"

	# merge year title and text
	sentimenttext = "year={}\n".format(int(year)) + "title={}\n".format(title) + "bgrf={}\n".format(bgrf) + "text=" + text
	#print(sentimenttext[:200])

	return sentimenttext, missing_data
	
def save_text(sentimenttext, name, savepath):
	# write text to savepath

	with open(join(savepath, "{}.txt".format(name)), "w", encoding="utf8") as outfile:
		outfile.write(sentimenttext)

def main(file_path,save_path, metadatafile):
	
	metadata = read_metadata(metadatafile)

	# get all ids from metadata file and from text files to check whether all texts are included
	metadata_ids = list(metadata["filename"])

	txt_ids = [] # these are added in the following for-loop
	# create dictionary for missing values
	missing_data = {}

	for txt in glob.glob(file_path):
		
			name = os.path.basename(txt).split(".")[0]
			print(name)

			txt_ids.append(name)
			text = read_file(txt)
			missing_data["{}".format(name)] = {"year":None, "title":None, "text":None, "bgrf":None}
			sentimenttext, missing_data = add_metadata(metadata, text, name, missing_data)

			if sentimenttext != "":
				save_sentimenttext = save_text(sentimenttext, name, save_path)


	# check if title is in metadatafile, but not in plain-text
	for id in metadata_ids:
		if id not in txt_ids:
			missing_data["{}".format(id)] = {"text": "x"}

	missing_data_df = pd.DataFrame.from_dict(missing_data, orient="index")
	missing_data_df = missing_data_df.dropna(axis=0, how="all")
	# save missing data dataframe

	with open("missing_data.csv", "w", encoding = "utf8") as outfile:
		missing_data_df.to_csv(outfile)

main(file_path, save_path, metadatafile)


