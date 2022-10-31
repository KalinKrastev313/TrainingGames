from random import randint
import  matplotlib.pyplot as plt


def remove_first_door(prize_place, first_guess):
    while True:
        first_door = randint(1, 3)
        if not first_door == prize_place and not first_door == first_guess:
            return first_door


def current_result_with_swapping(prize_place, first_guess):
    if not prize_place == first_guess:
        return 1
    else:
        return 0


def current_result_without_swapping(prize_place, first_guess):
    if prize_place == first_guess:
        return 1
    else:
        return 0


total_result_without_swapping = 0
total_result_with_swapping = 0
difference_data = []
relative_difference_data = []

for _ in range(1000):
    prize_place = randint(1, 3)
    first_guess = randint(1, 3)
    first_removed_door = remove_first_door(prize_place, first_guess)
    total_result_without_swapping += current_result_without_swapping(prize_place, first_guess)
    total_result_with_swapping += current_result_with_swapping(prize_place, first_guess)
    current_difference = total_result_without_swapping - total_result_with_swapping
    difference_data.append(current_difference)
    if total_result_with_swapping > 0:
        relative_difference_data.append(round(total_result_without_swapping/total_result_with_swapping, 4))


plt.plot(relative_difference_data)
plt.ylabel('Difference')
plt.xlabel('Guess number')
plt.show()
print(total_result_without_swapping)
print(total_result_with_swapping)
