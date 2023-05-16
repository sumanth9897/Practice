# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:17:12 2022

@author: suman
"""

#addition  in 2 single linked lists

class Solution:
	
	def reverse(self, head):
		if head is None or head.next is None:
			return head
		prev = None
		next = None
		curr = head
		while curr is not None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		head = prev
		return head

	

	def addTwoLists(self, first, second):

		
		curr1 = self.reverse(first)
		curr2 = self.reverse(second)

		
		sum = 0
		carry = 0
		res = None
		prev = None
		x = 0

		
		while curr1 is not None or curr2 is not None:

			
			sum = carry + (curr1.data if curr1 else 0) + \
				(curr2.data if curr2 else 0)
			x = sum//10
			carry = (x if sum >= 10 else 0)
			sum = sum % 10
			
			temp = Node(sum)

			if res is None:
				res = temp
			else:
				prev.next = temp
			prev = temp
			if curr1:
				curr1 = curr1.next
			if curr2:
				curr2 = curr2.next
		if carry > 0:
			temp.next = Node(carry)

		ans = self.reverse(res)
		return ans


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, val):
		if self.head is None:
			self.head = Node(val)
			self.tail = self.head
		else:
			self.tail.next = Node(val)
			self.tail = self.tail.next




def printList(n):
	while n:
		print(n.data, end = ' ')
		n = n.next
	print()



if __name__ == "__main__":

	arr1 = [4, 155]
	LL1 = LinkedList()
	for i in arr1:
		LL1.insert(i)
	print("First list is", end = " ")
	printList(LL1.head)

	arr2 = [222,3456]
	LL2 = LinkedList()
	for i in arr2:
		LL2.insert(i)
	print("Second list is", end = " ")
	printList(LL2.head)

	
	res = Solution().addTwoLists(LL1.head, LL2.head)
	print("Resultant list is", end = " ")
	printList(res)

