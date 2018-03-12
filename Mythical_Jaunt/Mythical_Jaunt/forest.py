from textwrap import dedent

"""
This is the forest scene.  The forest scene is the player's first interaction
with the elves.  There are many different ways in which this scene can occur.
The elves will react differently based on if the player has the ornate_key,
the smelly_key, and the clean clothes.  Thus we run loops to examine these
scenarios.  If the player does not have the ornate_key then the elves interact.
They interact in a friendly way if the player has clean clothes and a violent
way otherwise.  If the player has the ornate_key but not the smelly_key, then
the elves do not appear.  If the player has both keys the elves return and
again their behavior depends on the clothes.
"""

class Forest():

    def enter(self,inv):
        if inv['fused_key'] == 1:
            print(dedent("""
                The forest is comforting and seemingly empty.  You drink from
                the brook and then return to the plains.
                """))
            return 'plains', inv
        else:
            pass
        if inv['ornate_key'] == 0:
            print(dedent("""
                You wander through the trees.  As you go you notice the trees
                are spaced regularly and the ground is clear of brush and lichens.
                This is no wild forest.  You come to a babbling brook.  A tall
                pointed eared man stares at you.
                """))

            #elves attack dirty clothes
            if inv['clothes'] == 0:
                print(dedent("""
                    He roars a battle cry and beats his chest.  Do you run?
                    """))

                action2 = input("> ")

                if action2 == "yes" or action2 == "run":
                    print(dedent("""
                    You sprint through the forest.  Arrows whizz by your ears.
                    You stumble into the plains and the arrows cease.
                    """))
                    return 'plains', inv

                else:
                    print(dedent("""
                        He begins a menacing chant.
                        """))
                    return 'death', inv

            else:
                print(dedent("""
                    His mouth slacks open, but he quickly shuts it and stand
                    upright.  "Welcome to our land!  You who shimmer like the
                    sun.  You are the ideal form of legend!  Let me take you
                    to our king!"
                    """))

                return 'elfkingdom', inv

        #need to get blessing.  elves are watching.  will react based on clothes
        elif inv['ornate_key'] == 1 and inv['smelly_key'] == 1 and inv['elf_blessing'] == 0:
            print(dedent("""
                You walk calmly through the beautiful forest.  You feel a
                certainty that you are being watched by many eyes.
                """))

            action = input("> ")

            if action == "run" and inv['clothes'] == 0:
                print(dedent("""
                    War chants surround you.  Arrows fly tearing your smelly
                    clothes.  An elf drops down with a sword to block your
                    path but you scurry between her legs.  You arrive to the
                    plains shaken but unharmed.
                    """))
                return 'plains', inv

            #player can run but the elves did not intend to attack
            elif action == "run":
                print(dedent("""
                    You flee in terror.  You come to the plains without any
                    resistance.
                    """))
                return 'plains', inv

            else:
                if inv['clothes'] == 0:
                    print(dedent("""
                        War chants surround you.  Arrows fly tearing your smelly
                        clothes.  The elves shout in what feels like nonsense.
                        You begin to feel sick.
                        """))
                    return 'death', inv
                else:
                    print(dedent("""
                        The elf you first encountered walks forward from the trees.
                        "They are amazed.  You possess the key of the Yoogalie.
                        That they would not kill one so beautiful is wonderous enough,
                        but that they give you their great treasure leaves us without
                        words.  I must take you to the king to seek his wisdom."
                        """))
                    return 'elfkingdom', inv

        #To progress in the game player needs to go to the grove so no actions are offered
        else:
            print(dedent("""
                The forest is comforting and seemingly empty.  You drink from
                the brook and then return to the plains.
                """))
            return 'plains', inv
