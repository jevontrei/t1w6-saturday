text = "Coder Academy"
vowels = "aeiouAEIOU"

for each in text:
    if each in vowels:
        continue
    # can use the print function's "end" parameter from "\n" to "" to get it to print all on one line
    print(each, end="")