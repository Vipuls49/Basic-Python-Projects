#get user email address
email=input("What is your email address ?").strip()
#slice out user name
user_name=email[:email.index('@')]
print(user_name)
#slice domain name
domain=email[email.index('@')+1:]
print(domain)
#format message
output="Your username is {} and your domain name is {}".format(user_name,domain)
#display output message
print(output)