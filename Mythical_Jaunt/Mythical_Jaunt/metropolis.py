from textwrap import dedent

"""
Home scene of the Yoogalie.  The player needs to get the smelly key.
Player will get yoogalie_blessing if they already have the ornate_key.
Player will need to return here to get the blessing if they get the
smelly_key first.
"""

class Metropolis():

    def enter(self,inv):
        #this first if marks whether or not the player has been here.
        #the player can only come here in two situations: they don't have
        #the smelly_key or they have both keys and thus the elf's blessing
        if inv['smelly_key'] == 0:
            inv['smelly_key'] = 1
            if inv['ornate_key'] == 0:
                print(dedent("""
                    The little creature takes you at terrifying speed, weaving you
                    through bushes, trees, ferns, and lichens.  You lose all
                    sense of direction and suddenly you behold a giant metropolis.
                    The buildings stretch upwards as far as you can see, and the
                    city itself spraws out for miles.  An acrimonious stench
                    greets your nose causing you to feel a bit sick.  An obese
                    creature far more hideous than the first bows to you.  "Honored
                    traveller.  I am Queen Tickchaffgall.  We are humbled by your
                    presence.  Please, take this key of our city as a token of
                    appreciation."  You take the key, falberghasted by the
                    compliments.  The key has an odor more potent than the rest
                    of the city.  The look of the key is somehow sickening to you.
                    You bow to the queen and stash the key in your pocket.  Your
                    guide smiles up at you with his crooked teeth and rancid breath.
                    He jerks your arm and you are off running through the brush once
                    more.
                    """))

                return 'birth', inv
            else:
                #both keys are now obtained so we get the yoogalie_blessing
                #we just got the smelly_key so we don't have elf_blessing
                inv['yoogalie_blessing'] = 1
                print(dedent("""
                    The little creature takes you at terrifying speed, weaving you
                    through bushes, trees, ferns, and lichens.  You lose all
                    sense of direction and suddenly you behold a giant metropolis.
                    The buildings stretch upwards as far as you can see, and the
                    city itself spraws out for miles.  An acrimonious stench
                    greets your nose causing you to feel a bit sick.  An obese
                    creature far more hideous than the first bows to you.  "Honored
                    traveller.  I am Queen Tickchaffgall.  We are humbled by your
                    presence.  Please, take this key of our city as a token of
                    appreciation."  You take the key, falberghasted by the
                    compliments.  The key has an odor more potent than the rest
                    of the city.  The look of the key is somehow sickening to you.
                    You bow to the queen and stash the key in your pocket.  As you
                    bow the Queen leans over and smells you.  She takes the ornate
                    key from you pocket.
                    "The elves have approved of you!  I thought surely they would try
                    to kill something that smelled as nicely as you!  If both we
                    and the elves are agreed in honoring you then mayhaps there
                    can be peace between us yet.  As thanks, take this blessing!
                    Your guide smiles up at you with his crooked teeth and
                    rancid breath.  He jerks your arm and you are off running
                    through the brush once more.
                   """))

                return 'birth', inv

        else:
            #only way to get here is to already have the elf_blessing
            inv['fused_key'] = 1
            print(dedent("""
                The run through the bushes was no less terrifying then the first
                time.  You stare at the grand metropolis as you catch your breath.
                Queen Tickchaffgall saunters up to you, "I am amazed at this news.
                The elves have approved of you!  I thought surely they would try
                to kill you!  If both we and the elves are agreed in honoring
                you then mayhaps there can be peace between us yet.  As thanks,
                take this blessing!  The keys in your pockets start to glow.
                They fly from your pockets and smash together.  The crowd around
                you gasps.  You feel yourself become thin like air on a mountain
                top.  You try to gasp for breath.
                """))

            return 'plains', inv
