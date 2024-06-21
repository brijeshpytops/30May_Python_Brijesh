def user_forgot():
    email = input("Enter your email: ")
    import random
    otp = random.randint(111111, 999999)
    return email, otp