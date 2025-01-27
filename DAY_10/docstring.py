def format_name(first_name_, last_name_):
    """ Take the first and last name of a person and then return the title case version."""
    if first_name_ == "" and last_name_ == "":
        print("Please enter your first name and last name")
        return
    first_name_ = first_name_.title()
    last_name_ = last_name_.title()
    return first_name_ + " " + last_name_


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your name is",format_name(first_name, last_name))
