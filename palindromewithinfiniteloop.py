def checkpalindrome( ):
	var=1
	while var==1:
			ask = input("Check Palindrome/Not :  ")
			print(ask[::-1])
			if ask[::] == ask[::-1]:
				print ("Palindrome")
			else:
				print ("Not Palindrome")
	print("Good Bye")

checkpalindrome( )

						
