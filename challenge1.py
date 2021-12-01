f = open("input.txt", "r")
priorline = 0
count = 0
for x in f:
  currentline = int(x)
  if priorline == 0: 
    print("N/A - no previous measurement")
  elif currentline > priorline :
    print(f"{currentline} (increased).")
    count += 1
  else:
    print(f"{currentline} (decreased).")
  priorline = int(currentline)
print(f"The number of times a depth measurement increased was {count}.")