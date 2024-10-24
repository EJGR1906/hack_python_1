"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []

    for i in range(6):
        result.append(5-i)
    #...
    return result  