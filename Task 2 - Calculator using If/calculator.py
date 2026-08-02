# Task 2 : Calculator using if

num1 = int(input("Entre First Number :"))
num2 = int(input("Entre Second Number :"))
num3 = float(input("Entre Third Number :"))
op = input("Entre Your Op(*,/,+,-)")

print("==============================")

if op=="-,*":
    print("SUM:",num1-num2*num3)
    print("==============================")
elif op=="+,/":
    print("SUM:",int(num1/num2+num3))
    print("==============================")
elif op=="/,*,+,-":
    print("SUM:",num1/num2-num3*num1+num2)
    print("==============================")
else:
    print("INVALID OPERATION")

print("==============================")
