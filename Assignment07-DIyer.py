# ------------------------------------------------- #
# Title: Assignment07
# Description: Script demonstrates how Pickling
#               and Structured error handling work
# ChangeLog: (Who, When, What)
# ChangeLog: DIyer, 2/28/2022, Created
# ChangeLog: DIyer, 3/4/2022, modified after reviewing Assignment07
# ------------------------------------------------- #

# This imports code from another code file!
import pickle

'''Pickling Demo'''

# # create the list of customers
# customer_id = int(input("Enter ID (integer): "))
# customer_name = str(input("Enter a Name (string): "))
# customer_list = [customer_id, customer_name]
# print(customer_list)
#
# # store the data with pickle.dump method
# objFile = open("AppData.dat","ab")
# pickle.dump(customer_list, objFile)
# objFile.close()
#
# # read the data back with pickle.load method
# objFile = open("AppData.dat","rb")
# objFileData = pickle.load(objFile)
# objFile.close()
# print(objFileData)

'''Error handling demo'''

# try:
#     f = open("AppsData.dat", "rb")
# except Exception as e:
#     print("There is an error with your command, try again!")
#     print("Built-in Python error info: ")
#     print(e)
#     print(type(e))
#     print(e.__doc__)
#     print(e.__str__())


''' Both at same time'''
try:
    customer_id = int(input("Enter ID (integer): "))
    customer_name = str(input("Enter a Name (string): "))
    customer_list = [customer_id, customer_name]
    print(customer_list)

except Exception as e:
    print("Please use integers for ID")
    print("Built in error info:")
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())

# store the data with pickle.dump method
    objFile = open("AppData.dat","ab")
    pickle.dump(customer_list, objFile)
    objFile.close()

  # read the data back with pickle.load method
    objFile = open("AppData.dat","rb")
    objFileData = pickle.load(objFile)
    objFile.close()
    print(objFileData)