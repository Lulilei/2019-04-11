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
	with open('numOfRatedItems.txt','w') as fw:
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

# input:dataset of ratings.txt, itemID (type:str)
# output:the list of UserID, rated Items and ratings for all users satisfying the required conditions
def getUAndIAndRList(txtName, itemID, wFileTxt2):
	numOfRatedItems=countRatedItems(txtName)
	
	totalUserNum=49291
	# relationship: itemIDInfoList is included in userInfoList
	userInfoList = [[] for i in range(totalUserNum)] # save all user information whose rated number is greater than 3	
	userInfo = []
	itemIDInfoList = [[] for i in range(totalUserNum)] # save the temporary information of the designated itemID for the current user
	itemIDInfo = []
	
	with open(txtName,'r') as fr:
		all_data = fr.readlines()
	for i in range(totalUserNum):
		if numOfRatedItems[i] >= 3:
			for line in all_data:
				temp = line.strip('\n').split('\t')
				#if (int(temp[0]) == i):
				#	userInfo = [int(temp[0]),int(temp[1]),int(temp[2])]
				#	userInfoList[i].append(userInfo)
				if (int(temp[0]) == i) and (int(temp[1]) == itemID):
					itemIDInfo=[int(temp[0]),int(temp[1]),int(temp[2])]
					itemIDInfoList[i] = itemIDInfo
	#print len(userInfoList), len(itemIDInfoList)
	
	# save the result to two .txt files:
	#wFileTxt1 = 'userInfoList.txt'
	'''
	with open(wFileTxt1,'w') as fw:
		for i in range(len(userInfoList)):
			if userInfoList[i] != []:
				fw.write(str(userInfoList[i]))
				fw.write('\n')
	'''
	#wFileTxt2 = 'itemIDInfoList.txt'
	with open(wFileTxt2,'w') as fw:
		for i in range(len(itemIDInfoList)):
			if itemIDInfoList[i] != []:
				fw.write(str(itemIDInfoList[i]))
				fw.write('\n')
		
	#return userInfoList, itemIDInfoList
	
# test the def function:
if __name__=="__main__":
	'''
	# test
	txtName='D:/data2.txt'
	itemID='10'
	'''
	txtName = 'data/ratings.txt'
	#numOfRatedItems = countRatedItems(txtName)
	
	# test 10 times
	itemID = [[] for i in range(200)]
	wFileTxt = [[] for i in range(200)]
	
	for i in range(1):
		wFileTxt[i] = 'itemInfoList' + str(i) + '.txt'		
		temp = genRandItemID()
		if temp not in itemID:
			itemID[i] = temp
	#print itemID
		#print wFileTxt[i]
		getUAndIAndRList(txtName, itemID[i], wFileTxt[i])
	
	#print userInfoList
	#print itemIDInfoList
	