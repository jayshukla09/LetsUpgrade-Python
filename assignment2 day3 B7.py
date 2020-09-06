Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

for i in range(2,201):
    if i>1:
        for num in range(2,i):
            if (i%num)==0:
                break
        else:
            print(i)

