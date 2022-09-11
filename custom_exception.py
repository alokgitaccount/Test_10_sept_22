# 1.
print("1. .....example of custom exception .....")


class AgeError(Exception):
    def __init__(self, message):
        self.message = message


class NegAgeEror(Exception):
    def __init__(self, message):
        self.message = message


try:
    age = int(input("enter age = "))
    if age < 0:
        raise NegAgeEror("please dont enter any negative number ")
    if age < 18:
        raise AgeError("not eligible")
    if age >= 18:
        print("you are eligible fo vote .....")


except AgeError as ager:
    print("exception", ager)

except NegAgeEror as ne:
    print("exception", ne)
except ValueError as ve:
    print("please dont enter any alphabets ")

except Exception as es:
    print("exception ", es)

# 2.
print("2....example of custom exception.....")


class NameEror(Exception):
    def __init__(self, name):
        pass
        # self.name = name


try:
    name = input("enter name= ")
    if name.isalpha() == False:
        print("true")
        raise NameEror("dont enter any special symbol and any numeric digit")

except NameEror as ner:
    print("exception", ner)
except TypeError:
    print("dont enter numeric digit any special symbol")
except ValueError:
    print("dont enter any special symbol")
else:
    print("name is ", name)
finally:
    print("program completed successfully")

print("3.....example of custom exception.....")


class SpecialCharError(Exception):
    def __init__(self, message):
        self.message = message


class NumberError(Exception):
    def __init__(self, message):
        self.message = message


try:
    user_input = input("enter your password...= ")
    count_spcl_char = 0
    count_digit = 0
    # for char in user_input:
    #    if char.isdigit() == True:
    #        #if int(char) < 0:
    #            print(char)

    for char in user_input:
        if char.isalnum() == False and char.isspace() == False:
            count_spcl_char += 1  # input alok@123#$
    if count_spcl_char <= 1:  # output @ # $
        raise SpecialCharError("please enter atlest 2 special character")
    for char in user_input:
        if char.isdigit():
            count_digit += 1
    if count_digit <= 1:
        raise NumberError("please enter atleast 2 digit....")



except SpecialCharError as ser:
    print("exception", ser)
except NumberError as ner:
    print("exception", ner)
except Exception as es:                # Exception is super class , super class method always last other wise first super class exception
                                         # will print then there is no use of other excpetion
    print("exception", es)
else:
    print("\n...............password created successfully...............")
    print("your password is :", user_input)
