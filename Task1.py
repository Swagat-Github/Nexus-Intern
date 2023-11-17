## 1. Write a python function that accepts a string and calculates the number of upper case letters and lower case letters


def Occurence_of_upper_lower(string):
  Lwc = 0
  Upc = 0
  for char in string:
    if char.isalpha():
      if char.islower():
        Lwc += 1
      elif char.isupper():
        Upc += 1
  print("Occurence of Lowercase Characters:", Lwc)
  print("Occurence of Uppercase Characters:", Upc)


Input_string = input(
    "Enter a string to calculate the uppercase and lowercase characters:")
Occurence_of_upper_lower(Input_string)
