class A:
    pass

class B(A):
    pass

a = A()
b = B()
print(isinstance(a, A))
print(isinstance(b, B))

#모든 자식은 부모 타입, b는 본인의 타입인 B이면서 부모타입이다.
print(isinstance(b, A))
#부모는 절대 자식타입이 될 수 없다.
print(isinstance(a, B))
