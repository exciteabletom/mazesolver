# Maze Solver
> Created by Tommy Dougiamas  
> Licensed under GNU GPLv3

This algorithm finds the shortest path through black and white maze images. It outputs an image with the path marked in red.


### What are the rules for maze images?
- Walls marked with black pixels and paths marked with white pixels

- Walls around the entire maze

- One entrance on the top row and one exit on the bottom row

If this is confusing, check out some of the example mazes in the pics directory.

### How do I use it?

To use the maze solver create an image which meets the specifications listed above.

Then run 'solve.py' and supply it with the path to your image.

The image will be saved in "pics/{image_name}_out.jpg".


### How does the algorithm work?

- Start at the entrance and label it zero.

- Move to any neighbouring cells and mark them with 1

- Move to any of the cells neighbouring the ones marked 1 and label them 2

- Continue doing this until all cells are marked

- Start from the exit of the maze and move to any neighbouring path that is marked with a number lower than the current number. Until we reach 0 (the entrance)

We now have the shortest path from the entrance to the exit!

