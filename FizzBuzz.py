playGame = True
print('This is FizzBuzz for the number range 1 to 100.')
print("If the number is divisible by 3, you will see 'Fizz'")
print("If the number is divisible by 5, you will see 'Buzz'")
print("If the number is divisible by both 3 and 5, you will see 'FizzBuzz'")
print('Otherwise, if none of the above is true, you will just see the number.')
print('Would you like to see this?')
print('Type 1 to See')
print('Type 2 to Quit')
print()
while playGame == True:
    userInput = input('Type 1 or 2: ')
    print()
    try:
        userInput=int(userInput)
        
        if userInput != 1 and userInput != 2:
            print ('You must enter a 1 or 2')
            continue
        elif userInput == 1:
            playGame=True
            for FB in range(1, 101):
                
                #Have to check if its divisible by both 3 and 5 first
                if FB % 3 == 0 and FB % 5 == 0:
                    print('FizzBuzz')
                    continue
                elif FB % 3 == 0:
                    print('Fizz')
                    continue
                elif FB % 5 == 0:
                    print('Buzz')
                    continue
        
                print(FB)
                playGame=False

        elif userInput == 2:
            print('Goodbye!')
            playGame == False
            break

    except ValueError:
        print('Thats not a Numerical Value, try again...')
        print()
