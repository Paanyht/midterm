def divisible_by_7(x):
    if x % 7 == 0:
        return True
    else:
        return False
   
def compare_it(x, y):
    if type(x) is not int or type(y) is not int:
        return False
    if x != y:
        return False
    if x <= 0 or y <= 0:
        return  False 
    return True
de in your function.


   
 def keyword_counter(a, b , c):
    if b == True :
        text = c
    else:
        file_name = c
        with open(file_name, "r") as f:
            text = f.read().replace("\n", " ")

    result = {}
    for kw in a :
        result[kw] = 0
        for w in text.replace('.', ' ').split(' '):
            if kw.lower() == w.lower():
                result[kw] += 1
    return result
