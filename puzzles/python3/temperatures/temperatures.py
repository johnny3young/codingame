# the number of temperatures to analyse
n = int(input())
min_temperature = 5526
for i in input().split():
    temperature = int(i)
    if abs(temperature) < abs(min_temperature) or abs(temperature) == abs(min_temperature) and temperature > min_temperature:
        min_temperature = temperature

print(0 if n == 0 else min_temperature)
