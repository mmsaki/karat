# Antony: anthony@morganlatimer.com

# Solution by  Meek Msaki
# MyDiscord -> #Meek6464
# My github -> github.com/mmsaki

# O(n2)
def min_distance1(s, c):
    ans = []
    curr = [i for i, x in enumerate(s) if x == c]

    for i, v in enumerate(s):
        min_dis = []
        for j in curr:
            min_dis.append(abs(j - i))

        ans.append(min(min_dis))

    return ans


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


s1 = "ilovetocode"
c1 = 'c'
o1 = [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3]

s2 = "lool"
c2 = 'l'
o2 = [0, 1, 1, 0]

s3 = 'www'
c3 = 'w'
o3 = [0, 0, 0]


s4 = "whatitdo"
c4 = "a"
o4 = [2, 1, 0, 1, 2, 3, 4, 5]

s5 = "windows"
c5 = "w"
o5 = [0, 1, 2, 2, 1, 0, 1]

s6 = 'redisthebest'
c6 = 'e'
o6 = [1, 0, 1, 2, 3, 2, 1, 0, 1, 0, 1, 2]

s7 = 'givemejob'
c7 = 'g'
o7 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

s8 = "zahir"
c8 = "z"
o8 = [0, 1, 2, 3, 4]

s9 = "zahirz"
c9 = "z"
o9 = [0, 1, 2, 2, 1, 0]

s10 = "letsgetit"
c10 = "t"
o10 = [2, 1, 0, 1, 2, 1, 0, 1, 0]


print(
    f"""
1.  {[7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3]}      == {min_distance(s1, c1) == o1}    {o1 }
2.  {[0, 1, 1, 0]}                           == {min_distance(s2, c2) == o2}    {o2 }
3.  {[0, 0, 0]}                              == {min_distance(s3, c3) == o3}    {o3 }
4.  {[2, 1, 0, 1, 2, 3, 4, 5]}               == {min_distance(s4, c4) == o4}    {o4 }
5.  {[0, 1, 2, 2, 1, 0, 1]}                  == {min_distance(s5, c5) == o5}    {o5 }
6.  {[1, 0, 1, 2, 3, 2, 1, 0, 1, 0, 1, 2]}   == {min_distance(s6, c6) == o6}    {o6 }
7.  {[0, 1, 2, 3, 4, 5, 6, 7, 8]}            == {min_distance(s7, c7) == o7}    {o7 }
8.  {[0, 1, 2, 3, 4]}                        == {min_distance(s8, c8) == o8}    {o8 }
9.  {[0, 1, 2, 2, 1, 0]}                     == {min_distance(s9, c9) == o9}    {o9 }
10. {[2, 1, 0, 1, 2, 1, 0, 1, 0]}            == {min_distance(s10, c10) == o10}    {o10}
""")
