from importlib.metadata import entry_points


class Pokemon:
    
    # Attributes
    name = ""
    entryNumber = 0
    level = 5
    moves = ['Scratch', 'Ember', 'Tackle']

    # Contructor
    def __init__(this, name, entryNumber):
        this.name = name # Setting the pokemon object name.
        this.entryNumber = entryNumber # setting the pokemon object entry number


    # Begin Methods Section =============================== # 
    
    # increases the Pokemon's level by 1... could rework in the future to account for experience needed to level up.
    def levelUp(this):
        this.level += 1 
        
    # Prints the Pokemon's Information
    def printPokemonInfo(this):
        print("\n# ====================== #")
        print("Pokemon name: " + str(this.name))
        print("Pokedex Entry Number: " + str(this.entryNumber))
        print("Level: " + str(this.level))
        this.printMoves()
        
        
    # This is a method that will print a list of the moves on a Pokemon
    def printMoves(this):
        
        print("Pokemon Moves: ")
        i = 0
        while i < len(this.moves):
            print(this.moves[i])
            i += 1



# Instantiating our pokemon
partyMember1 = Pokemon("Pikachu", 25)
partyMember2 = Pokemon("Charmander", 4)

partyMember2.printPokemonInfo()

# # Checking output
# print(str(partyMember2.name) + " is at level " + str(partyMember2.level))

# #Level up Charmander
# partyMember2.levelUp()

# # Check the level
# print(str(partyMember2.name) + " is at level " + str(partyMember2.level))

# # Print the moves
# partyMember2.printMoves()