https://www.codewars.com/kata/5a2be17aee1aaefe2a000151

def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


print(array_plus_array([1, 2, 3], [4, 5, 6])) 



https://www.codewars.com/kata/5ab6538b379d20ad880000ab

def area_or_perimeter(l, w):
    if l == w:
        return l * w 
    else:
        return 2 * (l + w)  


print(area_or_perimeter(4, 4))  
print(area_or_perimeter(6, 4))  



https://www.codewars.com/kata/51f2b4448cadf20ed0000386


def remove_url_anchor(url):
    return url.split('#')[0]

print(remove_url_anchor("www.example.com#about"))  



https://www.codewars.com/kata/529eef7a9194e0cbc1000255


def is_anagram(test, original):
    
    test = test.replace(" ", "").lower()
    original = original.replace(" ", "").lower()
    
    
    return sorted(test) == sorted(original)


print(is_anagram('listen', 'silent')) 
print(is_anagram('hello', 'world'))    





https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd


def mygcd(x, y):
    while y:
        x, y = y, x % y
    return x


print(mygcd(30, 45))  
print(mygcd(8, 12))  

https://www.codewars.com/kata/5842df8ccbd22792a4000245


def expanded_form(num):
    num_str = str(num)
    result = []
    
    for i, digit in enumerate(num_str):
        if digit != '0':
            result.append(digit + '0' * (len(num_str) - i - 1))
    
    return ' + '.join(result)


print(expanded_form(70304))  
print(expanded_form(9000000)) 




https://www.codewars.com/kata/57f8ff867a28db569e000c4a

def kebabize(string):
    kebabized = ''
    for char in string:
        if char.isalpha():
            if char.isupper():
                kebabized += '-' + char.lower()
            else:
                kebabized += char
    
    if kebabized and kebabized[0] == '-':
        kebabized = kebabized[1:]
    return kebabized


print(kebabize('myCamelCasedString'))  
print(kebabize('ThisIsAnotherExample'))  
