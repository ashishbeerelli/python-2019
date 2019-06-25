#!/usr/bin/env python
# coding: utf-8

# In[9]:


def binarysearch(a,findex,rindex,taritem):
    while findex <= rindex:
        mindex= findex+(rindex-findex)//2
        if a[mindex] == taritem:
            return mindex
        if a[mindex]>taritem:
            rindex = mindex-1
        else:
            findex=mindex+1
    return -1
list1=[1,2,4,6,7,56,87]
res=binarysearch(list1,0,6,56)
if res!= -1:
    print("item is found")
else:
    print("item not found")


# In[11]:


def sortingnum(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

    for i in range(len(a)):
        print(a[i],end=" ")
list1=[76,67,7,37,3,9]
sortingnum(list1)


# In[14]:


str ="application"
print(str)

str1='application'
print(str1)

str2=""" application test
      working
      completed
      list
      string
      phyton """
print(str2)


# In[31]:


str ="application"
print(str)
print("str[0] = ",str[0])
print("str[-1] = ",str[-1])
print("str[-5] = ",str[-5])
print("str[1:5] = ",str[1:5])
print("str[0:3] = ",str[0:3])
print("str[:5] = ",str[:5])
print("str[1:-4] = ",str[1:-4])
print("str[1:4] = ",str[1:4])
print("str[::-1] = ",str[::-1])
print("str[5:0:-1] = ",str[5:0:-1])


# In[40]:


def ispalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
print(ispalindrome("ashish"))
print(ispalindrome("maam"))


# In[33]:


n=int(input("Enter The Number"))
cnt=0
while n!=0:
    cnt=cnt+1
    n=n//10
print(cnt)


# In[ ]:


def countchars(str):
    return len(str)



s=str(input("Enter a String"))
countchars(s)


# In[43]:


def countupperletters(str):
    cnt=0
    lst = list(str)
    for x in range (len(lst)):
        if ord(lst[x])>=65 and ord(lst[x])<=90:
            cnt=cnt+1
    return cnt

print(countupperletters("HJKHJH")) 


# In[7]:


def printdigital(str):
    lst= list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            print(lst[x],end ="")
            
    return
print(printdigital("gfjegy6346"))


# In[5]:


def sumofdigits(str):
   sum=0
   lst=list(str)
   for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
               sum=sum+ord(lst[x])-48
             
   return sum
sumofdigits("gefuyjwefh345")


# In[14]:


def sumofdigitseven(str):
    sum=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            if((ord(lst[x])-48)%2==0):
                sum=sum+ord(lst[x])-48
    return sum
sumofdigitseven("sdrtge4657")


# In[ ]:




