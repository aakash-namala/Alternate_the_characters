#program to alternate the characters

print('Enter two strings of same length')
string1=input('Enter the first string1:')
string2=input('Enter the first string2:')
if(len(string1))==(len(string2)):
    for i in range(len(string1)):
        print(string1[i]+string2[i],end='')
else:
    print('PLease enter the strings,which are having same length')
