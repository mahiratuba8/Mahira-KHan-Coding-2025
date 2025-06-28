largest=int(input('Enter a bigger number: '))
smallest=int(input('Enter a smaller number: '))

while(smallest):
    num_store=smallest
    smallest=largest%smallest
    largest=num_store
print('HCF is: ', largest)
