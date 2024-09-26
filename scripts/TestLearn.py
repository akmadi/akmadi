import re

# import numpy as np

# array1 = [10,20,30,40]

# array2 = [2,2,2,2]

# np_arr1 = np.array(array1)

# np_arr2 = np.array(array2)

# fract = np_arr1 / np_arr2

# print(fract[fract > 6])


l = [2,4,7,3,14,19]

# for i in l :
#     if (i % 2 == 0):
#         result =  True
#     else:
#         result = False
#     print(result)

# for i in l:
#     result = lambda x : x % 2 == 0
#     print(result(i))


# def methodargTest(first,second,third,*args):
#     print(first)
#     print(second)
#     print(third)
#     print(args)

# methodargTest(1,2,3,4,5,6,7)

# def methodPass(first,second,**args):
#     if args.get("action") == 'sample':
#         print('Print sum value %d'%(first+second))
#     if args.get("test") == "second":
#         return second
 
# result = methodPass(1,2,action="sample",test="second")  

# print(result)


def test_email(your_pattern):
    pattern = re.compile(r".*?@example.com|.*?@python.org|.*?@email.com")
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

pattern = r".*?@example.com|.*?@python.org|.*?@email.com" # Your pattern here!
test_email(pattern)



