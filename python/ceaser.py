# argument0 str1 is ceasered by key that is argument1 'key'
def ceaser(str1, key):
    new_str = ""
    if key >= -26 and key <= 26:
        for s in str1:
            s_ascii = ord(s)    #s_ascii is asciied s
            # if capital number
            if s_ascii >=ord('A') and s_ascii <= ord('Z'):
                s_new_ascii = s_ascii + key #ceasered
                #adjust number in range of capital number
                if s_new_ascii > ord('Z'):
                    s_new_ascii -= 26
                elif s_new_ascii < ord('A'):
                    s_new_ascii += 26
            # if lower number
            elif s_ascii >=ord('a') and s_ascii <= ord('z'):
                s_new_ascii = s_ascii + key #ceasered
                #adjust number in range of lower number
                if s_new_ascii > ord('z'):
                    s_new_ascii -= 26
                elif s_new_ascii < ord('a'):
                    s_new_ascii += 26
            else:
                s_new_ascii = s_ascii 
            new_s = chr(s_new_ascii)
            new_str += new_s
    else:
        print("argument 1 is out of range or not a number!")
    return new_str

#argument 0 (ceasered str1) become disceasered with key (argument 1) 
def disceaser(str1, key):
    new_str = ""
    if key >= -26 and key <= 26:
        for s in str1:
            s_ascii = ord(s)    #s_ascii is asciied s
            # if capital number
            if s_ascii >=ord('A') and s_ascii <= ord('Z'):
                s_new_ascii = s_ascii - key #ceasered
                #adjust number in range of capital number
                if s_new_ascii > ord('Z'):
                    s_new_ascii -= 26
                elif s_new_ascii < ord('A'):
                    s_new_ascii += 26
            # if lower number
            elif s_ascii >=ord('a') and s_ascii <= ord('z'):
                s_new_ascii = s_ascii - key #ceasered
                #adjust number in range of lower number
                if s_new_ascii > ord('z'):
                    s_new_ascii -= 26
                elif s_new_ascii < ord('a'):
                    s_new_ascii += 26
            else:
                s_new_ascii = s_ascii 
            new_s = chr(s_new_ascii)
            new_str += new_s
    else:
        print("argument 1 is out of range or not a number!")
    return new_str

str1 = "it's hot today"
key = 3
str1_ceaser = ceaser(str1,key)
print(str1_ceaser)
str1_disceaser = disceaser(str1_ceaser,key)
print(str1_disceaser)