'''
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를
출력하는 프로그램을 작성하시오.
'''
a, b = map(int, input().split())
 
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

print(gcd(a,b))
print(a*b//gcd(a,b))
