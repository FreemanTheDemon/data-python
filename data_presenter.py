cupcakes = open('CupcakeInvoices.csv')

for line in cupcakes:
    print(line)

cupcakes.seek(0, 0)

for line in cupcakes:
  line_list = line.rstrip('\n').split(',')
  print(line_list[2])

cupcakes.seek(0, 0)

total = 0

for line in cupcakes:
  line_list = line.rstrip('\n').split(',')
  total += float(round(float(line_list[-1]) * float(line_list[-2]), 2))
  print(round(float(line_list[-1]) * float(line_list[-2]), 2))

print(round(total), 2)

cupcakes.close()