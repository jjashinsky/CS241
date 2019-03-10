# Prompts the user for a postive value
# and returns the postive number.    
def prompt_number():
        number = int(input("Enter a positive number: "))
        # will continue untill a positive number is recognized.
        while number < 0:
            print("Invalid entry. The number must be positive.")
            number = int(input("Enter a positive number: "))
        return number

# Takes in a list of numbers and returns the sum
def compute_sum(list):
        return sum(list)

# Uses prompt_number() and compute_sum().
# Prompts the user 3 times for a postive number
# and returns the sum.
def main():
    count = 0
    users_list = []
    for i in range(3):
        number = prompt_number()
        print("")
        users_list.append(number)
    sum_list = compute_sum(users_list)
    print("The sum is: {}" .format(sum_list))

    
if __name__=="__main__":
    main()