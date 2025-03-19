from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from ball_sort import BallSort
from typing import List, Tuple, Optional

class Visualizer:
    def __init__(self):
        self.console = Console()
        self.color_map = {
            'R': '[red]●[/red]',
            'B': '[blue]●[/blue]',
            'G': '[green]●[/green]',
            'Y': '[yellow]●[/yellow]',
            'P': '[magenta]●[/magenta]',
            'C': '[cyan]●[/cyan]',
            'W': '[white]●[/white]',
            'O': '[orange1]●[/orange1]',
            'V': '[purple]●[/purple]',
            'M': '[magenta2]●[/magenta2]'
        }

    def display_state(self, state: BallSort, step: Optional[int] = None):
        table = Table(show_header=False, box=None)

        # Add columns for each tube
        for _ in range(len(state.tubes)):
            table.add_column(justify="center", width=3)

        # Create rows (from bottom to top)
        max_height = 4  # Maximum number of balls in a tube
        for row in range(max_height - 1, -1, -1):
            row_data = []
            for tube in state.tubes:
                if row < len(tube.balls):
                    color = tube.balls[row]
                    row_data.append(self.color_map.get(color, '○'))
                else:
                    row_data.append(' ')
            table.add_row(*row_data)

        # Add tube numbers
        tube_numbers = [str(i) for i in range(len(state.tubes))]
        table.add_row(*tube_numbers)

        title = "Ball Sort Puzzle"
        if step is not None:
            title += f" - Step {step}"

        self.console.print(Panel(table, title=title))

    def display_solution(self, initial_state: BallSort, moves: List[Tuple[int, int]]):
        self.console.clear()
        self.console.print("[bold green]Solution Found![/bold green]")
        self.console.print(f"Total moves: {len(moves)}\n")

        current_state = initial_state.clone()
        self.display_state(current_state, 0)

        with Progress() as progress:
            task = progress.add_task("[cyan]Showing solution...", total=len(moves))

            for step, (from_idx, to_idx) in enumerate(moves, 1):
                self.console.print(f"\nMove {step}: Tube {from_idx} → Tube {to_idx}")
                current_state.make_move(from_idx, to_idx)
                self.display_state(current_state, step)
                progress.update(task, advance=1)

    def display_error(self, message: str):
        self.console.print(f"[bold red]Error:[/bold red] {message}")