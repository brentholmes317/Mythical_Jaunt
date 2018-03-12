from textwrap import dedent

"""
This is a middle ground between the forest which leads to the elf kingdom and
the grove (flowers) which leads to the metropolis.  There is also a door, which
leads to the end game screen.
"""

class Plains():

    def enter(self,inv):
        if inv['plains_visited'] == 0:
            inv['plains_visited'] = 1
            print(dedent("""
                You come upon a great plains.  In the middle of the plains there
                is a giant door with a single key hole.  There is no wall, merely
                a door. You look on the opposite side of the door and behold there
                is nothing behind it.  To the East, you see a forest.  To the West,
                you see the grove of flowers.  Do you go to: the door, the forest,
                or the flowers?
                """))

            action = input("> ")

            if 'door' in action:
                if inv['fused_key'] == 1:
                    print(dedent("""
                        You slide your fused key into the door.
                        """))
                    return 'doorway', inv
                elif inv['ornate_key'] + inv['smelly_key'] == 0:
                    print(dedent("""
                        You do not seem to have a way to interact with the door.
                        """))
                    return 'plains', inv
                elif inv['ornate_key'] + inv['smelly_key'] == 1:
                    print(dedent("""
                        The key does not fit.
                        """))
                    return 'plains', inv
                elif inv['ornate_key'] + inv['smelly_key'] == 2:
                    print(dedent("""
                        Neither key fits.  Strange.
                        """))
                    return 'plains', inv

            elif 'forest' in action:
                return 'forest', inv

            else:
                return 'grove', inv
        else:
            print(dedent("""
                You return to the great plains.  In the middle of the plains there
                is a giant door with a single key hole.  To the East, you see a
                forest.  To the West, you see the grove of flowers.
                Do you go to: the door, the forest, or the flowers?
                """))

            action = input("> ")

            if 'door' in action:
                if inv['fused_key'] == 1:
                    print(dedent("""
                        You slide your fused key into the door.
                        """))
                    return 'doorway', inv
                elif inv['ornate_key'] + inv['smelly_key'] == 0:
                    print(dedent("""
                        You do not seem to have a way to interact with the door.
                        """))
                    return 'plains', inv
                elif inv['ornate_key'] + inv['smelly_key'] == 1:
                    print(dedent("""
                        The key does not fit.
                        """))
                    return 'plains', inv
                elif inv['ornate_key'] + inv['smelly_key'] == 2:
                    print(dedent("""
                        Neither key fits.  Strange.
                        """))
                    return 'plains', inv

            elif 'forest' in action:
                return 'forest', inv

            else:
                return 'grove', inv
