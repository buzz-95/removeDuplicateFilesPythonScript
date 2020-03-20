import os
import sys


class node:
	def __init__(self):
		self.arr = [None] * 10

class trie:
	def __init__(self):
		self.head = node()
	def addNcheck(self,key):
		idx = 0
		curr = self.head
		cnt = 0
		while idx < 23:
			if curr.arr[int(key[idx])] == None:
				newNode = node()
				curr.arr[int(key[idx])] = newNode
				curr = newNode
				cnt = cnt + 1
			else:
				curr = curr.arr[int(key[idx])]
			idx = idx + 1
		if cnt == 0:
			return True
		return False

mytrie = trie()


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

def processAllFiles(allFilesListStr):
	global mytrie
	for file in allFilesListStr:
		byteArray = open(file,"rb").read()
		hash1 = 0
		hash2 = 0
		hash3 = 0
		mod1 = 257
		mod2 = 1000000007
		mod3 = 1000000009
		for i in byteArray:
			if i == 0:
				i = 256
			hash1 = (hash1 * 256) % mod1
			hash1 = hash1 + int(i)
			hash2 = (hash2 * 256) % mod2
			hash2 = hash2 + int(i)
			hash3 = (hash3 * 256) % mod3
			hash3 = hash3 + int(i)
		hash1 = hash1 % mod1
		hash2 = hash2 % mod2
		hash3 = hash3 % mod3
		strhash1 = str(hash1)
		strhash2 = str(hash2)
		strhash3 = str(hash3)
		while len(strhash1) < 3:
			strhash1 = '0' + strhash1
		while len(strhash2) < 10:
			strhash2 = '0' + strhash2
		while len(strhash3) < 10:
			strhash3 = '0' + strhash3
		tothash = strhash1 + strhash2 + strhash3
		if mytrie.addNcheck(tothash):
			currDirectory = os.popen("pwd").read()
			currDirectory = currDirectory[:-1]
			currDirectory = currDirectory + "/"
			currFile = currDirectory + file
			print("\nDeleting " + currFile + "   ...\n")
			os.system("rm " + convertedFileName(file))
		#else:
		#	print(file + " : " + tothash)



def inEachDirectory(dirPath):
	os.chdir(dirPath)
	allFiles = os.popen("ls -l | egrep -v '^d'").read()
	allFilesList = [fileLine for fileLine in allFiles.split("\n")]
	allFilesList.pop(0)
	allFilesListStr = []
	for fileLine in allFilesList:
		if len(fileLine) == 0:
			continue
		fileName = lsHyphenlParser(fileLine)
		allFilesListStr.append(fileName)
	processAllFiles(allFilesListStr)
	allDirectories = os.popen("ls -l | egrep '^d'").read()
	allDirectoriesList = [directoryLine for directoryLine in allDirectories.split("\n")]
	allDirectoriesListStr = []
	for directoryLine in allDirectoriesList:
		if len(directoryLine) == 0:
			continue
		directoryName = lsHyphenlParser(directoryLine)
		allDirectoriesListStr.append(directoryName)
	for directory in allDirectoriesListStr:
		inEachDirectory(dirPath + directory + "/")

def main():
	argsList = list(sys.argv)
	if argsList[1][len(argsList[1]) - 1] != '/':
		argsList[1] = argsList[1] + '/'
	try:
		os.chdir(argsList[1])
	except:
		print("No Such Directory")
		exit()
	inEachDirectory(argsList[1])

if __name__ == '__main__':
	main()
