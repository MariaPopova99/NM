class A:
    def __init__(self):
        self.i=1

    def m(self):
        self.i =10
class B(A):
    def m(self):
        self.i +=1
        return self.i
def main():
    b=B()
    print(b.m())
main()

class A:
    def __init__(self):
        self.x=1
        self.__y=1
    def getY(self):
        return self.__y
    a=A()
    a.x=45
    print(a.x)
class parent:
    def __init__(self,param):
        self.v1=param
class child(parent):
    def __init__(self,param):
        self.v2=param
obj = child(11)
print('%d %d' % (obj.v2,obj.v2))

counter = 1
def foo():
    global counter
    for i in (1,2,3):
        counter+=1
foo()
print(counter)

ab = { 'Swaroop' : 'swaroop@swaroopch.com',
'Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com'
}
print(ab.get('Swaroop'))
print(ab.keys(),'\n',ab.values(),'\n', ab.items())

for i in sorted(ab):
    print(i ,':', ab[i])
for i in sorted(ab.items(),key=lambda pair:pair [1]):
    print(i)
sets = {1,2,3,3,3,5,6}
print(sets)
a,b=(1,2)
print(a,b)

s= 'А роза упала на лапу Азора'
p=(s.lower().replace(' ', ''))[::1]
s=s.lower().replace(' ', '')
if s == p:
    print('polindrom')