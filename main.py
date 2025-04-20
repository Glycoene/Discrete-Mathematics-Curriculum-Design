from itertools import product

def check_conditions(butler_bool: bool, chef_bool: bool, gardener_bool: bool, servant_bool: bool) -> bool:
    if butler_bool and not chef_bool:
        return False
    if chef_bool and gardener_bool:
        return False
    if not gardener_bool and not servant_bool:
        return False
    if servant_bool and chef_bool:
        return False
    return True
    # cond1 = (not butler_bool) or chef_bool
    # cond2 = not (chef_bool and gardener_bool)
    # cond3 = gardener_bool or servant_bool
    # cond4 = (not servant_bool) or (not chef_bool)
    # return cond1 and cond2 and cond3 and cond4

for butler, chef, gardener, servant in product([True, False], repeat=4):
    if check_conditions(butler, chef, gardener, servant):
        print(f"男管家：{'真话' if butler else '假话'}",
              f"厨师：{'真话' if chef else '假话'}",
              f"园丁：{'真话' if gardener else '假话'}",
              f"杂役：{'真话' if servant else '假话'}")