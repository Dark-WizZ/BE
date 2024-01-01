import re

def extract_symbols(regex_str):
    # Use regex to find all symbols in the regular expression
    symbols = re.findall(r'[a-zA-Z*/()+-]+', regex_str)

    return symbols

# Example usage:
input_regex = "abcd*(c/b)"
output_symbols = extract_symbols(input_regex)

print(output_symbols)
