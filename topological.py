# Copyright (c) 2012 SAMUEL D. DEAR

# Permission is hereby granted, free of charge, to any person  obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#Node object for use with the linked list
class node:
	#Constructor for node, takes in reference to the previous and next nodes in list
	def __init__(self,obj, prev, next):
		self.obj = obj
		self.previous = prev
		self.next = next
#a linked list object with reference to previous and next node
class doublyLinkedList:
	#constructor, initializes the list as empty.
	def __init__(self):
		self.start = None
		self.end = None
	#Inserts node before specified object.
	def addHere(self, objToInsert, objToBeInsertedBefore):
		#If list is empty, set the new node to first and last place. 
		if self.start == None:
			newnode = node(objToInsert, None, None)
			self.start = newnode
			self.end = newnode
		#If not, traverse the list to find the object you wish to insert before.
		else:
			trav = self.start
			while trav != None:
				if trav.obj == objToBeInsertedBefore:
					#If the object you wish to preempt is the first, set new node to the first.
					if(trav == self.start):
						newnode = node(objToInsert, None, trav)
						trav.previous = newnode
						self.start = newnode
					else:
						newnode = node(objToInsert, trav.previous, trav)
						trav.previous.next = newnode
						trav.previous = newnode
					break #Once found, break the loop.
				else: #If you don't find it, keep moving through the list
					trav = trav.next
	#Inserts object at the start of the list.
	def addStart(self, obj):
		#If list is empty, make proper adjustments to list.
		if self.start == None:
			newnode = node(obj, None, None)
			self.start = newnode
			self.end = newnode
		else:
			newnode = node(obj, None, self.start)
			self.start.previous = newnode
			self.start = newnode
	#Inserts object at the end of the list
	def addEnd(self, obj):
		#If the list is empty, just call addStart (no repetition)
		if self.start == None:
			self.addStart(obj)
		#Otherwise, add node to the end.
		else:
			newnode = node(obj, None, None)
			temp = self.end
			self.end = newnode
			newnode.previous = temp
			temp.next = newnode
	#Standard isEmpty function.
	def isEmpty(self):
		if self.start == None:
			return 1
		else:
			return 0
	#Prints the contents of the list as is.
	def printList(self):
		#check if the list is empty
		if self.start == None:
			print "The Linked List is empty..."
			return 0
		#Check if there is only one node
		if self.start.next == None:
			print self.start.obj
			return 1
		#Otherwise, print entire list.
		else:
			trav = self.start
			while trav != None:
				print trav.obj,
				trav = trav.next
			print
			return 1
	#Added for use in topSort functionality.
	def findListValue(self, obj):
		trav = self.start
		#Traverse list to see if the current object is subset of the next object
		while trav != None:
			#If so, return that object
			if set(obj).issubset(set(trav.obj)):
				return trav.obj
			#If not, keep going
			if not set(obj).issubset(set(trav.obj)):
				trav = trav.next
			else:
				trav = trav.next
		#If object is not subset to any element, return None
		return None

#Actual topsort function.
def topSort(aList):
	tList = doublyLinkedList()
	tList.addStart(aList[0])
	print 0
	print "Added: " + str(aList[0])
	i = 1
	temp = 1
	while i < len(aList):
		print i
		#set temp to the return value of findListValue
		temp = tList.findListValue(aList[i])
		#If no subset was found, insert new object at the end of the list
		if temp == None:
			print "Added: " + str(aList[i])
			tList.addEnd(aList[i])		
		#If it is a subset, add new object before returned object
		elif set(aList[i]).issubset(set(temp)):
			tList.addHere(aList[i], temp)
			print "Added: " + str(aList[i])
		#Default to add to the end of the list
		else:
			print "Added: " + str(aList[i])
			tList.addEnd(aList[i])
		i = i + 1
	print "Nothing to the left is superset to anything on the right,"
	print "and nothing to the right is subset to anything on the left."
	tList.printList()



#-------------------Testing Script------------------------

testList = [[1,2],[2,3],[1],[1,2,3],[1,3],[3],[2]]
print testList
topSort(testList)

print

testList = [[3, 6, 7], [10, 9, 3], [3], [1], [2], [1,2], [4,6], [10, 9], [10], [9], [6], [7], [5]]
print testList
topSort(testList)

print

testList = [[1, 5], [5], [1,3], [1, 3, 5], [4, 2, 3, 5], [4], [2, 4], [3, 4, 1, 5, 2]]
print testList
topSort(testList)

#-----------------------Output----------------------------

# sam@SAMS-TOME ~/Documents $ python topological.py
# [[1, 2], [2, 3], [1], [1, 2, 3], [1, 3], [3], [2]]
# 1
# Added: [2, 3]
# 2
# Added: [1]
# 3
# Added: [1, 2, 3]
# 4
# Added: [1, 3]
# 5
# Added: [3]
# 6
# Added: [2]
# [1] [2] [1, 2] [3] [2, 3] [1, 3] [1, 2, 3]
