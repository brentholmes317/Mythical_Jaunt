from textwrap import dedent

"""This file contains the Birth class.  Birth is the opening scene from
Mythical_Jaunt.  In this scene, the troll comes to the player and offers
a clean change of clothes.  The scene always ends by sending the player
to Grove.  We are able to revisit this scene and the troll will act differently
thus we utilize a 'birth_visited' variable to keep track if we've been here
or not."""

class Birth():

    def enter(self,inv):
        if inv['birth_visited'] == 0:
            inv['birth_visited'] = 1
            print(dedent("""
                You open your eyes.  Darkness.  A musty aroma greets your nostrils.
                It reminds you of wilting flowers.  You are held tight in the darkness.
                You feel a rustling and suddenly blinding light encapsulates you.
                The pressure is gone and you feel breeze agaisnt your wet skin.
                A short, gnarly troll approaches you.  He grunts, "Fresh Clothes?"
                You look down at your clothes.  They are covered in some kind of slimy
                liquid.
                """))

            action = input("> ")

            if "yes" in action:
                inv['clothes'] = 1
                print(dedent("""
                        The gnarly troll hands you some fresh clothes.  They are
                        a resplendent white.  As you try them on you are surprised
                        to find they fit perfectly to your form.
                        """))
                #I wait until here tp change birth_visited, so that if we don't
                #get yes or no, we still
                #get the intro part repeated instead of the return text.
                inv['birth_visited'] = 1
                #we return that we are going to the grove next and 'clothes'
                #needs to be changed to 1 in the dictionary.
                return 'grove', inv

            elif "no" in action:
                print(dedent("""
                        The gnarly troll shrugs, "Mk."  He walks away through the
                        rows of giant flowers.
                        """))
                inv['birth_visited'] = 1
                return 'grove', inv

            else:
                print("'A yes or no will suffice,' grunts the troll.")
                return 'birth', inv

        #throughout the game we need to change clothes.  This is how we do it.
        else:
            print(dedent("""
                The melancholy troll looks off into the distance.
                You clear your throat, but he stays motionless.  You cough
                uncomfortably.  A mouse sprints across the grassy ground.  The
                troll dives after it, but the mouse escapes into a hole in the
                ground.  The troll jumps up and glares at you.  "Look what you've
                done!"  He kicks dust, and then grunts "I suppose you've changed
                your mind about the clothes?"
                """))

            action = input("> ")

            if action == "yes" and inv['clothes'] == 0:
                inv['clothes'] = 1
                print(dedent("""
                He hands you fresh clothes.  They are
                a resplendent white.  They fit perfectly to your form.
                    """))
                return 'grove',inv
            elif action == "yes" and inv['clothes'] == 1:
                inv['clothes'] = 0
                print(dedent("""
                He hands you your old clothes.  They seem
                to have developed an even worse stench under the care of the
                troll.
                """))
                return 'grove', inv
            else:
                print(dedent("""
                    He glares at you.  "Why must you waste my time
                    and scare off my dinner!"
                    """))
                return 'grove',inv
