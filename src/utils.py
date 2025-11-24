# Utility functions (for input, validation, or other helpers)
# Will be implemented as needed.

def get_candidate_index(name, candidates):
    """
    Returns the index of a candidate name.
    If not found, returns -1.
    """
    for i in range(len(candidates)):
        if candidates[i] == name:
            return i
    return -1

def validate_ranks(ranks, candidate_count):
    '''
    Check if the ranks list is valid:
    - Must contain exactly candidate_count items
    - Must not have duplicates
    - Must contain only numbers from 0 to candidate_count - 1
    '''

    if len(ranks) != candidate_count:
        return False

    # All must be unique
    if len(set(ranks)) != candidate_count:
        return False

    # All must be within allowed range
    for r in ranks:
        if not (0 <= r < candidate_count):
            return False

    return True
