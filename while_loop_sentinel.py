total_sum = 0
while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
        continue  # Continue asking for input if it's invalid

# After the loop ends, print the total sum
print("The total sum is:", total_sum)
