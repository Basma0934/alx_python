def best_score(a_dictionary):
    """Returning a key with the biggest integer value."""
    if a_dictionary == {} or a_dictionary == None:
        return None
    else:
        BiggestValue = max(list(a_dictionary.values()))
        for key in a_dictionary:
            if a_dictionary[key] == BiggestValue:
                thebest_score = key
        return thebest_score
    



