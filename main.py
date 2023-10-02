"""Functions
"""
import turtle as t
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

def string2turtle(
    string: str,
    myturtle: t.Turtle
) -> list:

    """Return the string of instructions as a list of turtle commands for `myturtle` object
    """
    association_rules = {
        "F": (myturtle.forward, "forward"),
        "f": ([myturtle.up, myturtle.forward, myturtle.down], "forward_up"),
        "+": (myturtle.left, "left"),
        "-": (myturtle.right, "right")
    }
    nested = map(lambda x: association_rules[x], string)
    return list(nested)

def draw(
    string: str,
    rules: dict,
    distance: int,
    angle: float,
    deepth: int
) -> None:

    with ScreenContext() as context:
        screen = context.screen
        myturtle = t.Turtle()
        myturtle.penup()
        myturtle.goto(-700, 200)
        myturtle.pendown()
        turtle_path = string2turtle(
            rewrite(string=string, rules=rules, times=deepth),
            myturtle=myturtle,
        )

        for step_pack in turtle_path:
            name = step_pack[1]
            action = step_pack[0]
            if name == "forward":
                action(distance)
            elif name == "forward_up":
                action[0]()
                action[1](distance)
                action[2]()
            else:
                action(angle)
        myturtle.hideturtle()
        context.screenshot()




if __name__ == "__main__":
    conf1 = {
        "string":"F-F-F-F",
        "rules":{
            "F": "F-F+F+FF-F-F+F"
        },
        "distance": 5,
        "angle": 60.0,
        "deepth": 3
    }

    conf2 = {
        "string":"F+F+F+F",
        "rules":{
            "F": "F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF",
            "f": "ffffff"
        },
        "distance": 5,
        "angle": 90.0,
        "deepth": 3
    }
    draw(
        **conf2
    )
    
