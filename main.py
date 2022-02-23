# Code by 6icada
# Please do not copy code

# Calculate function
def Calculate(firstSide, secondSide):
    if int(firstSide) - int(secondSide) <= 0:
        # Adding vars
        intLowest = int(secondSide) - int(firstSide) + 1
        intHighest = int(firstSide) + int(secondSide) - 1
        stringLowest = str(intLowest)
        stringHighest = str(intHighest)

        # Output
        if intLowest == intHighest:
            print(f'-- : {intLowest} : --\n')
        else:
            print(f'{stringLowest} : {stringHighest}\n')
    else:
        # Adding vars
        intLowest = int(firstSide) - int(secondSide) + 1
        intHighest = int(firstSide) + int(secondSide) - 1
        stringLowest = str(intLowest)
        stringHighest = str(intHighest)

        # Output
        if intLowest == intHighest:
            print(f'-- : {intLowest} : --\n')
        else:
            print(f'{stringLowest} : {stringHighest}\n')

# Adding vars
firstSide = input('Enter first side: ')
secondSide = input('Enter second side: ')

Calculate(firstSide, secondSide)
