from textwrap import dedent

"""
Doorway to the Metropolis.  Adjacent to Birth and Plains.  Bushes shake
when certain the inventory does not contain the smelly_key or when it
contains the elf_blessing.
"""

class Grove():

    def enter(self,inv):
        #different the first time.  First time you've been here, you will not
        #have the smelly_key so that is assumed and the bushes rustle
        if inv['grove_visited'] == 0:
            inv['grove_visited'] = 1
            print(dedent("""
                You look around you and see that there are rows of giant flowers.
                Some of them are bloomed like yours, others are tight buds.  The
                air is filled with an intermingling of smells.  You walk down the
                rows and you hear a rustle.  Do you search the bushes?
                """))

            action = input("> ")

            if action == "yes" and inv['clothes'] == 0:
                print(dedent("""
                    A hideous beast stares up at you.  He grins with crooked teeth.
                    You can smell his rancid breath.  He reaches up and grabs your
                    hand.  Do you recoil? (yes/no)
                    """))

                action2 = input("> ")

                if action2 == "no":
                    print(dedent("""
                    He takes you through a tiny hole in the shrubs.
                    Your face gets scratched by the branches.
                    """))
                    return 'metropolis', inv

                else:
                    print(dedent("""
                        He scampers away.  You walk to the end of the grove.
                        """))
                    return 'plains', inv

            elif action == "yes" and inv['clothes'] == 1:
                print(dedent("""
                    The beast sniffs you cautiously.  Suddnely, he recoils voilently.
                    He runs through the bushes.  You try to follow, but the brush
                    is too thick.  You decide to carry on and walk to the end of the
                    grove.
                    """))

                return 'plains', inv

            #Player did not check rustle
            else:
                print(dedent("""
                    You amble down the quiet grove, admiring its beauty.
                    """))
                return 'plains', inv

        #any time player does not have smelly key we initiate the rustle
        elif inv['smelly_key'] == 0:
            print(dedent("""
                You have returned to the rows of giant flowers.  You walk down
                the rows and you hear a rustle.  Do you search the bushes?
                """))

            action = input("> ")

            if action == "yes" and inv['clothes'] == 0:
                print(dedent("""
                    A hideous beast stares up at you.  He grins with crooked teeth.
                    You can smell his rancid breath.  He reaches up and grabs your
                    hand.  Do you recoil? (yes/no)
                    """))

                action2 = input("> ")

                if action2 == "no":
                    print(dedent("""
                    He takes you through a tiny hole in the shrubs.
                    Your face gets scratched by the branches.  The bushes clear
                    and you behold a bustling metropolis.
                    """))
                    return 'metropolis', inv

                else:
                    print(dedent("""
                        He scampers away.  You are near your flower and in the
                        distance you can see the plains.  Where would you like
                        to go?
                        """))
                    response = input("> ")
                    if 'flower' in response:
                        return 'birth',inv
                    else:
                        return 'plains', inv

            elif action == "yes" and inv['clothes'] == 1:
                print(dedent("""
                    The beast sniffs you cautiously.  Suddnely, he recoils voilently.
                    He runs through the bushes.  You try to follow, but the brush
                    is too thick.  You are near your flower and in the
                    distance you can see the plains.  Where would you like
                    to go?
                    """))
                response = input("> ")
                if 'flower' in response:
                    return 'birth',inv
                else:
                    return 'plains', inv
            else:
                print(dedent("""
                    You are near your flower and in the
                    distance you can see the plains.  Where would you like
                    to go?
                    """))
                response = input("> ")
                if 'flower' in response:
                    return 'birth',inv
                else:
                    return 'plains', inv

        #wearing the right clothes with the elf's blessing and not the
        #yoogalie_blessing we see the little yoogalie
        elif inv['elf_blessing'] == 1 and inv['clothes'] == 0 and inv['yoogalie_blessing'] == 0:
            print(dedent("""
                You have returned to the rows of giant flowers.  You notice a
                familiar stnech.  "How are you?" the ripe young creatures grins
                up at you.  Do you recoil? (yes/no)
                """))

            action2 = input("> ")

            if action2 == "no":
                print(dedent("""
                    You suck in your breath.  Your face is battered reopening
                    the cuts and bothering the bruises.  The bushes clear
                    and you behold the vast metropolis.
                    """))
                return 'metropolis', inv

            else:
                print(dedent("""
                    He looks up at you heartbroken.  You feel a strange
                    sickening feeling overwhelm you.
                    """))
                return 'death', inv

        #all other cases lead to this.  Thus we have fewer possibilities in
        #the metropolis part of the program
        else:
            print(dedent("""
                You amble down the quiet grove, admiring its beauty.
                You are near your flower and in the distance you
                can see the plains.  Where would you like to go?
                """))
            response = input("> ")
            if 'flower' in response:
                return 'birth',inv
            else:
                return 'plains', inv
