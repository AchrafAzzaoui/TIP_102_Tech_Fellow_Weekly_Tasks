### SESSION 2, VERSION 1, Advanced Problem Set

# QUESTION 1: Count Unique Characters in a Script

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we consider only the keys of the dictionary or also validate that they have dialogue?
    Q2: How should we handle edge cases like empty dictionaries or duplicate keys?

2. Write out in plain English what you want to do:

    I need to count the number of unique character names in the script dictionary.
    Since dictionary keys are already unique by definition, I can simply count
    the number of keys in the dictionary. I'll convert the keys to a set to ensure
    uniqueness and return the length of that set.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Extract unique character names
    unique_characters <- empty set
    for each character in script keys:
        add character to unique_characters
    
    Subproblem 2: Return count of unique characters
    return length of unique_characters

4. Translate the pseudocode into Python and share your final answer:
    def count_unique_characters(script):
        unique_characters = set()
        for character in script.keys():
            unique_characters.add(character)
        
        return len(unique_characters)

"""

# QUESTION 2: Find Most Frequent Keywords

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we return keywords in any particular order when there are ties?
    Q2: What should happen if all scenes are empty or no keywords exist?

2. Write out in plain English what you want to do:

    I need to count the frequency of each keyword across all scenes and find
    the ones with the highest frequency. I'll iterate through all scenes,
    count each keyword occurrence, track the maximum frequency, then collect
    all keywords that have this maximum frequency and return them as a list.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Count frequency of all keywords
    freqs <- empty hashmap
    max_freq <- 0
    for each keywords list in scenes values:
        for each keyword in keywords:
            increment freqs[keyword]
            update max_freq to maximum of current max_freq and freqs[keyword]
    
    Subproblem 2: Find all keywords with maximum frequency
    most_frequent_keywords <- empty set
    for each keyword and freq in freqs:
        if freq equals max_freq:
            add keyword to most_frequent_keywords
    return list of most_frequent_keywords

4. Translate the pseudocode into Python and share your final answer:
    def find_most_frequent_keywords(scenes):
        freqs = {}
        max_freq = 0
        for keywords in scenes.values():
            for keyword in keywords:
                if keyword in freqs:
                    freqs[keyword] += 1
                else:
                    freqs[keyword] = 1
                max_freq = max(max_freq, freqs[keyword])
        
        most_frequent_keywords = set()
        for keyword, freq in freqs.items():
            if freq == max_freq:
                most_frequent_keywords.add(keyword)

        return list(most_frequent_keywords)

"""

# QUESTION 3: Track Scene Transitions

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we handle the case where there are fewer than 2 scenes?
    Q2: Should the queue be used for actual processing or just demonstration purposes?

2. Write out in plain English what you want to do:

    I need to simulate scene transitions using a queue data structure. I'll add
    all scenes to the queue, then process them by removing the first scene as
    the starting point, and then for each remaining scene, I'll print the
    transition from the previous scene to the current scene.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize queue with all scenes
    queue <- empty deque
    for each scene in scenes:
        add scene to queue
    
    Subproblem 2: Process transitions
    prev <- remove first scene from queue
    for remaining scenes:
        curr <- remove next scene from queue
        print transition from prev to curr
        prev <- curr

4. Translate the pseudocode into Python and share your final answer:
    from collections import deque
    def track_scene_transitions(scenes):
        queue = deque()
        for scene in scenes:
            queue.append(scene)
        prev = queue.popleft()
        for idx in range(1, len(scenes)):
            curr = queue.popleft()
            print(f"Transition from {prev} to {curr}")
            prev = curr

"""

# QUESTION 4: Organize Scene Data by Date

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we handle invalid date formats or assume all dates are well-formed?
    Q2: Should we modify the original list or return a new sorted list?

2. Write out in plain English what you want to do:

    I need to sort the scene records by their date field. Since dates are in
    YYYY-MM-DD format, they can be sorted lexicographically. I'll use Python's
    built-in sorted function with a lambda key function that extracts the first
    element (date) from each tuple for comparison.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Sort records by date field
    return sorted list of scene_records using first element as key

4. Translate the pseudocode into Python and share your final answer:
    def organize_scene_data_by_date(scene_records):
        return sorted(scene_records, key = lambda x: x[0])

"""

# QUESTION 5: Filter Scenes by Keyword

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the keyword matching be case-sensitive or case-insensitive?
    Q2: Should we match whole words only or partial matches within words?

2. Write out in plain English what you want to do:

    I need to filter out scenes that contain the specified keyword, keeping only
    scenes that do not contain the keyword. I'll use Python's filter function
    with a lambda function that checks if the keyword is not present in each
    scene description, then convert the result to a list.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Filter scenes that don't contain keyword
    filtered_scenes <- empty list
    for each scene in scenes:
        if keyword not in scene:
            add scene to filtered_scenes
    return filtered_scenes

4. Translate the pseudocode into Python and share your final answer:
    def filter_scenes_by_keyword(scenes, keyword):
        return list(filter(lambda x: keyword not in x, scenes))

"""