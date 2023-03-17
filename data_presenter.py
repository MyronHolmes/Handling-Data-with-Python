
def multiply(num1, num2):
    x = float(num1) 
    y = float(num2)
    product = x * y
    return product


def multiply_challenge(num1, num2):
    x = float(num1) 
    y = float(num2)
    product = x * y
    return int(product)


open_file = open('CupcakeInvoices.csv')

for line in open_file:
    line = line.strip()
    value = line.split(',')
    print(value)
    

open_file.seek(0)
for line in open_file:
    line = line.strip()
    value = line.split(',')
    print(value[2])


open_file.seek(0)
for line in open_file:
    line = line.strip()
    value = line.split(',')
    print(multiply(value[3], value[4]))


open_file.seek(0)
total_sum = 0
for line in open_file:
    line = line.strip()
    value = line.split(',')
    total_sum += multiply(value[3], value[4])
print(total_sum)    


open_file.seek(0)

    
int_total_sum = 0
for line in open_file:
    line = line.strip()
    value = line.split(',')
    int_total_sum += multiply_challenge(value[3], value[4])
print(int_total_sum)    

open_file.close()

