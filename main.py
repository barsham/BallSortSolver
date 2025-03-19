from ball_sort import BallSort
from solver import Solver
from visualizer import Visualizer
import sys

def parse_input() -> list:
    tubes = []
    visualizer = Visualizer()
    tube_count = 15

    print(f"Enter the contents of {tube_count} tubes (use capital letters for colors, empty for blank tubes):")
    print("Available colors: R(ed), B(lue), G(reen), Y(ellow), P(ink), C(yan), W(hite), O(range), V(iolet), M(agenta)")
    print("Example: RGGB or press Enter for empty tube")
    print("Ctrl+C to cancel input\n")

    try:
        for i in range(tube_count):
            while True:
                try:
                    tube_input = input(f"Tube {i}: ").strip().upper()
                    if not tube_input:
                        tubes.append([])
                        break
                    if len(tube_input) > 4:
                        print("Too many balls! Maximum is 4 balls per tube")
                        continue
                    if not all(c in "RBGYPCWOVM" for c in tube_input):
                        print("Invalid input! Use only R,B,G,Y,P,C,W,O,V,M for colors")
                        continue
                    tubes.append(list(tube_input))
                    break
                except EOFError:
                    print("\nInput terminated unexpectedly. Please try again.")
                    sys.exit(1)

        return tubes

    except KeyboardInterrupt:
        print("\nInput cancelled by user")
        sys.exit(1)

def main():
    visualizer = Visualizer()

    try:
        # Get input
        tubes = parse_input()

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