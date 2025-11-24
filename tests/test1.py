import unittest
import sys
import os

# Ensure the correct path is added to find modules in the 'src' directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import tideman
import utils

class TidemanCoreTest(unittest.TestCase):

    def setUp(self):
        """Initializes the Tideman system before each test run."""
        # a=0, b=1, c=2, d=3
        self.candidates = ["a","b","c","d"] 

        tideman.initialise(self.candidates)
        self.candidate_count = tideman.candidate_count

        # Access global state variables directly
        self.preference_matrix = tideman.preferences
        self.locked_edges = tideman.locked
        self.strongest_pairs = tideman.pairs

    # --- UTILITY TESTS (Corrected Names) ---

    def test_gci_valid_invalid(self):
        """Test get_candidate_index for valid and invalid names."""
        self.assertEqual(utils.get_candidate_index("c", self.candidates), 2)
        self.assertEqual(utils.get_candidate_index("e", self.candidates), -1)

    def test_vr_valid(self):
        """Test validate_ranks with a valid, non-sequential ranking."""
        # Valid ranks (indices 0, 1, 2, 3 in some order)
        self.assertTrue(utils.validate_ranks([1, 3, 0, 2], self.candidate_count))
    
    def test_vr_invalid(self):
        """Test validate_ranks against duplicates, incorrect length, and out-of-range indices."""
        # Invalid: Duplicate index (0, 0)
        self.assertFalse(utils.validate_ranks([0, 0, 1, 2], self.candidate_count))
        # Invalid: Incorrect length
        self.assertFalse(utils.validate_ranks([1, 2, 3], self.candidate_count))
        # Invalid: Index out of range (4 is outside [0, 3])
        self.assertFalse(utils.validate_ranks([0, 1, 2, 4], self.candidate_count))

    # --- TIDEMAN STEP 1: record_preferences (Corrected Name) ---

    def test_rp_single_voter(self):
        """Test recording preferences for a single voter."""
        # Ranks: a (0) > b (1) > c (2) > d (3)
        rank_prefs = [0, 1, 2, 3] 
        tideman.record_preferences(rank_prefs)
        
        # Check specific preference counts
        self.assertEqual(self.preference_matrix[0][1], 1, "a should beat b 1-0")
        self.assertEqual(self.preference_matrix[1][0], 0, "b should lose to a 0-1")
        self.assertEqual(self.preference_matrix[0][2], 1, "a should beat c 1-0")

    # --- TIDEMAN STEP 2 & 3: add_pairs and sort_pairs ---

    def test_add_and_sort_pairs(self):
        """Test that pairs are created correctly and sorted by margin."""
        # Margin Setup: (a vs b: 10 vs 2 = Margin 8) and (c vs d: 5 vs 1 = Margin 4)
        self.preference_matrix[0][1] = 10; self.preference_matrix[1][0] = 2
        self.preference_matrix[2][3] = 5; self.preference_matrix[3][2] = 1
        
        tideman.add_pairs()
        tideman.sort_pairs()
        
        # Check sorted order (descending margin: 8, 4)
        expected_sorted_pairs = [(0, 1), (2, 3)]
        self.assertListEqual(self.strongest_pairs, expected_sorted_pairs)

    # --- TIDEMAN STEP 4: lock_pairs and creates_cycle ---
    def test_lock_pairs_cycle_prevention(self):
        """Test the crucial cycle prevention logic using a classic 3-way cycle."""
        
        # 1. MANUALLY SET PREFERENCES (Correctly defines the margins)
        # The margins must be set for the lock_pairs function to work consistently.
        self.preference_matrix[0][1] = 10; self.preference_matrix[1][0] = 0
        self.preference_matrix[1][2] = 10; self.preference_matrix[2][1] = 0
        self.preference_matrix[2][0] = 10; self.preference_matrix[0][2] = 0

        # 2. POPULATE THE GLOBAL PAIRS LIST (using the instance variable linked in setUp)
        # Pairs: (a, b), (b, c), (c, a)
        # The pairs list is cleared in setUp, so we must add the pairs here.
        self.strongest_pairs.extend([(0, 1), (1, 2), (2, 0)])
        
        # 3. EXECUTE LOCKING
        tideman.lock_pairs()
        
        # 4. ASSERTIONS
        self.assertTrue(self.locked_edges[0][1], "a->b should be locked")
        self.assertTrue(self.locked_edges[1][2], "b->c should be locked")
        self.assertFalse(self.locked_edges[2][0], "c->a must be skipped to prevent cycle 0->1->2->0")
        
        # Verify no unintended edges were locked
        total_locked = sum(sum(row) for row in self.locked_edges)
        self.assertEqual(total_locked, 2, "Only two edges should have been locked.")
            
    # --- TIDEMAN STEP 5: find_winner ---

    def test_find_winner_clear_source(self):
        """Test finding the winner who has no incoming locked edges."""
        # Locked Edges: a -> b (0->1), c -> d (2->3), d -> b (3->1)
        # Chain: a has no incoming edges. All others are defeated by someone.
        self.locked_edges[0][1] = True
        self.locked_edges[2][3] = True
        self.locked_edges[3][1] = True
        
        # 'a' is the source and should win.
        self.assertEqual(tideman.find_winner(), "a")

    def test_find_winner_no_edges(self):
        """Test the edge case where no edges are locked (e.g., all ties)."""
        # Since the 'locked' matrix is all False, 'a' (index 0) is the first candidate
        # found without an incoming edge, and should be returned.
        self.assertEqual(tideman.find_winner(), "a")

if __name__ == '__main__':
    # Standard unittest execution
    unittest.main()