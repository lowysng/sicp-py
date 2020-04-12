# 1.7.5 Recursion Example: Partitions
"""
The number of partitions of a positive integer  n,
using parts up to size  m, is the number of ways
in which  n  can be expressed as the sum of positive 
integer parts up to  m  in increasing order. 

The number of ways to partition  n  using integers
up to  m  equals
- the number of ways to partition  n - m  using
  integers up to  m, and 
- the number of ways to partition  n  using 
  integers up to  m - 1

Base case:
- There is one way to partition 0: include no parts
- There are 0 ways to partition a negative n
- There are 0 ways to partition any  n  greater than 0 using 
  parts of size 0 or less
"""
def count_partition(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partition(n-m, m) + count_partition(n, m-1)

