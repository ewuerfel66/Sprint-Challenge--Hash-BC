#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Insert (weight, index) into hash table
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    # Iterate through hash table
    for weight in weights:
        # Find the counterweight
        diff = limit - weight

        # Exception: weight == diff
        if weight == diff:
            # Instantiate indices
            indices = []

            for i in range(length): # O(n)
                if weights[i] == weight:
                    indices.append(i)
                    
            indices.reverse()

            return indices

        # See if the counterpart exists in the ht
        elif hash_table_retrieve(ht, diff) != None:
            # It does! Retrieve the values
            indices = [hash_table_retrieve(ht, weight), hash_table_retrieve(ht, diff)]
            
            # Sort it
            if indices[0] < indices[1]:
                indices = [indices[1], indices[0]]
            
            return indices        

    # If we make it through the for loop, return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
