# Your first task is to determine if the given sequence of characters is a valid barcode or not.
# Each line must not contain anything else but a valid barcode. A barcode is valid when:
#     • Is surrounded with a "@" followed by one or more "#"
#     • Is at least 6  characters long (without the surrounding "@" or "#")
#     • Starts with a capital letter
#     • Contains only letters (lower and upper case) and digits
#     • Ends with a capital letter
# Next you have to determine the product group of the item from the barcode.
# The product group is obtained by concatenating all the digits found in the barcode.
# If there are no digits present in the barcode, the default product group is "00".

import re
n = int(input())
valid_barcodes = []
pattern = r"@#+[A-Z][a-z0-9A-Z]{4,}[A-Z]@#+"
for i in range(n):
    barcode = input()
    match = re.findall(pattern,barcode)
    barcode = ""
    if match:
        for i in str(match):
            if i.isdigit():
                barcode += i
        if barcode == "":
            barcode = "00"
        print(f"Product group: {barcode}")
    else:
        print("Invalid barcode")