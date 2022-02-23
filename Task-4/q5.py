rows = int(input("Enter no.of Rows = "))



for s in range(rows - 1, -1, -1):
   for t in range(0, s):
         print(end = ' ')
   for g in range(s, rows):
         print('*', end = ' ')
   print()
