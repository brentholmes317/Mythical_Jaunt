from sys import exit
from textwrap import dedent

"""This is the final scene in Mythical_Jaunt.  This scene is merely an ending"""

class Doorway():

    def enter(self, inv):
        print(dedent("""
            The door opens and a blinding light encapsulates you.  Your eyes
            adjust to the splendor and you see a large fairy floating above an
            enormous hibiscus.  She smiles at you.  "Congratulations.  You have
            made peace with the warring peoples of this land.  Through your
            perserverance and insight, you have done a great good.  For this
            I grant you an invaluable knowledge.  I bestow upon you the meaning
            of life.  You listen carefully to here sing song voice and as you
            come to comprehend her meaning you eyes snap open.  You look around
            to find you are in your bedroom."
            """))
        exit(1)
