#usando comando Elif

age = int (input('digite sua idade: '))
if age <=4:
    price = 0
    
elif age <=18:
    price = 25
    
else:
    price = 50
print('Sua entrada é R$'+str(price)+',00')
