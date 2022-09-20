import npc_class


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

    monster1 = npc_class.Npc('monster', 100, 'sword', 'red_gem', 0.345, 1000,
                             {'str': 8, 'int': 2, 'chr': 1, 'agl': 3}, 'Rawwwrr!')

    print(monster1.hp)
    print(monster1.stats)

    print(f'This is the monster\'s hp: {monster1.get_hp()}')

    monster1.speak()
    
    monster1.set_hp(78)

    print(monster1.hp)


if __name__ == '__main__':
    main()
