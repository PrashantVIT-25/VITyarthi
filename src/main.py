from . import tideman
from .utils import get_candidate_index, validate_ranks

def main():

    # Read candidates
    n = int(input("Number of candidates: "))
    cand_list = []

    for _ in range(n):
        cand_list.append(input("Candidate name: "))

    tideman.initialise(cand_list)

    # Read preferences
    voter_count = int(input("Number of voters: "))

    for _ in range(voter_count):
        ranks = []
        print("Enter voter preferences: ")

        for i in range(tideman.candidate_count):
            name = input(f"Rank {i+1}: ")

            idx = get_candidate_index(name, tideman.candidates)
            if idx == -1:
                print("Invalid vote.")
                return
            
            ranks.append(idx)

        if not validate_ranks(ranks, tideman.candidate_count):
            print("Invalid vote.")
            return

        tideman.record_preferences(ranks)

    # Tideman steps
    tideman.add_pairs()
    tideman.sort_pairs()
    tideman.lock_pairs()

    print("Winner:", tideman.find_winner())

if __name__ == "__main__":
    main()
