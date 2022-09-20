# import npc_class
from npc_class import Npc
import character_class
import useful_functions


def main():
    npc = {
        'npc_type': 'monster',
        'hp': 100,
        'weapon': 'sword',
        'drop': 'red_gem',
        'defence_factor': 0.345,
        'xp': 1000,
        'stats': {'str': 8, 'int': 2, 'chr': 1, 'agl': 3}
    }

    damage = 10
    npc['hp'] -= damage
    print(npc['hp'])

    print(npc['stats'])

    stats_dict = npc['stats']
    strength_stat = stats_dict['str']
    print(strength_stat)

    str_stat = npc['stats']['str']
    print(str_stat)

    monster1 = Npc('monster', 100, 'sword', 'red_gem', 0.345, 1000,
                   {'str': 8, 'int': 2, 'chr': 1, 'agl': 3}, 'Rawwrrr!')

    print(monster1.hp)
    print(monster1.stats)

    print(f'This is the monster\'s hp: {monster1.get_hp()}')

    monster1.speak()
    monster1.take_damage(78)
    print(monster1.hp)

    generic_character = character_class.Character()
    generic_character.x_pos = 34
    generic_character.y_pos = 109

    position = generic_character.get_position()

    print(position)

    monster1.x_pos = 24
    monster1.y_pos = 68
    monster_pos = monster1.get_position()

    print(monster_pos)

    # use functions from the 'useful_functions.py' file
    print(useful_functions.useful_print_function('Joe'))
    print(useful_functions.do_addition(5, 6))
    print(useful_functions.another_print_function('something'))

    # immutable object
    some_str = 'This is half of the string...'
    print(some_str)
    new_string = useful_functions.add_to_string(some_str)
    some_str = new_string
    print(some_str)

    # mutable objects
    some_python_list = [34, 78, 123, 89, 'joe']
    print(some_python_list)
    useful_functions.change_elemete_list(some_python_list)
    print(some_python_list)


if __name__ == '__main__':
    main()
