from random import randrange

# Globals
# Could be pulled from a separate file using read if desired.
cave_name = "Mysterious Cave"
cave_description = "As you stumble inside, your torch goes out. You hear things moving in the darkness and voices whispering.\nWho knows what lies ahead?"


class Location:

    # Constructor
    # Let's say a Location needs a name, a description (probably pulled)
    # from a file or a global string at the top, n monsters, and a Treasure.
    def __init__(self, name, description, n_monsters, treasure):
        self.name = name
        self.description = description
        self.n_monsters = n_monsters
        self.treasure = treasure
        self.hasVisited = False
        # here we would create a self.monstersList, which instantiates
        # and stores Monster types (leaving that to you).
        # Each Monster would be instantiated randomly (hit points based on difficulty?)

    # This is the same for all locations, so we can go ahead and write.
    def get_description(self):
        return f"You have entered {self.name}.\n{self.description}\nBeware: There are {self.n_monsters} monsters in this location!"


# Cave implements the ABC Location
class Cave(Location):

    # Constructor is almost same as location, but n_monsters is randomly generated here.
    def __init__(self, name, description, treasure):
        n_monsters = randrange(1, 4)  # 1-3 monsters
        Location.__init__(self, name, description, n_monsters, treasure)


def main():
    treasure = (
        "Treasure"
    )  # just a string for now, replace with actual Treasure object later
    cave_location = Cave(cave_name, cave_description, treasure)

    print(cave_location.get_description())


if __name__ == "__main__":
    main()
