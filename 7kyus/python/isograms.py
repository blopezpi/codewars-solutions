def is_isogram(string):
    result = [ False for i in string.lower() if string.lower().count(i) > 1 ]
    return True if not result else False  
