# Input monthly salary
salary = float(input("Enter your monthly salary: "))
# Input requested loan amount
loan = float(input("Enter the total loan amount: "))

# Check salary eligibility
if salary >= 30000:
    print("Check loan amount eligibility")
    
    # Check loan amount eligibility
    if loan <= 10 * salary:
        # Input number of months for repayment
        months = float(input("Enter total months to repay: "))
        
        # Calculate total amount with interest
        total_amount = loan * 1.10  # Adding 10% interest
        
        # Display approval message
        print(f"Approved! Total amount to repay (including interest): {total_amount:.2f}")
    else:
        print("Not eligible: loan amount too high")
else:
    print("Not eligible: salary too low")

        
   