import sys
import argparse
from ball_sort import BallSort
from solver import Solver
from visualizer import Visualizer

def get_test_configuration() -> list:
    """Returns a test configuration with 12 colors, 4 balls each, distributed across 14 tubes"""
    return [
        ['P', 'LP', 'PU', 'W'],    # Tube 0
        ['LG', 'B', 'O', 'G'],     # Tube 1
        ['R', 'DP', 'Y', 'DG'],    # Tube 2
        ['P', 'LP', 'PU', 'W'],    # Tube 3
        ['LG', 'B', 'O', 'G'],     # Tube 4
        ['R', 'DP', 'Y', 'DG'],    # Tube 5
        ['P', 'LP', 'PU', 'W'],    # Tube 6
        ['LG', 'B', 'O', 'G'],     # Tube 7
        ['R', 'DP', 'Y', 'DG'],    # Tube 8
        ['P', 'LP', 'PU', 'W'],    # Tube 9
        ['LG', 'B', 'O', 'G'],     # Tube 10
        ['R', 'DP', 'Y', 'DG'],    # Tube 11
        [],                         # Empty tube for moves
        []                          # Empty tube for moves
    ]

def parse_input() -> list:
    tubes = []
    visualizer = Visualizer()
    tube_count = 14  # Changed from 15 to 14 tubes
    valid_colors = {'P', 'LP', 'PU', 'W', 'LG', 'B', 'O', 'G', 'R', 'DP', 'Y', 'DG'}

    print(f"Enter the contents of {tube_count} tubes (use capital letters for colors, empty for blank tubes):")
    print("Available colors: P(ink), LP(Light Purple), PU(rple), W(hite), LG(Light Green),")
    print("                 B(lue), O(range), G(reen), R(ed), DP(Dark Purple), Y(ellow), DG(Dark Green)")
    print("Example: Enter colors separated by commas like: P,LP,PU,W")
    print("Ctrl+C to cancel input\n")

    try:
        for i in range(tube_count):
            while True:
                try:
                    tube_input = input(f"Tube {i}: ").strip().upper()
                    if not tube_input:
                        tubes.append([])
                        break

                    # Split input by commas and remove whitespace
                    colors = [c.strip() for c in tube_input.split(',')]

                    if len(colors) > 4:
                        print("Too many balls! Maximum is 4 balls per tube")
                        continue

                    if not all(c in valid_colors for c in colors):
                        print("Invalid input! Use only the available color codes separated by commas")
                        continue

                    tubes.append(colors)
                    break
                except EOFError:
                    print("\nInput terminated unexpectedly. Please try again.")
                    sys.exit(1)

        return tubes

    except KeyboardInterrupt:
        print("\nInput cancelled by user")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Ball Sort Puzzle Solver')
    parser.add_argument('--test', action='store_true', help='Run with test configuration')
    args = parser.parse_args()

    visualizer = Visualizer()

    try:
        # Get input or use test configuration
        tubes = get_test_configuration() if args.test else parse_input()

        # Create initial state
        try:
            initial_state = BallSort(tubes)
        except ValueError as e:
            print(f"Error: {str(e)}")
            return

        # Display initial state
        print("\nInitial State:")
        visualizer.display_state(initial_state)

        # Solve the puzzle
        print("\nSolving...")
        solver = Solver(initial_state)
        solution = solver.solve()

        if solution:
            visualizer.display_solution(initial_state, solution)
        else:
            print("\nNo solution found!")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()