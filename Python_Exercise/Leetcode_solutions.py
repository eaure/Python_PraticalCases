# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# def romantointeger(s):
# 	num = 0
# 	dict1 = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#     for i in range(0,len(s)+1):
#     	if d[s[i]] < d[s[i+1]]:
#     		num - = d[s[i]]
#     	num += d[s[i]]
#     return num

# Stack-Baseball Game

# 不知道和栈有什么关系。。这不是列表问题吗。。
def baseball_game(data):
    sum=0
    resultlist = []
    for i in data:
        if i == "+":
            resultlist.append(resultlist[-1]+resultlist[-2])
        elif i == "D":
            resultlist.append(2*resultlist[-1])
        elif i == "C":
            del resultlist[-1]
        else:
            resultlist.append(int(i))
    for a in resultlist:
        sum += a 
    return sum

print(baseball_game(["5","2","C","D","+"]))


