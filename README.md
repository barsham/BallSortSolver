# 🧩 Ball Sort Puzzle Solver

A Python-based solution for the Ball Sort Puzzle game, implementing a bruteforce algorithm to solve puzzles with up to 15 tubes. The solver uses a depth-first search approach to find the optimal sequence of moves to sort colored balls into their respective tubes.

![Ball Sort Puzzle](generated-icon.png)

## ✨ Features

- 🎯 Solves Ball Sort puzzles with up to 14 tubes (12 colors + 2 empty tubes)
- 🎨 Supports 12 different colors with rich terminal visualization
- 🔄 Interactive input for custom puzzle configurations
- 📊 Step-by-step solution display with move counter
- 🎮 Test mode with pre-configured puzzle
- 🎯 Validates puzzle configurations for solvability
- 🖥️ Beautiful terminal UI using Rich library

## 🛠️ Requirements

- Python 3.11 or higher
- Rich library for terminal visualization
- Terminal with ANSI color support

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/barsham/BallSortSolver.git
cd BallSortSolver
```

2. Install the required packages:
```bash
pip install rich
```

## 🎮 Usage

### Running with Test Configuration

To run the solver with a pre-configured test puzzle:

```bash
python main.py --test
```

### Running with Custom Configuration

To solve your own puzzle:

```bash
python main.py
```

Follow the prompts to input the contents of each tube. Use the following color codes:

- P: Pink
- LP: Light Purple
- PU: Purple
- W: White
- LG: Light Green
- B: Blue
- O: Orange
- G: Green
- R: Red
- DP: Dark Purple
- Y: Yellow
- DG: Dark Green

Enter colors separated by commas, for example: `P,LP,PU,W`

For empty tubes, just press Enter without typing anything.

## 🧮 Algorithm

The solver uses a depth-first search with backtracking to find the solution:

1. Validates the initial state to ensure:
   - Each color appears exactly 4 times
   - Maximum of 12 different colors
   - Maximum of 4 balls per tube

2. For each state:
   - Checks if the puzzle is solved (all tubes either empty or containing 4 balls of the same color)
   - Finds all valid moves
   - Tries each valid move recursively
   - Backtracks if a move leads to a dead end
   - Keeps track of visited states to avoid cycles

3. A move is considered valid when:
   - Source tube is not empty
   - Destination tube is not full
   - The top ball of the source tube can be placed on the destination tube
   - The move doesn't undo the previous state

## 🎨 Color Codes

The puzzle uses the following color codes:

| Code | Color | Description |
|------|-------|-------------|
| P | Pink | Magenta colored ball |
| LP | Light Purple | Light purple colored ball |
| PU | Purple | Deep purple colored ball |
| W | White | White colored ball |
| LG | Light Green | Light green colored ball |
| B | Blue | Blue colored ball |
| O | Orange | Orange colored ball |
| G | Green | Green colored ball |
| R | Red | Red colored ball |
| DP | Dark Purple | Dark purple colored ball |
| Y | Yellow | Yellow colored ball |
| DG | Dark Green | Dark green colored ball |

## 📝 Example

Initial state:
```
Tube 0: P,LP,PU,W
Tube 1: LG,B,O,P
Tube 2: O,G,DG,W
...
```

The solver will display:
1. The initial state visualization
2. Step-by-step moves with tube numbers
3. The final solved state

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your PR:
- Includes a clear description of the changes
- Updates documentation as needed
- Adds tests for new features
- Follows the existing code style

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the mobile game "Ball Sort Puzzle"
- Terminal UI powered by [Rich](https://github.com/Textualize/rich)

---

Made with ❤️ by [Barsham](https://github.com/barsham) using [Replit](https://replit.com/) in 20 minutes

Don't forget to ⭐ this repository if you found it helpful!
