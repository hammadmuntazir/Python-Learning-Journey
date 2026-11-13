import re

email = input('Enter email: ')

email_condition = r'^[a-z]+[._]?[a-z0-9]+@\w+\.[a-z]{2,3}$'

if re.search(email_condition, email):
    print('Valid email')
else:
    print('Invalid email')
