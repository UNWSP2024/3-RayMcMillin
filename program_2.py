# Ray McMillin, 2/7/25, Age Classifier

def categorize_age(age):

    if age <= 1:
        return 'Infant'
    if age > 1 and age < 13:
        return 'Child'
    if age >= 13 and age < 20:
        return 'Teenager'
    if age >= 20:
        return 'Adult'
    return ageCategory

if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)
