import re

# Name pattern: allows spaces, hyphens, and apostrophes with uppercase after apostrophe/hyphen/space
name = r"^[A-Z][a-z]*(?:[ '-][A-Z][a-z]*)*$"
name_regex = re.compile(name)

# Phone number pattern: matches 123-456-7890, (123) 456-7890, or 5555555555 (10 consecutive digits)
phone_number = r'^(\d{10}|\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
phone_regex = re.compile(phone_number)

# Email pattern: must start with a letter, then letters, numbers, dots, underscores, or hyphens
email_address = r'^[A-Za-z][\w\.-]*@[\w\.-]+\.\w{2,}$'
email_regex = re.compile(email_address)
