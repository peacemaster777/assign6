#ques1
def is_perfect_number(number):
    if number <=0:
        return False
    divisors_sum = sum(i for i in range(1,number) if number%i==0)
    if divisors_sum == number:
        print("True")
    else:
        print("False")

a = int(input())
is_perfect_number(a)