#task1
f = open("input.txt", "r")
forward_total = 0
depth = 0
for x in f:
  currentline = x.strip()
  if (currentline.find('forward') != -1): 
    forward_total += int(currentline[-1])
  if (currentline.find('down') != -1): 
    depth += int(currentline[-1])
  if (currentline.find('up') != -1): 
    depth -= int(currentline[-1])
print(f"Total distance forward = {forward_total}")
print(f"Total depth  = {depth}")
print(f"Total distance = {depth * forward_total}")

#task2
f = open("input.txt", "r")
forward_total = 0
depth = 0
aim = 0 
for x in f:
  currentline = x.strip()
  if (currentline.find('forward') != -1): 
    forward_total += + int(currentline[-1])
    depth += (aim * int(currentline[-1]))
  if (currentline.find('down') != -1): 
    aim += int(currentline[-1])
  if (currentline.find('up') != -1): 
    aim -= int(currentline[-1])
print(f"Total distance forward = {forward_total}")
print(f"Total depth  = {depth}")
print(f"Total distance = {depth * forward_total}")





