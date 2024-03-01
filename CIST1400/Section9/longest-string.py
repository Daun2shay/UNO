def compare_strings(string1, string2):

 if len(string1) > len(string2):
   return f"{string1} is longer than {string2}"
 elif len(string1) < len(string2):
   return f"{string2} is longer than {string1}"
 else:
   return f"{string1} and {string2} are the same length"


string1 = input()
string2 = input()
print(compare_strings(string1, string2))
