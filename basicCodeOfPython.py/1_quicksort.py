def quickSort(cards):
    if len(cards) <= 1:
        return cards
    else:
        pivot = cards[len(cards) // 2]
        less = [i for i in cards if i <= pivot]
        greater = [i for i in cards if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
