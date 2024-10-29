number = int(input("Enter a number from the list: (1: Maths, 2: English, 3: Science) "))
match number:
  case 1:
      print("Maths")
  case 2:
      print("English")
  case 3:
      print("Science")
  case other:
      print("Error!")