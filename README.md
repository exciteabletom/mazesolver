# Maze Solver
### Created by Tommy Dougiamas  

This algorithm finds the shortest path through black and white maze images. It outputs an image with the path marked in green.


## Installing

### **Easy Installation**

Check that your python version is >=3.5 with `python3 -V`.
Also make sure that pip is installed with `pip -V`.

To install, simply run `pip install mazesolver --user` on the command line.

You can run the tool using `mazesolver`.

## What are the rules for maze images?
- Walls marked with black pixels and paths marked with white pixels

- Walls around the entire maze

- One entrance on the top row and one exit on the bottom row

*If this is confusing, check out some of the example mazes in the **pics** directory.*



## How do I use it?

You can use `mazesolver --help` to get a list of commands.

Make sure that your image meets the specifications above.

Normal usage will look something like this: `mazesolver -i path/to/input_img -o path/to/output_dir/`



## How does the algorithm work?

- Start at the entrance and label it zero.

- Move to any neighbouring cells and mark them with 1

- Move to any of the cells neighbouring the ones marked 1 and label them 2

- Continue doing this until all cells are marked

- Start from the exit of the maze and move to any neighbouring cell that == the current cell's number -1. Until we reach 0 (the entrance).

We now have the shortest path from the entrance to the exit!


> Licensed under GNU GPLv3
