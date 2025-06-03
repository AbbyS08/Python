# 99 Bottles of Beer on the Wall song
# Setting the original amount of bottles to 99
bottles = 99
# The loop will stop when the number of bottles is 0
while bottles > 0:
    # Printing the lyrics for bottles 99 to 3
    if bottles > 2:
        print(f"{bottles} bottles of beer on the wall \n{bottles} bottles of beer \nTake one down, pass it around \n{bottles - 1} bottles of beer on the wall!")
    # Bottles 2 and 1 are printed separately because the lyrics change
    elif bottles == 2:
        print(f"{bottles} bottles of beer on the wall \n{bottles} bottles of beer \nTake one down, pass it around \n{bottles - 1} bottle of beer on the wall!")
    elif bottles == 1:
        print(f"{bottles} bottle of beer on the wall \n{bottles} bottle of beer \nTake it down, pass it around \nNo bottles of beer on the wall!")
    # Decreasing the number of bottles by one for each time the loop ends
    bottles -= 1
