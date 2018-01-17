print('+------Loan Calculator------+')
borrow = int(input('Amount Borrowed (USD): '))
interest = float(input('Rate when borrowed (%): ')) * .01
term = int(input('Term (yrs): '))
print('\nYou\'ll be paying ${:,.2f}\n\r'.format((borrow*interest*term + borrow))) 
tot = borrow*interest*term + borrow
ppy = tot / term
print("Payment#\t\tAmount\t\tRem. Balance")
print("--------\t\t------\t\t------------")
for i in range(1,(term + 1)):
	bal = tot - i*ppy
	print("{0}\t\t\t${1:,.2f}\t\t   ${2:,.2f}".format(i,ppy,bal))
	
