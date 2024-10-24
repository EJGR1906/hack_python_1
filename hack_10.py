"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"

    
    #...
    return list(result.replace("o", "0").replace("i", "1").replace("a", "@").upper())

print(fn_hack_10()) # ['f', '00', 'z', '1', 'm', '@', 'n']