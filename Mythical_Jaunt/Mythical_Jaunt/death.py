from sys import exit
from random import randint
from textwrap import dedent

"""
This scene ends the game with a loss.
"""

class Death():

    quips = [
        "You got transformed into a tree.  A tree lives a long life, but a boring one.",
        "You become a cloud, and you really need to rain!",
        "You wake up drenched in sweat.  What a strange dream!",
        dedent("""
        The speed of time increases.  You watch civilizations rise and die.
        You experience all, but cannot participate.
        You have been turned to stone.
        """),
    ]

    def enter(self,inv):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
