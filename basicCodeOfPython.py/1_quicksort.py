<<<<<<< HEAD
def quickSort(cards):
    if len(cards) <= 1:
        return cards
    else:
        pivot = cards[len(cards) // 2]
        less = [i for i in cards if i <= pivot]
        greater = [i for i in cards if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
=======
def quicksort(cards):
  if len(cards)==1:
    return 1
  else:
    pivot = cards[0]
    less = [i for i in cards if i <= pivot]
    greater = [i for i  in cards if i > pivot]
    return quicksort[less] + pivot + quicksort[greater]
>>>>>>> e6ba0bf757041669ef2bff057324800e6c6780e4
