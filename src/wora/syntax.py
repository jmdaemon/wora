import typing

def tern(cond, x, y) -> typing.Any:
    ''' Ternary operator '''
    return x if cond else y

def tern_bool(cond) -> bool:
    ''' Returns true if the condition is true, else false '''
    return tern(cond, True, False)
