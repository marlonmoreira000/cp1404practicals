"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# state_code = input("Enter short state: ")
# state_code_formatted = state_code.upper()
#
# while state_code != "":
#     if state_code_formatted in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code_formatted])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ")
#     state_code_formatted = state_code.upper()

    ################################################################

for key in CODE_TO_NAME:
    print("{:3} in {}".format(key, CODE_TO_NAME[key]))


