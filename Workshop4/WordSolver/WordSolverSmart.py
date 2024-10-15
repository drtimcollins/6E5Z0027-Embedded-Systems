import WordSolver                  # Import WordSolver module

s = WordSolver.Solver()            # Create a Solver object
N = s.play()                       # Play a single game
print(f"That took {N} guesses.")   # Report number of guesses taken