#!/usr/bin/env python3
def bubblesort(in_list: list) -> list:

  swaps = False
  for i in range(0, len(in_list)-1):
    if in_list[i] > in_list[i+1]:
        temp = in_list[i+1]
        in_list[i+1] = in_list[i]
        in_list[i] = temp
        swaps = True

  if swaps == True:
    bubblesort(in_list)

  return in_list

a = [3,7,2,8,4,6,9,1,4]

b = bubblesort(a)

print(b)