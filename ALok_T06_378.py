'''
1. Implement palindrome using iterator(for loop) and generator mechanism.
'''
'''
#step1:-user input number
#step2:-iterate through 
print("1.a......palindrome using for loop ...only for numbers....")
number = input("Enter any number :")
indx = 0
for elem in range(len(number)):
    if number[indx] != number[
        -1 - indx]:  # here i am taking -1-i because i=0 so  now index numbers[-1] so it will  gives last element
        #   so i am comparing first index to last index element,second to second last ........
        break
    else:
        print('It is a palindrome')
        break

print("1.b .......palindrome using for loop for string.......")
strng = input("....enter sting....  =  ")
indx = 0
for char in range(len(strng)):
    if strng[indx] != strng[-1 - indx]:
        break
    else:
        print("It is palindrome")
        break
'''
print("1.c.......... generator mechanism...........")
print("1.c......palindrome.........................")
'''
2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		         10 + 11 + 12 + 13
'''
'''
num1 = int(input("enter a number = "))
num2 = int(input("enter a number = "))
list1 = [int(n1) for n1 in str(num1)]
list2=[int(n2) for n2 in str(num2)]
output=[]
final_output=[]
sum1=0
sum2=0
for indx in range(len(list1)):
    sum1=list1[indx]+list2[indx]
    output.append(sum1)
#print(output)         #[10, 11, 12, 13]
for val in range(len(output)):
    sum2=output[val]+sum2
final_output.append(sum2)
print(final_output)
'''
'''
3.3. st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba
'''
st = "ab@#cd!ef"


class Solution:
    def reverseOnlyLetters(self, S):
        if not S:
            return S
        str_ = ""
        index1 = 0
        index2 = len(S) - 1
        while index1 < len(S):
            if index2 >= 0 and S[index1].isalpha() and S[index2].isalpha():
                str_ += S[index2]
                index2 -= 1
                index1 += 1
            elif S[index1].isalpha():
                index2 -= 1
            elif not S[index1].isalpha():
                str_ += S[index1]
                index1 += 1
            else:
                index2 -= 1
                index1 += 1
        return str_


ob1 = Solution()
print(ob1.reverseOnlyLetters(st))

'''
4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
'''
'''
print("4.. findout elements duplicates count output in dict....")
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
dict = {}
for item in some_list:
    if some_list.count(item) > 1:
        dict[item] = some_list.count(item)
print(dict)
'''
'''
5.5. # t1 = (1, 2, 3, "a", "c") 
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")
'''
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lst1 = []
lst2 = []
lst = []
for elem1 in t1:
    lst1.append(elem1)
for elem2 in t2:
    lst2.append(elem2)
sum=0
indx=0
for item2 in lst2:
    if type(item2)==int:
        sum=lst1[indx]+item2
        lst.append(sum)
        indx+=1
indx2=0
sum2=0
for char1 in t1:
    if type(char1)==str:
        sum2=char1+lst2[indx2]
        lst.append(sum2)
        indx2+=1
print(lst)


'''
6  #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196
'''
print("6...............................................")
'''
step1.first import module re ie regular expression.

'''
inp = "216.08.094.196"
import re

ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)


'''
7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]
'''
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
output=[]
for item in l:
    if type(item)==list:
        print(item)