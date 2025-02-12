#*********************************************************************************#
# FILE: FizzBuzz Problem                                                          #
#                                                                                 #
# DESCRIPTION: This program prints each number from 1 to 100 on a new line.       #
# For each multiple of 3, print "Fizz" instead of the number.                     #
# For each multiple of 5, print "Buzz" instead of the number.                     #
# For each multiples of both 3 and 5, print "FizzBuzz" instead of the number.     #
# Otherwise, print the number.                                                    #
#                                                                                 #
# DEVELOPER: Yingqiang Yuan                                                       #
# DEVELOPER PHONE: +1 (509) 288-2111                                              #
# DEVELOPER EMAIL: yingqiang.yuan@gmail.com                                       #
#                                                                                 #
# VERSION: 1.0                                                                    #
# CREATED DATE-TIME: 20250207-11:44 Pacfic Time Zone USA                          #
#                                                                                 #
# VERSION: 1.1                                                                    #
# REVISION DATE-TIME: 20250210-14:18                                              #
# DEVELOPER MAKING CHANGE: First_name Last_name                                   #
# DEVELOPER MAKING CHANGE: PHONE: +1 (XXX) XXX-XXXX                               #
# DEVELOPER MAKING CHANGE: EMAIL: first.last@email.com                            #
#*********************************************************************************#

for i in range(1, 101):
    outputWord = ""

    if i%3==0:
        outputWord += "Fizz"
    if i%5==0:
        outputWord += "Buzz"
    if outputWord == "":
        outputWord = str(i)

    print(outputWord)
