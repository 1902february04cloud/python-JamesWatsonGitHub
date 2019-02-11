#!/usr/bin/env python3
'''
**Program that solves 10 different question**
James Watson
Revature Cloud Admin Program
2/10/2019
'''
#imports nessasary write to file functionality
import os
#main method
def main():
	#setup for calling all my functions and calling them
	print('***Print Hello World backwards***')
	reversePrint = reverse('Hello World')
	print(reversePrint)
	print()
	print('***Print the acronym of Access Control List***')
	acronymPhrase = acronym('Access Control List')
	print(acronymPhrase)
	print()
	print('***What kind of triangle has side lengths of 10.1, 10.3, and 10.2***')
	triangleType = whichTriangle(10.1, 10.3, 10.2)
	print(triangleType)
	print()
	print('***Your scrabble word is cabbage. The score is:***')
	score = scrabble('cabbage')
	print(score)
	print()
	print('***20 an armstrong number!***')
	armstrongNumberTest = armstrong(20)
	print(armstrongNumberTest)
	print()
	print('Print all prime factors of 100')
	primeFactorsResult = primeFactors(100)
	print(primeFactorsResult)
	print()
	print('Is this a pangram: The quick brown fox jumps over the lazy dog')
	pangramSentence = pangram('The quick brown fox jumps over the lazy dog')
	print(pangramSentence)
	print()
	print('Print the list in order: 7,4,8,2,7,5,1')
	sortedList = sort([7,4,8,2,7,5,1])
	print(sortedList)
	print()
	print ('ROT 13 Cypher of the word: dOg DoG Zz')
	rot = rotate(13, 'dOg DoG Zz')
	print(rot)
	print() 
	evenAndOdds()
#reverseFunction
def reverse(string):
	reverseString = ''
	length = len(string)
	#iterate through the length of string
	while length > 0:
		#reverse string through index
		reverseString = reverseString + string[length - 1]
		length = length - 1
	#set string equal to my new backwards string
	string = reverseString
	return string
#acronym function
def acronym(phrase):
	shortPhrase = ''
	#find upper case letters. Then add them to empty list
	for p in phrase:
		if p.isupper():
			shortPhrase = shortPhrase + p
	#set it equal to new acronym
	phrase = shortPhrase
	return phrase
#finding type of triangle
def whichTriangle(sideOne, sideTwo, sideThree):
	triangle = ''
	#if they are all equal, its equilateral
	if sideOne == sideTwo and sideTwo == sideThree and sideOne == sideThree:
		triangle = 'Equilateral Triangle'
	#if only two sides match, isosceles
	elif sideOne == sideTwo or sideTwo == sideThree or sideOne == sideThree:
		triangle = 'Isosceles Triangle'
	#else scalene
	else:
		triangle = 'Scalene Triangle'
	
	return triangle
#find value of scabble word
def scrabble(word):
	#set values for each string
	scrabbleScore = 0
	value1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
	value2 = ['D', 'G']
	value3 = ['B', 'C', 'M', 'P']
	value4 = ['F', 'H', 'V', 'W', 'Y']
	value5 = ['K']
	value6 = ['J', 'X']
	value7 = ['Q', 'Z']
	#for loops that iterate over the word to find the ;etter and assign them a score
	for w in word:
		for v in value1:
			if w.upper() == v:
				#ensures that it keeps adding up score
				scrabbleScore = scrabbleScore + 1
		for v in value2:
			if w.upper() == v:
				scrabbleScore = scrabbleScore + 2	
		for v in value3:
                        if w.upper() == v:
                                scrabbleScore = scrabbleScore + 3
		for v in value4:
                        if w.upper() == v:
                                scrabbleScore = scrabbleScore + 4
		for v in value5:
                        if w.upper() == v:
                                scrabbleScore = scrabbleScore + 5
		for v in value6:
                        if w.upper() == v:
                                scrabbleScore = scrabbleScore + 8
		for v in value7:
                        if w.upper() == v:
                                scrabbleScore = scrabbleScore + 10
	return scrabbleScore
#find armstrong number
def armstrong(number):
	#set variables
	calculatedNumber = 0
	armstrongNumber = False
	stringNumber = str(number)
	numLength = len(stringNumber)
	#iterate through number
	for n in stringNumber:
		#grab that number to the power of the length number
		newNumber = int(n)**int(numLength)
		#calculate new number
		calculatedNumber = calculatedNumber + newNumber
	#if they are equal, return true
	if number == calculatedNumber:
		armstrongNumber = True

	return armstrongNumber
#find prime factors
def primeFactors(number):
	#set variables
	primeFactors = set([])
	allFactors = []
	#find all the factors using iteration 
	for n in range(1, number + 1):
		if number % n == 0:
			allFactors.append(n)
	#find all prime factors using the same iteration
	for a in allFactors:
		if a > 1:
			for n in range(2, a + 1):
				if a % n == 0:		
					primeFactors.add(n)
					break				
	return primeFactors
#find pangram
def pangram(sentence):
	#set variables
	pangramList = 'abcdefghijklmnopqrstuvwxyz'
	pangramSentence = True
	#if all letters are not in sentence, return false
	for x in pangramList:
		if x not in sentence.lower():
			pangramSentence = False
	return pangramSentence
#sort 
def sort(numbers):
	#iterate through the index to the length of numbers
	for x in range(len(numbers)):
		#iterate through the numbers one index ahead of x
		for y in range(x + 1, len(numbers)):
			#swap varaibles using temp if x is larger
			if numbers[x] > numbers[y]:
				temp = numbers[x]
				numbers[x] = numbers[y]
				numbers[y] = temp
	return numbers
#rot
def rotate(key, string):
	#set variables
	completedCypher = ''
	addingNew = []
	uppercaseList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	lowercaseList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#iterate string
	for letter in string:
		if letter in uppercaseList:
			for index in range(len(uppercaseList)):
				#if letter is an uppercase letter
				if letter == uppercaseList[index]:
					newIndex = index + key
					#if we reach the end of list, loop around
					if newIndex > 25:
						#set looped letter and index
						newIndex = newIndex - 26
						newLetter = uppercaseList[newIndex]
					else:
						newLetter = uppercaseList[newIndex]
			#add letter		
			addingNew.append(newLetter)
		#same thing as above but for lowercase letter	
		elif letter in lowercaseList:
			for index in range(len(lowercaseList)):
				if letter == lowercaseList[index]:
					newIndex = index + key
					if newIndex > 25:
						newIndex = newIndex - 26
						newLetter = lowercaseList[newIndex]					
					else:
						newLetter = lowercaseList[newIndex]

			addingNew.append(newLetter)
		#if there is a space, add it to list
		if letter == ' ':
			addingNew.append(' ')
	#join the list
	completedCypher = completedCypher.join(addingNew)
	return completedCypher
#print even and odd to different text files		
def evenAndOdds():
	#write over them at the beginning of script, to be blank
	evenTxt = open('even.txt','w')
	evenTxt.write('')
	oddTxt = open('odd.txt', 'w')
	oddTxt.write('')
	count = 0
	print('Input 10 numbers and I will put them in even and odd files:')
	#iterate 10 times to find 10 integers
	while count < 10:
		number = input()
		count = count + 1
		#if even, add it to even file
		if int(number) % 2 == 0:
			open('even.txt','a+')
			evenTxt.write(number + '\n')
		#else add it to odd file
		else:
			open('odd.txt','a+')
			oddTxt.write(number + '\n')
	#close files
	evenTxt.close()
	oddTxt.close()
	

if __name__ == '__main__':
	main()
