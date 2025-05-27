# simple_interest.py

print("💰 Simple Interest Calculator 💰")

# Taking inputs
try:
    principal = float(input("Enter the Principal amount (P): ₹ "))
    rate = float(input("Enter the Rate of Interest (R%): "))
    time = float(input("Enter the Time period in years (T): "))

    # Calculate Simple Interest
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print(f"\n✅ Simple Interest: ₹ {simple_interest:.2f}")
    print(f"💵 Total Amount after {time} years: ₹ {total_amount:.2f}")

except ValueError:
    print("❌ Please enter valid numeric inputs only.")
