# Maze Solver
> Created by Tommy Dougiamas  
> Licensed under GPLv3
### What are the rules for maze images?
This algorithm can find the shortest path through any maze that follows these rules:

- Walls marked with black pixels and paths marked with white pixels
- Walls around the entire maze
- One entrance on the top row and one exit on the bottom row

### How does the algorithm work?

- Start at the exit and label it zero.

- Move to any neighbouring cells and mark them with 1

- Move to any of the cells neighbouring the ones marked 1 and label them 2

- Continue doing this until all cells are marked

- Start from the exit of the maze and move to any neighbouring path that is marked with a number lower than the current number.

We now have the shortest path from the entrance to the exit!

### How do I use it?
To use the maze solver simply provide an image which meets the specifications listed above.

Then run 'solve.py' and supply it with the path to the image! The image will be saved in "./pics/out.jpg"

If you don't want to make an image, simply use some of the ones I have premade in the 'pics' directory
