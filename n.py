def max_distinct_char(str1, n):
    count = [0] * 256
    for i in range(n):
        count[ord(str1[i])] += 1
    max_distinct = 0
    for i in range(256): 
        if (count[i] != 0): 
            max_distinct += 1    
    return max_distinct 
def smallestSubstr(str1): 
  n = len(str1)     
  max_distinct = max_distinct_char(str1, n) 
  minl = n   
  for i in range(n):
      for j in range(n):
          sub = str1[i:j] 
          substr_length = len(sub) 
          sub_distinct_char=max_distinct_char(sub,substr_length) 
          if (substr_length < minl and max_distinct == sub_distinct_char):
              minl = substr_length 
  return minl 
str1 = input()
length=smallestSubstr(str1); 
print(length)   
  
