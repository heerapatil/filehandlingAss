#9. Write a Python program to count the frequency of words in a file. 

from collections import Counter
with open("text.txt") as f:
    print Counter(f.read().split())
    
    
'''OUTPUT:
Counter({'\\n': 10, 'dfsdf': 2, '\\n,': 1, 'people': 1, 'fsdfgsdhf': 1, 'dfsdfs': 1, 'hi': 1, 'dfsdfsdf': 1, 'are': 1, 'how': 1, 'you': 1, 'hello': 1, 'dfsfksdf': 1})
'''
    
