import re


str = '3 товара по цене 200.99'
pat = r'\d+.\d'
match = re.search(pat, str)
print(match.group())