data=input("enter your sentence here")
import string
print(string.ascii_letters)
v={
"a":0,
"e":0,
"i":0,
"o":0,
"u":0,
}
for i in data:
    if i in v:
        v[i]+=1
print(v)

alpha={}
a=string.ascii_lowercase
for i in a:
    alpha[i]=0
print(alpha)

for i in data:
    if i in alpha:
        alpha[i]+=1
pangram=False
c=0
for i in alpha:
    if alpha[i]>0:
        pangram=True
        c+=1
    else:
        pangram=False
print(c)


