num1 = input("Input number: ");
num1 = int(num1);

num2 = input("Input another number: ");
num2 = int(num2);

small = min(num1,num2);
large = max(num1,num2);

for i in range(small, large):
	print(i);