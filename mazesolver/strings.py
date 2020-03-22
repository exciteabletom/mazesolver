## strings.py - Tommy Dougiamas
# This file contains all static strings

help_message = """\
Valid Commands
---------------
-h, --help    -  Prints this help page and exits
-v, --version -  Prints the version of the program and exits
--maze-rules  -  Prints the rules for maze images

-i, --input   -  Input maze file (required)
-o, --output  -  Output directory

Example Usages 
---------------
mazesolver -i path/to/maze.jpg -o path/to/dir/
mazesolver -i path/to/maze.jpg

Contact Info
---------------
Email: tom@digitalnook.net
Github: https://github.com/exciteabletom

Licensed under GPLv3: https://www.gnu.org/licenses/gpl-3.0.en.html \
"""
maze_rules = """\
What are the rules for maze images?
---------------

- Walls marked with black pixels and paths marked with white pixels

- Walls around the entire maze

- One entrance on the top row and one exit on the bottom row
 
Check out some of the example mazes at https://github.com/exciteabletom/mazesolver/tree/master/pics \
"""

version = "2.0.1"
version_long = f"mazesolver{version}"
