def quicksort(cards):
  if len(cards)==1:
    return 1
  else:
    pivot = cards[0]
    less = [i for i in cards if i <= pivot]
    greater = [i for i  in cards if i > pivot ]
    return quicksort[less] + pivot + quicksort[greater]
