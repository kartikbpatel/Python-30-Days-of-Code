t = int(input())
for i in range(0,t):
    s = input()
    left=''
    right=''
    for j in range(0,len(s)):
        if(j%2==0):
            left+=s[j]
        else:
            right+=s[j]
    print (left,right)