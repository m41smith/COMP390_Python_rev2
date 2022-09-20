
# this file has some functions that we can use throughout our project

def useful_print_function(incoming_str):
    return f'Hello, {incoming_str}'


def do_addition(term1, term2):
    return term1 + term2


def another_print_function(some_string):
    for _ in range(5):
        print(some_string)
    return 'the loop is done!'


def add_to_string(incoming_str):
    new_string = f'{incoming_str} this is the other half'
    return new_string

def change_elemete_list(some_list):
    some_list[0] = 'new_string'
