import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
x=input("Довжина")
y=input("Ширина")
x1=float(x)*0.1
y1=float(y)*0.1
x2=float(x)*0.01
y2=float(y)*0.01
s1=x1*y1
s2=x2*y2
print(s1,"ар")
print(s2,"Га")
printTimeStamp("Олійник")