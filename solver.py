from typing import List, Set, Optional, Tuple
from ball_sort import BallSort
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

class Solver:
    def __init__(self, initial_state: BallSort):
        self.initial_state = initial_state
        self.visited_states: Set[str] = set()
        self.solution: List[Tuple[int, int]] = []
        self.start_time = time.time()
        self.nodes_explored = 0
        self.max_depth = 0

    def solve(self) -> Optional[List[Tuple[int, int]]]:
        logging.info("Starting puzzle solution search...")
        if self._solve_recursive(self.initial_state, depth=0):
            elapsed_time = time.time() - self.start_time
            logging.info(f"Solution found! Time: {elapsed_time:.2f}s, "
                        f"Nodes explored: {self.nodes_explored}, "
                        f"Max depth: {self.max_depth}")
            return self.solution
        logging.warning("No solution found!")
        return None

    def _solve_recursive(self, state: BallSort, depth: int = 0) -> bool:
        if state.is_solved():
            return True

        if depth > self.max_depth:
            self.max_depth = depth
            if depth % 10 == 0:  # Log progress every 10 levels
                logging.info(f"Reached depth {depth}, "
                           f"Visited states: {len(self.visited_states)}, "
                           f"Nodes explored: {self.nodes_explored}")

        state_hash = state.get_state_hash()
        if state_hash in self.visited_states:
            return False

        self.visited_states.add(state_hash)
        self.nodes_explored += 1
        valid_moves = state.get_valid_moves()

        # Sort moves to prioritize promising ones (moving to empty tubes last)
        valid_moves.sort(key=lambda move: len(state.tubes[move[1]].balls) > 0)

        for from_idx, to_idx in valid_moves:
            new_state = state.clone()
            new_state.make_move(from_idx, to_idx)

            self.solution.append((from_idx, to_idx))
            if self._solve_recursive(new_state, depth + 1):
                return True
            self.solution.pop()

        return False