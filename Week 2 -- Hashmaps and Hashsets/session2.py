
### SESSION 1, VERSION 1, Advanced Problem Set


# QUESTION 1: Balanced Art Collection

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: What is the expected time complexity?
    Q2: What is the expected space complexity?

2. Write out in plain English what you want to do:

    I will create a TreeMap frequency counter that maps art_pieces to their
    frequency in art_pieces -- this will ensure sorted order.
    Then, I will create a sliding window over the keys and values of this 
    treemap. idx0 will always be 1 less than idx2. If the keys at idx0 and idx1
    have a difference of 1, then we will store the max length as max of curr max and
    val at idx0 + val at idx1.
    Return max length.



3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Find the frequency of each art piece value in sorted order
    
    freqs <- empty treemap 
    for art piece in art pieces 
        increment freq of art piece in freqs

    Subproblem 2: Find the longest subsequence with a diff of 1 between min and max val
    max_subseq_length <- 0
    vals, freqs = list of freqs keys, list of freqs vals
    idx1 <- 0
    idx2 <- 1
    while True then
        if idx1 > length of vals - 1 or idx2 > length of vals - 1 then
            exit while loop
        else if diff of vals[idx2] and vals[idx1] greater than 1 then
            increment both idx1 and idx2
        else then
            curr_candidate <- sum of freqs[idx1] and freqs[idx2]
            max_subseq_length <- max of max_subseq_length and curr_candidate
            increment both idx1 and idx2



4. Translate the pseudococde into Python and share your final answer:
    def find_balanced_subsequence(art_pieces):
        from sortedcontainers import SortedDict
        freqs = SortedDict()
        for art_piece in art_pieces:
            freqs[art_piece] = 1 + freqs.get(art_piece, 0)

        max_subseq_length = 0
        vals, freqs = list(freqs.keys()), list(freqs.values())
        idx_1 = 0
        idx_2 = 1
        while True:
            if idx_1 > len(vals) - 1 or idx_2 > len(vals) - 1:
                break
            elif vals[idx_2] - vals[idx_1] > 1:
                idx_1 += 1
                idx_2 += 1
            else:
                max_subseq_length = max(max_subseq_length, freqs[idx_1] + freqs[idx_2])
                idx_1 += 1
                idx_2 += 1
        return max_subseq_length



"""

# QUESTION 2: Verifying Authenticity

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: What defines an authentic collection in this context?
    Q2: Are there any edge cases to consider (empty arrays, negative numbers)?

2. Write out in plain English what you want to do:

    I need to verify if a collection is authentic by checking two conditions:
    First, the length of the array should equal the maximum value plus 1.
    Second, the maximum value should appear exactly twice in the collection.
    If both conditions are met, return True, otherwise False.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Find the maximum value in the collection
    max_val <- maximum value in art_pieces
    
    Subproblem 2: Check authenticity conditions
    if length of art_pieces != max_val + 1 then
        return False
    else if count of max_val in art_pieces != 2 then
        return False
    else then
        return True

4. Translate the pseudocode into Python and share your final answer:

    def is_authentic_collection(art_pieces):
        max_val = max(art_pieces)
        if len(art_pieces) != max_val + 1 or art_pieces.count(max_val) != 2:
            return False
        else:
            return True
"""


    

# QUESTION 3: Gallery Wall

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: What should happen when we encounter a duplicate piece?
    Q2: Should empty sublists be included in the final result?

2. Write out in plain English what you want to do:

    I need to organize art pieces into sublists where each sublist contains unique pieces.
    When I encounter a duplicate piece, I start a new sublist with that piece.
    I'll use a set to track which pieces I've seen in the current sublist.
    When I find a duplicate, I clear the set and start fresh with the duplicate piece.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize data structures
    unique_2d <- list with one empty sublist
    visited <- empty set
    
    Subproblem 2: Process each piece in collection
    for each piece in collection:
        if piece not in visited then
            add piece to current sublist
            add piece to visited set
        else then
            create new empty sublist
            add piece to new sublist
            clear visited set
            add piece to visited set

4. Translate the pseudocode into Python and share your final answer:
    def organize_exhibition(collection):
        unique_2d = [[]]
        visited = set()
        for piece in collection:
            if piece not in visited:
                unique_2d[-1].append(piece)
                visited.add(piece)
            else:
                unique_2d.append([])
                unique_2d[-1].append(piece)
                visited.clear()
                visited.add(piece)
        return unique_2d

"""



# QUESTION 4: Gallery Subdomain Traffic

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: How should we handle the subdomain parsing (e.g., counting all subdomains)?
    Q2: What format should the output be in?

2. Write out in plain English what you want to do:

    I need to count the visits for each subdomain by parsing the input strings.
    For each input, I'll extract the count and domain, then split the domain
    into all possible subdomains. I'll accumulate the counts for each subdomain
    and return the results in the specified format.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Parse each entry and count visits for all subdomains
    domain_counts <- empty hashmap
    for each cpdomain in cpdomains:
        count_str, domain <- split cpdomain by space
        count <- convert count_str to integer
        subdomains <- split domain by dots
        
        for each index in range of subdomains length:
            subdomain <- join subdomains from index to end with dots
            add count to domain_counts[subdomain]
    
    Subproblem 2: Format output
    result <- empty list
    for each domain and count in domain_counts:
        append formatted string to result
    return result

4. Translate the pseudocode into Python and share your final answer:

def subdomain_visits(cpdomains):
    domain_counts = {}
    for cpdomain in cpdomains:
        count_str, domain = cpdomain.split(" ")
        count = int(count_str)
        subdomains = domain.split('.')

        for idx in range(len(subdomains)):
            subdomain = ".".join(subdomains[idx:])
            domain_counts[subdomain] = domain_counts.get(subdomain, 0) + count
        
    result = []
    for domain, count in domain_counts.items():
        result.append(f"{count} {domain}")
    return result

"""

# QUESTION 5: Beautiful Collection

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: How do we define the beauty of a substring?
    Q2: Should we consider all possible substrings or only contiguous ones?

2. Write out in plain English what you want to do:

    I need to calculate the total beauty sum of all substrings in a collection.
    For each substring, I'll count the frequency of each character, then calculate
    the beauty as the difference between maximum and minimum frequencies.
    I'll sum up all these beauty values for every possible substring.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize total beauty counter
    total_beauty <- 0
    n <- length of collection
    
    Subproblem 2: Generate all possible substrings
    for i from 0 to n:
        for j from i+1 to n+1:
            substring <- collection[i:j]
            
    Subproblem 3: Calculate beauty for each substring
    char_count <- empty hashmap
    for each char in substring:
        increment count of char in char_count
    frequencies <- list of values in char_count
    max_freq <- maximum of frequencies
    min_freq <- minimum of frequencies
    beauty <- max_freq - min_freq
    total_beauty <- total_beauty + beauty

4. Translate the pseudocode into Python and share your final answer:
    def beauty_sum(collection):
        total_beauty = 0
        n = len(collection)
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = collection[i:j]
                char_count = {}
                for char in substring:
                    char_count[char] = char_count.get(char, 0) + 1
                frequencies = list(char_count.values())
                max_freq = max(frequencies)
                min_freq = min(frequencies)

                beauty = max_freq - min_freq
                total_beauty += beauty
        
        return total_beauty


"""



