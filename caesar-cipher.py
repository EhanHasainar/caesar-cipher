letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



again = True

while again is True:
  crypt = input("Want to 'encrypt' or 'decrypt': ").lower()
  print()

  msg = input('Type your message: ').lower().strip()
  msg = msg.replace(" ", "")
  print()

  shiftno = int(input('Shift Number: '))
  print()

  receive = str()

  if crypt == 'encrypt':
    for i in msg:
      receive = receive + letters[(letters.index(i)+shiftno)%26]

  elif crypt == 'decrypt':
    for i in msg:
      receive = receive + letters[(letters.index(i)-shiftno)%26]
  else:
    print("Sorry didn't get that")
  print(receive)
  print()
  ask = str(input("Type 'yes' to continue and 'no' to stop: "))
  print()
  if ask == 'yes':
    again = True
  elif ask == 'no':
    again = False
  else:
    print("Sorry didn't get that")
    print()
    again = False

