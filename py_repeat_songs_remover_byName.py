import os
import sys

def lsHyphenlParser(lsHyphenlLine):
	lsHypenlList = [part for part in lsHyphenlLine.split(" ")]
	# removing file permissions
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0) 
	# removing number of links
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0)
	# removing owner name
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0)
	# removing owner group
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0)
	# removing size of the file
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0)
	# removing month
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0)
	# removing day
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0)
	# removing year 
	while lsHypenlList[0] == "":
		lsHypenlList.pop(0)
	lsHypenlList.pop(0)	
	fileName = ""
	for parts in lsHypenlList:
		fileName = fileName + parts + " "
	fileName = fileName[:-1]
	return fileName

def convertedFileName(fileName):
	escapeCharacters = ['\'']
	ret = "'"
	for c in fileName:
		if c == ' ':
			ret = ret + ' '
		elif c in escapeCharacters:
			ret = ret + "'\\'" + c
		else:
			ret = ret + c
	ret = ret + "'"
	return ret

def inEachDirectory(dirPath,allFilesListStr):
	os.chdir(dirPath)
	allFiles = os.popen("ls -l | egrep -v '^d'").read()
	allFilesList = [fileLine for fileLine in allFiles.split("\n")]
	allFilesList.pop(0)
	for fileLine in allFilesList:
		if len(fileLine) == 0:
			continue
		fileName = lsHyphenlParser(fileLine)
		allFilesListStr.add(fileName)
	allDirectories = os.popen("ls -l | egrep '^d'").read()
	allDirectoriesList = [directoryLine for directoryLine in allDirectories.split("\n")]
	allDirectoriesListStr = []
	for directoryLine in allDirectoriesList:
		if len(directoryLine) == 0:
			continue
		directoryName = lsHyphenlParser(directoryLine)
		allDirectoriesListStr.append(directoryName)
	for directory in allDirectoriesListStr:
		inEachDirectory(dirPath + directory + "/",allFilesListStr)

def delDupsInEachDirectory(dirPath,allFilesListStr):
	os.chdir(dirPath)
	allFiles = os.popen("ls -l | egrep -v '^d'").read()
	allFilesList = [fileLine for fileLine in allFiles.split("\n")]
	allFilesList.pop(0)
	for fileLine in allFilesList:
		if len(fileLine) == 0:
			continue
		fileName = lsHyphenlParser(fileLine)
		if fileName in allFilesListStr:
			allFilesListStr.remove(fileName)
		else:
			currDirectory = os.popen("pwd").read()
			currDirectory = currDirectory[:-1]
			currDirectory = currDirectory + "/"
			currFile = currDirectory + fileName
			print("\n" + currFile + "\n")
			os.system("rm " + convertedFileName(fileName))
	allDirectories = os.popen("ls -l | egrep '^d'").read()
	allDirectoriesList = [directoryLine for directoryLine in allDirectories.split("\n")]
	allDirectoriesListStr = []
	for directoryLine in allDirectoriesList:
		if len(directoryLine) == 0:
			continue
		directoryName = lsHyphenlParser(directoryLine)
		allDirectoriesListStr.append(directoryName)
	for directory in allDirectoriesListStr:
		delDupsInEachDirectory(dirPath + directory + "/",allFilesListStr)



def main():
	argsList = list(sys.argv)
	if argsList[1][len(argsList[1]) - 1] != '/':
		argsList[1] = argsList[1] + '/'
	try:
		os.chdir(argsList[1])
	except:
		print("No Such Directory")
		exit()
	allFilesListStr = set()
	inEachDirectory(argsList[1],allFilesListStr)
	os.chdir(argsList[1])
	delDupsInEachDirectory(argsList[1],allFilesListStr)
	
if __name__ == '__main__':
	main()
