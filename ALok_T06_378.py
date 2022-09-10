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

'''
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
final_out=[]
for item in l:
    if type(item)==list:
        output.extend(item)
    else:
        output.append(item)
for item2 in output:
    if type(item2)==list:
        final_out.extend(item2)
    else:
        final_out.append(item2)
print(final_out)

'''
8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line 
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total 
'''
lines = ["my name is alok kumar rathore \n  my empid is 378 \n i am from t06 batch "]
with open("C:\\Users\\Alok Kumar Rathore\\Desktop\\vn2_t06_378_file.txt", 'w') as fp:
    for line in lines:
        fp.write(line)
        fp.write('\n')
fp.close()


with open(r"C:\\Users\\Alok Kumar Rathore\\Desktop\\vn2_t06_378_file.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

number_of_words = 0


file1 = open("C:\\Users\\Alok Kumar Rathore\\Desktop\\vn2_t06_378_file.txt", "r")

word_count = 0
i = 0
str1 = ""
print("Contents of file " + "C:\\Users\\Alok Kumar Rathore\\Desktop\\vn2_t06_378_file.txt" + " are:")

# display and count number of  words in each line of text file
for line in file1:
    i += 1
    print(line, end='')
    words_in_line = len(line.split())
    str1 = str1 + "Words in Line No: " + str(i) + " are : " + str(words_in_line) + "\n"
    word_count += words_in_line

print('\n\n ' + str1)
print('\n\nTotal Number of  words in this file are = ' + str(word_count))

# number of characters
# and lines in a file
def counter(fname):

    # variable to store total line count
    num_lines = 0

    # variable to store total character count
    num_charc = 0

    # variable to store total space count
    num_spaces = 0
    with open("C:\\Users\\Alok Kumar Rathore\\Desktop\\vn2_t06_378_file.txt", 'r') as f:

        # loop to iterate file
        # line by line
        for line in f:
            num_lines += 1

            for letter in line:

                if (letter == ' '):

                    # incrementing the space
                    # count by 1
                    num_spaces += 1

                # loop to iterate every
                # letter character by
                # character
                for i in letter:

                    # condition to check
                    # that the encountered character
                    # is not white space and not
                    # a newline character
                    if (i != " " and i != "\n"):
                        # incrementing character
                        # count by 1
                        num_charc += 1

    # printing total line count
    print("Number of lines in text file: ",
          num_lines)

    # printing total character count
    print('Number of characters in text file: ',
          num_charc)



fileHandle = open("C:\\Users\\Alok Kumar Rathore\\Desktop\\vn2_t06_378_file.txt", "r")
tot = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for char in fileHandle.read():
    if char>='a' and char<='z':
        if char not in vowels:
            tot = tot+1
    elif char>='A' and char<='Z':
        if char not in vowels:
            tot = tot+1
print("\nThere are " + str(tot) + " Consonants available in the File")


# Python program to count number of vowels,
# newlines and character in textfile


# Opening the file in read mode
txt_file = open("C:\\Users\\Alok Kumar Rathore\\Desktop\\vn2_t06_378_file.txt", "r")

# Initialize three variables to count number of vowels,
# lines and characters respectively
vowel = 0
line = 0
character = 0

# Make a vowels list so that we can
# check whether the character is vowel or not
vowels_list = ['a', 'e', 'i', 'o', 'u',
                   'A', 'E', 'I', 'O', 'U']

# Iterate over the characters present in file
for alpha in txt_file.read():

# Checking if the current character is vowel or not
    if alpha in vowels_list:
        vowel += 1

        # Checking if the current character is
        # not vowel or new line character
    elif alpha not in vowels_list and alpha != "\n":
        character += 1

# Checking if the current character
# is new line character or not
    elif alpha == "\n":
        line += 1

# Print the desired output on the console.
print("Number of vowels in ", " ", " = ", vowel)

