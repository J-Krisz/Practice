# Return the longest strict palindrome of the string.


def palindrome(string):

    res = list()
    for i in range(len(string)):
        for j in range(0, i):
            res = string[j:i + 1]

            if res == res[::-1]:
                temp.append(res)

    return max(res, key=len)

