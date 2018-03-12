from textwrap import dedent

class ElfKingdom():

    def enter(self,inv):
        if inv['ornate_key'] == 0:
            inv['ornate_key'] = 1
            if inv['smelly_key'] == 0:
                print(dedent("""
                    The elf takes you to his king, who stands tall even
                    amongst the elves.  He wears flowing, dazzling white
                    garments and is covered in flowers of bright colors.
                    He looks upon you and in a baratone voice, "I am amazed
                    by your splendor!  You are a true friend of the elf
                    kingdom."  He reaches into his flowing robes and produces
                    an ornate key.  "I grant you this token of our people
                    as an honor to you, our great guest."  You watch as the
                    elves bring forth food and drink.  Such a lavish feast
                    you have never experienced.  As the feast concludes, the
                    elf you met at the creek takes your hand and dashes you
                    through the forest back to the plains.
                    """))
                return 'plains', inv
            else:
                print(dedent("""
                    The elf takes you to his king, who stands tall even
                    amongst the elves.  He wears flowing, dazzling white
                    garments and is covered in flowers of bright colors.
                    He looks upon you and in a baratone voice, "I am amazed
                    by your splendor!  You are a true friend of the elf
                    kingdom."  He reaches into his flowing robes and produces
                    an ornate key.  "I grant you this token of our people
                    as an honor to you, our great guest."  As he reaches out
                    to hand you the key, his nose curls and he wretches.
                    "That stench!  Could it be the heirloom of the Yoogalie?
                    I thought they would kill such a beautiful creature!
                    If both we and the elves are agreed in honoring
                    you then mayhaps there can be peace between us yet.
                    As thanks, take this blessing!
                    """))
                if 'yoogalie_blessing' == 1:
                    inv['fused_key'] = 1
                    print(ddent("""
                        The keys in your pockets
                        start to glow.  They fly from your pockets and smash
                        together.  The crowd around you gasps.  You feel
                        yourself become thin like air on a mountain top.
                        You try to gasp for breath.
                        """))
                    return 'plains', inv
                else:
                    inv['elf_blessing'] = 1
                    print(dedent("""
                        You watch as the elves bring forth food and drink.
                        Such a lavish feast you have never experienced.
                        As the feast concludes, the elf you met at the
                        creek takes your hand and dashes you
                        through the forest back to the plains.
                        """))
                    return 'plains', inv

        else:
            inv['fused_key'] = 1
            print(dedent("""
                    You return to the king.  He booms from his throne,
                    "We have heard you visited the Yoogalie.
                    I thought they would kill such a beautiful creature!
                    If both we and the elves are agreed in honoring
                    you then mayhaps there can be peace between us yet.
                    As thanks, take this blessing! The keys in your pockets
                    start to glow.  They fly from your pockets and smash
                    together.  The crowd around you gasps.  You feel
                    yourself become thin like air on a mountain top.
                    You try to gasp for breath.
                """))

            return 'plains', inv
