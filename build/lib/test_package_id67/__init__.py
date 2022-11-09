## a basic method
  
def count_in_list(l, word):
  count = 0
  for element in l:
     if element==word:
         count += 1
  return count
  
from .Dogs import Dog
