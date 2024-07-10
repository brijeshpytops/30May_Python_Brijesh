# single in heritance
# class A:
#     def feature1(self):
#         print("feature 1 working")

# class B(A):
#     def feature2(self):
#         print("feature 2 working")

# obj = B()
# # print(dir(obj))
# obj.feature2()
# obj.feature1()

# multi-level inheritance
# class A:
#     def feature1(self):
#         print("feature 1 working")

# class B(A):
#     def feature2(self):
#         print("feature 2 working")

# class C(B):
#     def feature3(self):
#         print("feature 3 working")

# class D(C):
#     def feature4(self):
#         print("feature 4 working")

# obj = D()
# # print(dir(obj))
# obj.feature4()
# obj.feature3()
# obj.feature2()
# obj.feature1()

# multiple inheritance
# class A:
#     def feature1(self):
#         print("feature 1 working")

# class B:
#     def feature2(self):
#         print("feature 2 working")

# class C(A, B):
#     def feature3(self):
#         print("feature 3 working")

# obj = C()
# obj.feature1()
# obj.feature2()
# obj.feature3()

# herachical inheritance
class A:
    def feature1(self):
        print("feature 1 working")

class Al(A):
    def feature2(self):
        print("feature 2 working")

class All:
    def featureall(self):
        print("feature all working")

class Alm:
    def featurealm(self):
        print("feature alm working")

class Alr(Al):
    def featurealr(self):
        print("feature alr working")

class Ar:
    def feature3(self):
        print("feature 3 working")
    
obj = Alr()
print(Alr.mro())
# print(dir(obj))