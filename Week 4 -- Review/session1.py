### SESSION 1, VERSION 1, Advanced Problem Set

# PROBLEM 1: Brand Filter

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the criterion match exactly or can it be a partial match within the criteria list?
    Q2: What should be returned if no brands meet the criterion - an empty list?

2. Write out in plain English what you want to do:

    I need to filter through a list of brands and find those that meet a specific sustainability criterion.
    For each brand, I'll check if the given criterion exists in their criteria list.
    If it does, I'll add the brand's name to my result list.
    Finally, I'll return the list of sustainable brand names.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize result storage
    sustainable_brands <- empty list
    
    Subproblem 2: Check each brand for the criterion
    for each brand in brands:
        if criterion exists in brand["criteria"]:
            add brand["name"] to sustainable_brands
    
    Subproblem 3: Return filtered results
    return sustainable_brands

4. Translate the pseudocode into Python and share your final answer:

    def filter_sustainable_brands(brands, criterion):
        Time complexity: O(n * m), where n is the number of brands, 
        and m is the avg. number of criteria per brand
        
        Space complexity: O(k) where k is the number of sustainable brands
        
        sustainable_brands = []
        for brand in brands:
            if criterion in brand["criteria"]:
                sustainable_brands.append(brand["name"])
        
        return sustainable_brands

"""

def filter_sustainable_brands(brands, criterion):
    """
    Time complexity: O(n * m), where n is the number of brands, 
    and m is the avg. number of criteria per brand
    
    Space complexity: O(k) where k is the number of sustainable brands
    """
    sustainable_brands = []
    for brand in brands:
        if criterion in brand["criteria"]:
            sustainable_brands.append(brand["name"])
    
    return sustainable_brands


# PROBLEM 2: Eco-Friendly Materials

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the function return a regular dictionary or maintain any specific ordering?
    Q2: How should we handle empty materials lists - skip the brand or count as zero?

2. Write out in plain English what you want to do:

    I need to count how many times each material appears across all brands.
    I'll use a dictionary to track material counts, iterating through each brand
    and each material within that brand. For each material I encounter,
    I'll increment its count in my dictionary. Finally, I'll return the
    complete count dictionary.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize material counter
    counter <- empty dictionary with default value 0
    
    Subproblem 2: Count materials across all brands
    for each brand in brands:
        for each material in brand["materials"]:
            increment counter[material] by 1
    
    Subproblem 3: Return material counts
    return counter

4. Translate the pseudocode into Python and share your final answer:

    def count_material_usage(brands):
        Time complexity: O(n * m), where n is the number of brands,
        and m is the avg. number of materials per brand
        
        Space complexity: O(u) where u is the number of unique materials
        
        from collections import defaultdict
        counter = defaultdict(int)
        
        for brand in brands:
            for material in brand["materials"]:
                counter[material] += 1
        
        return counter

"""

def count_material_usage(brands):
    """
    Time complexity: O(n * m), where n is the number of brands,
    and m is the avg. number of materials per brand
    
    Space complexity: O(u) where u is the number of unique materials
    """
    from collections import defaultdict
    counter = defaultdict(int)

    for brand in brands:
        for material in brand["materials"]:
            counter[material] += 1

    return counter


# PROBLEM 3: Fashion Trends

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the output maintain any specific order of the trending materials?
    Q2: If a material appears exactly once, should it be excluded from trending?

2. Write out in plain English what you want to do:

    I need to identify materials that appear more than once across all brands.
    I'll use two sets: one to track materials I've seen once, and another to track
    materials I've confirmed as trending (seen multiple times).
    As I iterate through each material, if I've seen it before, I'll add it to trending.
    If I haven't seen it, I'll add it to my visited set. Finally, I'll return
    the trending materials as a list.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize tracking sets
    visited_materials <- empty set
    trending_materials <- empty set
    
    Subproblem 2: Track material occurrences
    for each brand in brands:
        for each material in brand["materials"]:
            if material in visited_materials:
                add material to trending_materials
            else:
                add material to visited_materials
    
    Subproblem 3: Return trending materials
    return list of trending_materials

4. Translate the pseudocode into Python and share your final answer:

    def find_trending_materials(brands):
        Time complexity: O(n * m), where n is the number of brands,
        and m is the avg. number of materials per brand
        
        Space complexity: O(u) where u is the number of unique materials
        
        visited_materials = set()
        trending_materials = set()

        for brand in brands:
            for material in brand['materials']:
                if material in visited_materials:
                    trending_materials.add(material)
                else:
                    visited_materials.add(material)
        
        return list(trending_materials)

"""

def find_trending_materials(brands):
    """
    Time complexity: O(n * m), where n is the number of brands,
    and m is the avg. number of materials per brand
    
    Space complexity: O(u) where u is the number of unique materials
    """
    visited_materials = set()
    trending_materials = set()

    for brand in brands:
        for material in brand['materials']:
            if material in visited_materials:
                trending_materials.add(material)
            else:
                visited_materials.add(material)
    
    return list(trending_materials)


# PROBLEM 4: Fabric Pairing

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we return the pair with the highest cost under budget, or closest to budget?
    Q2: What should happen if no valid pairs exist within the budget?

2. Write out in plain English what you want to do:

    I need to find the pair of fabrics whose combined cost is closest to the budget
    without exceeding it. I'll sort the fabrics by cost first, then use two pointers
    approach - one at the start (cheapest) and one at the end (most expensive).
    I'll track the best pair found so far and move pointers based on whether
    the current sum is under or over budget. This ensures I find the optimal pair efficiently.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Sort fabrics and initialize variables
    sort fabrics by cost in ascending order
    l <- 0 (left pointer)
    r <- length of fabrics - 1 (right pointer)
    min_diff <- infinity
    min_diff_pair <- None
    
    Subproblem 2: Use two pointers to find best pair
    while l < r:
        sum <- fabrics[l][1] + fabrics[r][1]
        if sum <= budget and abs(sum - budget) < min_diff:
            min_diff <- abs(sum - budget)
            min_diff_pair <- (fabrics[l][0], fabrics[r][0])
        
        if sum < budget:
            increment l
        elif sum > budget:
            decrement r
        else:
            break (found exact match)
    
    Subproblem 3: Return best pair
    return min_diff_pair

4. Translate the pseudocode into Python and share your final answer:

    def find_best_fabric_pair(fabrics, budget):
        Time complexity: O(n log n) due to sorting, where n is the number of fabrics
        
        Space complexity: O(1) as we only use constant extra space
        
        fabrics.sort(key = lambda x: x[1])

        l = 0
        r = len(fabrics) - 1
        min_diff = float('inf')
        min_diff_pair = None

        while l < r:
            sum = fabrics[l][1] + fabrics[r][1]
            if sum <= budget and abs(sum - budget) < min_diff:
                min_diff = abs(sum - budget)
                min_diff_pair = (fabrics[l][0], fabrics[r][0])

            if sum < budget:
                l += 1
            elif sum > budget:
                r -= 1
            else:
                break
        
        return min_diff_pair

"""

def find_best_fabric_pair(fabrics, budget):
    """
    Time complexity: O(n log n) due to sorting, where n is the number of fabrics
    
    Space complexity: O(1) as we only use constant extra space
    """
    fabrics.sort(key = lambda x: x[1])

    l = 0
    r = len(fabrics) - 1
    min_diff = float('inf')
    min_diff_pair = None

    while l < r:
        sum = fabrics[l][1] + fabrics[r][1]
        if sum <= budget and abs(sum - budget) < min_diff:
            min_diff = abs(sum - budget)
            min_diff_pair = (fabrics[l][0], fabrics[r][0])

        if sum < budget:
            l += 1
        elif sum > budget:
            r -= 1
        else:
            break
    
    return min_diff_pair


# PROBLEM 5: Fabric Stacks

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the stack be organized with highest rating on top or lowest rating on top?
    Q2: Are we simulating the retrieval order or just organizing for optimal retrieval?

2. Write out in plain English what you want to do:

    I need to organize fabrics so that when retrieved from a stack (LIFO - Last In, First Out),
    they come out starting with the least eco-friendly fabric. Since stacks are LIFO,
    to get the least eco-friendly first, I need to put the most eco-friendly on the bottom
    and least eco-friendly on top. This means sorting in descending order by rating,
    then returning just the fabric names in that order.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Sort fabrics by eco-friendliness rating
    sort fabrics by rating in descending order (highest to lowest)
    
    Subproblem 2: Extract fabric names in sorted order
    fabric_names <- empty list
    for each fabric in sorted fabrics:
        add fabric[0] (name) to fabric_names
    
    Subproblem 3: Return organized fabric names
    return fabric_names

4. Translate the pseudocode into Python and share your final answer:

    def organize_fabrics(fabrics):
        Time complexity: O(n log n) due to sorting, where n is the number of fabrics
        
        Space complexity: O(n) for storing the result list
        
        fabrics.sort(key = lambda x: x[1], reverse = True)
        
        return [fabric[0] for fabric in fabrics]

"""

def organize_fabrics(fabrics):
    """
    Time complexity: O(n log n) due to sorting, where n is the number of fabrics
    
    Space complexity: O(n) for storing the result list
    """
    fabrics.sort(key = lambda x: x[1], reverse = True)

    return [fabric[0] for fabric in fabrics]