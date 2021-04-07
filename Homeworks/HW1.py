#Homework 1 _ Day-2

#Question 1   
#Create a List and swap the second half of the list with the first half of the list and print this list on the secreen.
liste = list(range(6))
reverseListe = liste[len(liste)//2:] + liste[:len(liste)//2]
print(reverseListe)

#Ask the user to input a single digit integer to a variable 'n'. Then, print out all of the even numbers from 0 to n (including n).
n = int(input('Please enter a single digit number: '))
while n:
    if 0<n<10:
        even = [i for i in range(n+1) if i%2==0]
	#print as a list
        print(even)
        break
    else:
        n = int(input("You entered the wrong number, please enter a single digit number:"))
	
## or print as integers
for i in even:
	print(i)
