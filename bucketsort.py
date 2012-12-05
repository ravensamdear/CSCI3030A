# Copyright (c) 2012 SAMUEL D. DEAR

# Permission is hereby granted, free of charge, to any person  obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#User defined queue class for specific use.
class Queue:
	#Constructor, declare each variable
	def __init__(self):
		self.inst = []
		self.outst = []
		self.size = 0
	#Push method, add object to queue(list)
	def push(self, obj):
		self.inst.append(obj)
		self.size = self.size + 1
	#Pop method, remove object from queue 
	def pop(self):
		if not self.outst:
			self.inst.reverse()
			self.outst = self.inst
			self.inst = []
		self.size = self.size - 1
		return self.outst.pop()
	#isEmpty method, check to see if the queue is empty.
	def isEmpty(self):
		if self.size == 0:
			return 1
		else:
			return 0
#user defined bucket sort class, takes in a list, max number in list, and the length of each subset.
def bucket(A, m, n):
	print ("Initial subsets of interval [1," + str(m) + "] of length " + str(n) + ":")	
	for var in A:
		print var,
	print
	#B is the bucket list.
	B = []
	passcount = 0
	r=0
	#B becomes a list of queues
	while(r < m):
		B.append(Queue())
		r += 1
	p = n-1
	#Pass Loop
	while(p >= 0):
		#Each Bucket
		i = 0
		for i in range(m):
			#Traverse A
			j = 0
			for j in range(len(A)):
				#If the last element in the subset matches the bucket number, put it in that queue				
				if A[j][p] == i + 1:
					B[i].push(A[j])
				j +=1 
			i += 1
		A = []		
		y = 0
		#Pop all elements out of queue in order into A
		while y < m:
			while(not(B[y].isEmpty())):							
				A.append(B[y].pop())
			y += 1
		passcount = passcount+1
		print("Pass " + str(passcount) + ":")		
		for var in A:
			print var,
		print
		p -= 1
	return A


#----------------TESTING SCRIPT-----------------

A = [[2,1,3],[3,2,3],[1,2,1],[2,3,2],[1,1,3],[3,1,1],[3,3,1],[2,2,2]]

bucket(A,3,3)

A = [[1,4,5,3],[3,5,4,2],[5,4,4,2],[1,1,2,1],[4,3,3,2],[2,5,5,1],[4,3,5,5],[4,5,5,5],[5,4,4,3]]

bucket(A, 5, 4)
