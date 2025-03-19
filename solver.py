from typing import List, Set, Optional, Tuple
from ball_sort import BallSort

class Solver:
    def __init__(self, initial_state: BallSort):
        self.initial_state = initial_state
        self.visited_states: Set[str] = set()
        self.solution: List[Tuple[int, int]] = []

    def solve(self) -> Optional[List[Tuple[int, int]]]:
        if self._solve_recursive(self.initial_state):
            return self.solution
        return None

    def _solve_recursive(self, state: BallSort) -> bool:
        if state.is_solved():
            return True

        state_hash = state.get_state_hash()
        if state_hash in self.visited_states:
            return False

        self.visited_states.add(state_hash)
        valid_moves = state.get_valid_moves()

        for from_idx, to_idx in valid_moves:
            new_state = state.clone()
            new_state.make_move(from_idx, to_idx)
            
            self.solution.append((from_idx, to_idx))
            if self._solve_recursive(new_state):
                return True
            self.solution.pop()

        return False
