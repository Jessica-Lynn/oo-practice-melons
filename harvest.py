############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        



        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        my_melons_pairings_list = self.pairings
        my_melons_pairings_list.append(pairing)


        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    Muskmelon = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    Muskmelon.add_pairing("mint")
    all_melon_types.append(Muskmelon)

    Casaba = MelonType("cas", "2003", "orange", False, False, "Casaba")
    Casaba.add_pairing("mint", "strawberries")
    all_melon_types.append(Casaba)

    Crenshaw = MelonType("cren", "1996", "green", False, False, "Crenshaw")
    Crenshaw.add_pairing("proscuitto")
    all_melon_types.append(Crenshaw)

    Yellow_watermelon = MelonType("yw", "2013", "yellow", False, True, "Yellow Watermelon")
    Yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(Yellow_watermelon)
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        pairings_list_for_each melon = melon.pairings

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



