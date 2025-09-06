# Accept the inputs 
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

# Convert the rate to a decimal number 
rate = rate / 100 

# Initialize the accumulator for the interest 
totalInterest = 0.0 

# Display the header for the table 
print("%4s%18s%10s%16s" % \
      ("Year", "Starting balance",
       "Interest", "Ending balance"))

# Compute and display the results for each year 
for year in range(1, years + 1): 
   interest = startBalance * rate
   endBalance = startBalance + interest
   print("%4d%18.2f%10.2f%16.2f" % \
        (year, startBalance, interest, endBalance))
   startBalance = endBalance
   totalInterest += interest 
   