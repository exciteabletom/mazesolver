# Maze Solver
> Created by Tommy Dougiamas  
> Licensed under GPLv3
### What are the rules for maze images?
This algorithm can find the shortest path through any maze that follows these rules:

- Walls marked with black pixels and paths marked with white pixels
- Walls around the entire maze
- One entrance on the top row and one exit on the bottom row

### How does the algorithm work?

- Start at the entrance and label it zero.

- Move to any neighbouring cells and mark them with 1

- Move to any of the cells neighbouring the ones marked 1 and label them 2

- Continue doing this until all cells are marked

- Start from the exit of the maze and move to any neighbouring path that is marked with a number lower than the current number. Until we reach 0 (the entrance)

We now have the shortest path from the entrance to the exit!

### How do I use it?
To use the maze solver create an image which meets the specifications listed above (look at the example images for help).

Then run 'solve.py' and supply it with the path to your image.

The image will be saved in "pics/{image_name}_out.jpg".

If you don't want to make an image, you can use some of the premade ones.
