### WEEK 5, SESSION 1, Advanced Problem Set Version 1

# QUESTION 1: Villager Class

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should all the provided attributes be publicly accessible or are there any privacy considerations?
    Q2: Are there any default values needed for the parameters besides the empty list for furniture?

2. Write out in plain English what you want to do:

    I need to create a class constructor for the Villager class that initializes
    four attributes. The constructor should accept three required parameters:
    name, species, and catchphrase, and set them as instance attributes.
    Additionally, I need to initialize a furniture attribute as an empty list.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Define constructor method
    define __init__ method with parameters self, name, species, catchphrase
    
    Subproblem 2: Initialize instance attributes
    set self.name to name parameter
    set self.species to species parameter
    set self.catchphrase to catchphrase parameter
    set self.furniture to empty list

4. Translate the pseudocode into Python and share your final answer:
    class Villager:
        def __init__(self, name, species, catchphrase):
            self.name = name
            self.species = species
            self.catchphrase = catchphrase
            self.furniture = []

"""

# QUESTION 2: Add Furniture

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the method provide any feedback when an invalid item is attempted to be added?
    Q2: Should we allow duplicate items to be added to the furniture list?

2. Write out in plain English what you want to do:

    I need to add a method to the Villager class that validates furniture items
    before adding them to the villager's furniture list. The method should check
    if the item_name matches one of the five valid items, and only add it to the
    furniture list if it's valid. Invalid items should be ignored.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Define valid items
    valid_items <- set containing the five allowed furniture items
    
    Subproblem 2: Validate and add item
    if item_name is in valid_items:
        append item_name to self.furniture

4. Translate the pseudocode into Python and share your final answer:
    def add_item(self, item_name):
        valid_items = {"acoustic guitar", "ironwood kitchenette", 
                       "rattan armchair", "kotatsu", "cacao tree"}
        
        if item_name in valid_items:
            self.furniture.append(item_name)

"""

# QUESTION 3: Group by Personality

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the function handle empty input lists or None values gracefully?
    Q2: Should the comparison be case-sensitive when matching personality types?

2. Write out in plain English what you want to do:

    I need to create a function that filters a list of Villager instances based
    on their personality attribute. The function should iterate through the list
    of villagers, check each villager's personality against the target personality
    type, and collect the names of matching villagers into a result list.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Filter villagers by personality
    result <- empty list
    for each villager in townies:
        if villager.personality equals personality_type:
            add villager.name to result
    return result

4. Translate the pseudocode into Python and share your final answer:
    def of_personality_type(townies, personality_type):
        return [villager.name for villager in townies if villager.personality == personality_type]

"""

# QUESTION 4: Telephone

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we handle potential circular references to avoid infinite loops?
    Q2: What should happen if start_villager and target_villager are the same instance?

2. Write out in plain English what you want to do:

    I need to implement a function that traverses a chain of villager neighbors
    to determine if a message can reach from start_villager to target_villager.
    I'll follow the neighbor links starting from start_villager, checking each
    villager in the chain until I either find the target_villager or reach the
    end of the chain (None neighbor).

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Traverse neighbor chain
    curr_villager <- start_villager
    while curr_villager is not None:
        if curr_villager equals target_villager:
            return True
        else:
            curr_villager <- curr_villager.neighbor
    
    Subproblem 2: Handle case where target not found
    return False

4. Translate the pseudocode into Python and share your final answer:
    def message_received(start_villager, target_villager):
        curr_villager = start_villager
        while curr_villager:
            if curr_villager == target_villager:
                return True
            else:
                curr_villager = curr_villager.neighbor
        
        return False

"""

# QUESTION 5: Linked Up

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we verify that the linked list is properly connected after creation?
    Q2: Are there any memory considerations when linking these nodes?

2. Write out in plain English what you want to do:

    I need to connect the four existing Node instances to create a linked list
    in the specified order. Each node's next attribute should point to the
    subsequent node in the sequence, with the last node's next remaining None.
    I'll set the next pointers to establish the chain: kk_slider -> harriet -> saharah -> isabelle.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Link nodes in sequence
    set kk_slider.next to harriet
    set harriet.next to saharah
    set saharah.next to isabelle
    (isabelle.next remains None by default)

4. Translate the pseudocode into Python and share your final answer:
    kk_slider.next = harriet
    harriet.next = saharah
    saharah.next = isabelle

"""