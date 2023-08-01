#str1 becomes scyatle cipher with key
def scytale(str1, key):
    new_str = ""    #sctaled string
    strlist = []
    key_count = 0
    # the number of list is key
    for k in range(key):
        strlist.append("")
    # distribute str to strlist implement
    for s in str1:
        strlist[key_count] += s
        key_count = (key_count + 1) % key
    # united string of strlist
    for strs in strlist:
        new_str += strs
    return new_str

#str1 release from scyatle cipher with key
def disscytale(str1, key):
    new_str = ""
    strlist = []
    key_count = 0
    #strlist created
    l_key = len(str1)
    if l_key % 3 == 0:
        new_key = l_key // key
    else:
        new_key = l_key // key + 1
    for k in range(new_key):
        strlist.append("")
    #distribute str to strlist implement
    for s in str1:
        strlist[key_count] += s
        key_count = (key_count + 1) % new_key
    # united string of strlist
    for strs in strlist:
        new_str += strs
    return new_str

str1 = "It's hot today."
key = 3
str1_scytale = scytale(str1,key)
print(str1_scytale)
str1_disscytale = disscytale(str1_scytale,key)
print(str1_disscytale)