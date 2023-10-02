"""Functions
"""
import turtle as t
from itertools import chain

from turtle_tutorial.contextGraph import ScreenContext

def rewrite(string: str, rules: dict, times: int)->str: #Functional style? using recursion
    """rewrite a `string` n `times` using some replacing `rules`
    """
    rewrited_string = string
    for _ in range(times):
        temp = ""
        for letter in rewrited_string:
            if rules.get(letter):
                temp += rules[letter]
            else:
                temp += letter
        rewrited_string = temp

    return rewrited_string

def string2turtle(string: str, myturtle: t.Turtle) -> list:
    """Return the string of instructions as a list of turtle commands for `myturtle` object
    """
    association_rules = {
        "F": [myturtle.forward],
        "f": [myturtle.up, myturtle.forward, myturtle.down],
        "+": [myturtle.left],
        "-": [myturtle.right]
    }
    nested = map(lambda x: association_rules[x], string)
    return list(chain.from_iterable(nested))

def draw(
    string: str,
    rules: dict,
    distance: int,
    angle: float,
    deepth: int
) -> None:

    with ScreenContext as context:
        screen = context.screen
        myturtle = t.Turtle()
        turtle_path = string2turtle(
            rewrite(string=string, rules=rules, times=deepth),
            myturtle=myturtle
        )

        for step_name in turtle_path:
            step = turtle_path
            print(step.__str__)



if __name__ == "__main__":
    t1 = t.Turtle
    print(string2turtle("FF-f-F+F+f", t1))
