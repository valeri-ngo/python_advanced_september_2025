from collections import deque

def input_data() -> tuple[deque[int], list[int]]:
    bees = deque(int(x) for x in input().split())
    bee_eaters = [int(y) for y in input().split()]
    return bees, bee_eaters

def fight(bees_count: int, eaters_count: int) -> tuple[int, int]:
    power = eaters_count * 7
    if bees_count > power:
        return bees_count - power, 0
    elif bees_count < power:
        used = bees_count // 7
        survivors = eaters_count - used
        return 0, survivors
    else:
        return 0, 0

def fight_process(bees: deque[int], bee_eaters: list[int]) -> None:
    current_bees = bees.popleft()
    current_eaters = bee_eaters.pop()
    rem_bees, rem_eaters = fight(current_bees, current_eaters)
    if rem_bees > 0:
        bees.append(rem_bees)
    elif rem_eaters > 0:
        bee_eaters.append(rem_eaters)

def result_print(bees: deque[int], eaters: list[int]) -> str:
    result = "The final battle is over!\n"
    if not bees and not eaters:
        result += "But no one made it out alive!"
    elif bees:
        result += f"Bee groups left: {', '.join(map(str, bees))}"
    else:
        result += f"Bee-eater groups left: {', '.join(map(str, eaters))}"
    return result

def main() -> None:
    bees, bee_eaters = input_data()
    while bees and bee_eaters:
        fight_process(bees, bee_eaters)
    print(result_print(bees, bee_eaters))

if __name__ == "__main__":
    main()



# bees = deque([int(x) for x in input().split()])
# bee_eaters = [int(x) for x in input().split()]
#
# while bees and bee_eaters:
#
#     current_bees = bees.popleft()
#     current_bee_eaters = bee_eaters.pop()
#
#     while current_bees > 0 and current_bee_eaters > 0:
#         if current_bee_eaters * 7 <= current_bees:
#             current_bees -= current_bee_eaters * 7
#             current_bee_eaters = 0
#         else:
#             current_bee_eaters -= (current_bees // 7)
#             current_bees = 0
#
#     if current_bees > 0 and current_bee_eaters == 0:
#         bees.append(current_bees)
#     elif current_bees == 0 and current_bee_eaters > 0:
#         bee_eaters.append(current_bee_eaters)
#
# print(f"The final battle is over!")
# if not bees and not bee_eaters:
#     print(f"But no one made it out alive!")
# elif bees:
#     print(f"Bee groups left: {', '.join(map(str, bees))}")
# elif bee_eaters:
#     print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters))}")
