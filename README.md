# karat-july-12 zoom

1. create function that returns the minimum distance between character

```py
def min_distance(string, character):
  # start here
  return
```

# Solution

1. Run solution

   ```sh
   python 01.py
   ```

1. O(n^2)

   ```py
   # O(n^2)
   def min_distance1(s, c):
    ans = []
    curr = [i for i, x in enumerate(s) if x == c]

    for i, v in enumerate(s):
        min_dis = []
        for j in curr:
            min_dis.append(abs(j - i))

        ans.append(min(min_dis))

    return ans
   ```

1. O(n)

   ```py
   # O(n)
   def min_distance(s, c):
    ans = []
    prev = cur = s.index(c)

    for i, v in enumerate(s):
        try:
            cur = s[i:].index(c) + i
        except:
            prev = cur

        if v == c:
            ans.append(0)
        else:
            ans.append(min(abs(cur - i), abs(prev - i)))
    return ans
   ```
