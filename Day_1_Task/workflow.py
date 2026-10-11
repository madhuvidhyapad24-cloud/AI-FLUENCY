
print("=" * 50)
print("       RULE-BASED WORKFLOW")
print("       Course Fee Assistant")
print("=" * 50)

# Fixed course fee data
fees = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

# Step 1: Display all course fees
print("\nSTEP 1: Course Fees")

for course, fee in fees.items():
    print(f"{course}: Rs. {fee}")

# Step 2: Check a fixed course
print("\nSTEP 2: Fee Lookup")

course = "CS101"
print(f"Fee for {course}: Rs. {fees[course]}")

# Step 3: Check the budget using fixed rules
print("\nSTEP 3: Budget Check")

budget = 15000
fee = fees["CS101"]

if fee <= budget:
    print(f"{course} is within the budget of Rs. {budget}.")
else:
    print(f"{course} exceeds the budget of Rs. {budget}.")

# Step 4: Calculate a fixed combination
print("\nSTEP 4: Total Fee Calculation")

total = fees["CS101"] + fees["AI202"]
print(f"CS101 + AI202 = Rs. {total}")

# Step 5: Compare against another fixed budget
print("\nSTEP 5: Final Budget Decision")

budget = 30000

if total <= budget:
    print(f"Total Rs. {total} is within the budget of Rs. {budget}.")
else:
    print(f"Total Rs. {total} exceeds the budget of Rs. {budget}.")

print("\nWorkflow completed successfully.")
