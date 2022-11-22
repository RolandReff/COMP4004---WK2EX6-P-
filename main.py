if __name__ == "__main__":
  weight = int(input('Enter weight (g):'))
  lenght = int(input('Enter height (cm):'))
  diameter = int(input('Enter diameter (cm):'))

  if (weight <= 2000 and lenght <= 90 and diameter <= 7):
   print('Yes')
  else:
   print('No')
