divisorNum = int(input())
divisors = list(map(int, input().split()))

num_of_guess = 1
base = 1

for num in divisors:
    base *= num

while (base * num_of_guess) <= 1000 and (base * num_of_guess) >=1:
    num_of_guess += 1

print(num_of_guess-1)