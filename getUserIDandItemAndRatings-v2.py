import numpy as np
import random
# count the number of rated items for each user and save in a list named as numOfRatedItems
def countRatedItems(txtName):
	with open(txtName,'r') as fr:
		all_data = fr.readlines()
	totalUserNum = 49291
	#totalUserNum=110 # for test
	numOfRatedItems = [0 for i in range(totalUserNum)]	
	for line in all_data:
		temp = line.strip('\n').split('\t')
		userID = int(temp[0])
		#print userID
		numOfRatedItems[userID] += 1
	with open('data/numOfRatedItems.txt','w') as fw:
		for i in range(len(numOfRatedItems)):
			fw.write(str(numOfRatedItems[i]))
			fw.write('\n')
	return numOfRatedItems

# generate random itemID to be predicted for a certain user
def genRandItemID():
	totalUserNum = 49290
	userID = random.randint(1,totalUserNum) # including 1 and totalUserNum
	print userID
	with open('data/numOfRatedItems.txt','r') as fr:
		all_data=fr.readlines()
		while (all_data[userID] != ''):
			if int(all_data[userID]) >= 3:
				break
			else:
				userID += 1
		print userID
		if userID > totalUserNum:
			genRandItemID()
		print userID
		lenItemForuserID = int(all_data[userID])
		print "len is:",lenItemForuserID
		tempInt = random.randint(1, lenItemForuserID)		
		print tempInt
	
	#find the itemID from the ratings.txt
	with open('data/ratings.txt','r') as fr:
		all_ratings = fr.readlines()
	itemID = 0
	num = 1
	for line in all_ratings:
		temp = line.strip('\n').split('\t')		
		if int(temp[0]) == userID:			
			if num == tempInt:		
				itemID = int(temp[1])
				break
			else:
				num += 1
				continue
	print itemID
	return itemID

# input: userInfoList.txt, itemID (type:str)
# output:a list file with userID, rated itemID and ratings from all users who rated itemID and the number of total rating items is bigger than 3
def getUAndIAndRList(userInfoListTxt, itemIDList, wFileTxt):
	with open(userInfoListTxt, 'r') as fr:
		all_data = fr.readlines()
	totalUserNum = len(all_data)
	totalItemID = len(itemIDList)
	itemIDComRatedList = [[] for i in range(totalItemID)] # save the temporary information of the designated itemID for the current user
	itemIDInfo = []
	
	for i in range(totalUserNum):		
		lenOfItemRatedLeast3ByUi = len(all_data[i])
		for j in range(lenOfItemRatedLeast3ByUi):
			temp = all_data[i][j]
			for k in range(totalItemID):
				if (int(temp[i][j][1]) == itemIDList[k]):
					itemIDInfo=[int(temp[i][j][0]),int(temp[i][j][1]),int(temp[i][j][2])]
					itemIDComRatedList[k].append(itemIDInfo)
	# save the result to multiple .txt files (the number is totalItemID):
	for k in range(totalItemID):
		with open(wFileTxt,'w') as fw:
			for i in range(len(itemIDComRatedList[k])):
				if itemIDComRatedList[k] != []:
					fw.write(str(itemIDInfoList[k][i]))
					fw.write('\n')
	#return userInfoList, itemIDInfoList
	
# test the def function:
if __name__=="__main__":
	txtName = 'data/userInfoList.txt'
	
	# test 10 times
	# produce 100 different itemIDs as the input parameters of getUAndIAndRList function
	# in order to further get common rated itemInfo files for 100 times
	for i in range(10):
		wFileTxt[i] = 'itemInfoList' + str(i) + '.txt'		
		temp = genRandItemID()
		if temp not in itemID:
			itemID[i] = temp
	#print itemID
		#print wFileTxt[i]
		getUAndIAndRList(txtName, itemIDList, wFileTxt[i])
	