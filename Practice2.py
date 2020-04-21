""" Problem Statement: An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case """

#my Solution
""" def is_isogram(string):
    b=[]
    if len(string) == 0:
        c = "true"
    else:
        for i in string.lower():
            b.append(i)
            b.sort()
            for j in range(0,len(b)-1):
                if b[j] == b[j+1]:
                    c = "false"
                    break
                else:
                    c = "true"    
    return c     """

#Solution 1
""" def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True    
 """
#Solution 2
""" def is_isogram(string): 
    return len(set(string.lower())) == len(string) """

#Solution 3
is_isogram = lambda s: len(set(s.lower())) == len(s)

print(is_isogram("Dermatoglyphics"))