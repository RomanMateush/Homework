a=int(input())
b=int(input())
if b%a==0 or a%b==0:
    print("YES")
elif a==0 or b==0:
    print("YES")
elif a==0 and b==0:
    print("YES")
else:
    print("NO")
