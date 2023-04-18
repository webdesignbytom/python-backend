## Break email addresses into parts

## Collect email
## slice and split input
## save first part as user name
## middle saved as domain

def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Enter your email address: ")

    (username, domain) = email_input.split("@")

    (domain, extension)= domain.split(".")

    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)


while True:
    main()