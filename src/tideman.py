MAX = 9

# Global Variables
preferences = []
locked = []
candidates = []
pairs = []

candidate_count = 0
pair_count = 0

def initialise(cand_list):

    # Sets up the election based on a list of candidate names.

    global candidates, preferences, locked, pairs, candidate_count, pair_count

    candidates = cand_list
    candidate_count = len(candidates)

    # Build fresh matrices
    preferences = [[0]*candidate_count for _ in range(candidate_count)]
    locked = [[False]*candidate_count for _ in range(candidate_count)]

    pairs = []
    pair_count = 0

def record_preferences(ranks):

    global preferences

    for i in range(candidate_count):
        for j in range(i+1, candidate_count):
            preferred = ranks[i]
            less_preferred = ranks[j]
            preferences[preferred][less_preferred] += 1

def add_pairs():

    global pairs, pair_count

    for i in range(candidate_count):
        for j in range(candidate_count):
            if i == j:
                continue

            if preferences[i][j] > preferences[j][i]:
                pairs.append((i,j))
                pair_count += 1

def sort_pairs():

    pairs.sort(
        key = lambda p: preferences[p[0]][p[1]] - preferences[p[1]][p[0]],
        reverse = True # strongest diffs -> smallest diffs
    )

def creates_cycle(winner, loser):
    if winner == loser:
        return True

    for i in range(candidate_count):
        if locked[loser][i]:
            if creates_cycle(winner, i):
                return True
    return False

def lock_pairs():

    global locked

    for (winner, loser) in pairs:
        if not creates_cycle(winner, loser): #creates_cycle
            locked[winner][loser] = True

def find_winner():

    for i in range(candidate_count):
        source = True

        for j in range(candidate_count):
            if locked[j][i]:
                source = False
                break
        if source:
            return candidates[i]

    return None
