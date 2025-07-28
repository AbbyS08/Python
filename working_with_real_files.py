#Sales Totals Processing

def main():
    try:
        # Opening sales_totals.txt
        file = open("8/sales_totals.txt", "rt")
        # Initializing counters
        total = 0
        line_count = 0
        # Reading the lines in the file
        line_list = file.readlines()
        # Processing each line in a loop
        for line in line_list:
            # Changing the line to a float
            line = float(line)
            # Printing each line
            print(f"{line:.2f}", end=" ")
            # Adding to counters
            total += line
            line_count += 1
        # Closing the file
        file.close()
        # Calculating the average of the numbers
        average = total/line_count
        # Printing total, line count, and average
        print(f"\nTotal: {total:.2f}\nNumber of Entries: {line_count}\nAverage: {average:.2f}")
    # Error Messages
    except FileNotFoundError:
        print("The file couldn't be found.")
    except ValueError:
        print("The line couldn't be converted into a float.")
    except ZeroDivisionError:
        print("The line count is equal to zero.")
    except:
        print("Something went wrong.")
        

main()