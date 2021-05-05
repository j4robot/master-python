# def blackjack_hand_greater_than(hand_1, hand_2):
#     first_hand_total = 0
#     second_hand_total = 0
#     hand_1.reverse()

#     for x in range(len(hand_1)):
#         if hand_1[x].isdigit():
#             first_hand_total += int(hand_1[x])
#         if hand_1[x] in ['J', 'Q', 'K']:
#             if (first_hand_total < 21) and (first_hand_total + 10 < 21):
#                 first_hand_total += 10
#             else:
#                 first_hand_total += 1
#         if hand_1[x] == 'A':
#             if (first_hand_total < 21) and (first_hand_total + 11 < 21):
#                 first_hand_total += 11
#             else:
#                 first_hand_total += 1

#     for x in range(len(hand_2)):
#         if hand_2[x].isdigit():
#             second_hand_total += int(hand_2[x])
#         if hand_2[x] in ['J', 'Q', 'K']:
#             if (second_hand_total < 21) and (second_hand_total + 10 < 21):
#                 second_hand_total += 10
#             else:
#                 second_hand_total += 1
#         if hand_2[x] == 'A':
#             if (second_hand_total < 21) and (second_hand_total + 11 < 21):
#                 second_hand_total += 11
#             else:
#                 first_hand_total += 1
#     return first_hand_total <= 21 and (first_hand_total > second_hand_total or second_hand_total > 21)

def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)
            
    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)



print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))
print(blackjack_hand_greater_than(['K'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10']))