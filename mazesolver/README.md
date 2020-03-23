# Main project Directory
Contains the main package that is built by `../setup.py`   

- Typical workflow looks like this:
   `
   __main__.py  # Run by user from command-line
   |
   ----->maze_matrix=load_maze.load(input_path)
	   |
	   V
	   -->solution=solve.solve(maze_matrix) 
	   |
	   V
	   -->create_final_image.create(solution, output_directory)
   `
      

- `g.py`
   - Stores all variables that need to be manipulated by multiple files. (global variables)    

- `__main__.py`
   - Handles all command line args
   - Calls all the functions that solve the maze using information from those args   
   - The entrypoint `main()` is used by the cli tool

- `load_maze.py`
   - Contains functions that convert a maze image into a matrix    
   - Entrypoint is called `load()`. It takes a string path to a maze image

- `solve.py`
   - Contains functions that convert a maze matrix into a list of cells representing a path through that maze
   - Entrypoint is called `solve()`. It uses the variable `g.maze` as input.   

- `create_final_image.py`
   - Contains functions that create an image based on a list of cells, an input image, and an output location
   - Entrypoint is called `create()`.


