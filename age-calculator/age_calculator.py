from datetime import datetime, date

def calculate_age(birthdate):
    today = date.today()
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    if age_days < 0:
        age_months -= 1
        age_days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

def days_until_birthday(birthdate):
    today = date.today()
    next_birthday = date(today.year, birthdate.month, birthdate.day)
    if today > next_birthday:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)
    return (next_birthday - today).days

def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(dob_input, "%Y-%m-%d").date()
        years, months, days = calculate_age(birthdate)
        days_left = days_until_birthday(birthdate)

        print(f"\n🎉 You are {years} years, {months} months, and {days} days old.")
        print(f"📅 Days until your next birthday: {days_left} days")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
