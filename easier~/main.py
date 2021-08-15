first = float(input())
second = float(input())
third = float(input())
forth = float(input())

sum = first+second+third+forth
average = sum/4
product = first*second*third*forth
max = max(first, second, third, forth)
min = min(first, second, third, forth)
print(f"Sum : {sum:.6f}")
print(f"Average : {average:.6f}")
print(f"Product : {product:.6f}")
print(f"MAX : {max:.6f}")
print(f"MIN : {min:.6f}")
