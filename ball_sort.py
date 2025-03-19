from typing import List, Tuple, Set, Optional
from copy import deepcopy

class Tube:
    def __init__(self, balls: List[str], max_size: int = 4):
        self.balls = balls
        self.max_size = max_size

    def can_push(self, ball: Optional[str]) -> bool:
        if ball is None or len(self.balls) >= self.max_size:
            return False
        return len(self.balls) == 0 or self.balls[-1] == ball

    def push(self, ball: Optional[str]) -> None:
        if ball is not None and self.can_push(ball):
            self.balls.append(ball)

    def pop(self) -> Optional[str]:
        if self.balls:
            return self.balls.pop()
        return None

    def is_complete(self) -> bool:
        return len(self.balls) == self.max_size and all(b == self.balls[0] for b in self.balls)

    def is_empty(self) -> bool:
        return len(self.balls) == 0

    def peek(self) -> Optional[str]:
        return self.balls[-1] if self.balls else None

    def __str__(self) -> str:
        return str(self.balls)

class BallSort:
    def __init__(self, tubes: List[List[str]]):
        self.tubes = [Tube(t) for t in tubes]
        self.validate_initial_state()

    def validate_initial_state(self) -> None:
        # Count total balls of each color
        color_count = {}
        for tube in self.tubes:
            for ball in tube.balls:
                color_count[ball] = color_count.get(ball, 0) + 1

        # Each color should appear exactly 4 times
        max_colors = 12  # Maximum number of colors allowed
        if len(color_count) > max_colors:
            raise ValueError(f"Too many colors! Maximum allowed is {max_colors} colors")

        for color, count in color_count.items():
            if count != 4:
                raise ValueError(f"Invalid initial state: Color {color} appears {count} times (should be 4)")

    def is_solved(self) -> bool:
        return all(t.is_empty() or t.is_complete() for t in self.tubes)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        moves = []
        for i in range(len(self.tubes)):
            for j in range(len(self.tubes)):
                if i != j and self.is_valid_move(i, j):
                    moves.append((i, j))
        return moves

    def is_valid_move(self, from_idx: int, to_idx: int) -> bool:
        if from_idx == to_idx:
            return False

        from_tube = self.tubes[from_idx]
        to_tube = self.tubes[to_idx]

        if from_tube.is_empty() or to_tube.is_complete():
            return False

        if from_tube.is_complete():
            return False

        return to_tube.can_push(from_tube.peek())

    def make_move(self, from_idx: int, to_idx: int) -> None:
        if self.is_valid_move(from_idx, to_idx):
            ball = self.tubes[from_idx].pop()
            self.tubes[to_idx].push(ball)

    def clone(self):
        return deepcopy(self)

    def get_state_hash(self) -> str:
        return "|".join("".join(t.balls) for t in self.tubes)