# var = input("Enter a string value")

# if var == var[::-1]:
#     print('True')
# else:
#     print('False')

# dict = {
#     "name": "student1",
#     "class": "Grade2",
#     "Age": 7
# }

# for k,v in dict.items():
#     print("%s : %s"%(k,dict.get(k)))

# list = [1,2,3,4,5]

# x = 4

# if 3 < x < 5:
#     print(x)

# x = 'This is a test string'

# print(" ".join([k.capitalize() for k in x.split()]))

# number = 123
# print(f"{number}")


# test = ["sample","list","sample"]

# list2 = [1,2,3,4,5,6]

# test.append('Fourth')

# #test.extend(list2)

# #test.remove('Fourth')

# #print(test.index(6))
# print(test)

# print(sorted(list2))

# sample = test.copy()

# print(sample)


# def cubeOfaNum(num:int) -> int:
#     return num ** 3

# try:
#     num = int(input('Enter a number: \n'))
#     print(cubeOfaNum(num))
# except Exception:
#     print('Not a number')
# finally:
#     print('method complete')

def monthName(shortName:str, MonthsDict:dict):
    return MonthsDict.get(shortName.capitalize())
    


monthNames = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}


print(monthName('mar',monthNames))