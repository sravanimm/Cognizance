while True:
  p = input("Number:")
  a=p[::-1]
  if p==a:
    print(True)
  else:
    print(False)
  i=input("Do you want to check one more time(y/n)?")
  if i=='y':
        True
  if i=='n':
        break
