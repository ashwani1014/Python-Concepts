class A:
    label="A : Base class"

class B(A):
    label="B : Base class"
    
class C(B):
     label="C : Base class"

class D(B,A):
    pass   


c=D()
print(c.label)