input = """
#############################################################################################################################################
#.......#.....#.......#.....#...#.......###...###...###...#...#...###...#...............###...###...........#.............#...#.....#.....###
#.#####.#.###.#.#####.#.###.#.#.#.#####.###.#.###.#.###.#.#.#.#.#.###.#.#.#############.###.#.###.#########.#.###########.#.#.#.###.#.###.###
#.....#.#...#.#.....#.#.#...#.#.#.....#.#...#.#...#.....#...#...#...#.#.#.#...#.........#...#.#...#.........#.......#.....#.#...#...#...#...#
#####.#.###.#.#####.#.#.#.###.#.#####.#.#.###.#.###################.#.#.#.#.#.#.#########.###.#.###.###############.#.#####.#####.#####.###.#
#.....#...#.#.###...#...#...#.#.#.....#.#...#.#...........#.........#.#.#...#.#.#...#...#...#...#...#.......#...###.#...#...#.....#...#.#...#
#.#######.#.#.###.#########.#.#.#.#####.###.#.###########.#.#########.#.#####.#.#.#.#.#.###.#####.###.#####.#.#.###.###.#.###.#####.#.#.#.###
#.#.....#...#...#.........#.#.#.#.....#...#.#.#.....###...#...#...#...#.###...#...#...#...#.....#.###.....#...#...#.#...#.#...#...#.#...#...#
#.#.###.#######.#########.#.#.#.#####.###.#.#.#.###.###.#####.#.#.#.###.###.#############.#####.#.#######.#######.#.#.###.#.###.#.#.#######.#
#...###.....#...###...###.#.#.#.#...#...#...#...#...#...#.....#.#...#...#...#.............###...#.....###.......#.#.#.#...#...#.#...#.......#
###########.#.#####.#.###.#.#.#.#.#.###.#########.###.###.#####.#####.###.###.###############.#######.#########.#.#.#.#.#####.#.#####.#######
#.......###.#.###...#...#.#...#...#.###.........#...#...#.....#.#...#.....#...#...###.........#.......#...###...#...#.#.#...#...#...#.#.....#
#.#####.###.#.###.#####.#.#########.###########.###.###.#####.#.#.#.#######.###.#.###.#########.#######.#.###.#######.#.#.#.#####.#.#.#.###.#
#.....#.....#...#.....#.#.#.........#...#...#...#...#...#.....#.#.#.....#...#...#...#.........#.....#...#...#...#.....#.#.#.......#...#.#...#
#####.#########.#####.#.#.#.#########.#.#.#.#.###.###.###.#####.#.#####.#.###.#####.#########.#####.#.#####.###.#.#####.#.#############.#.###
#...#.......#...#...#.#.#.#.###...#...#...#...#...#...#...#...#...#.....#...#.....#.....###...#.....#.....#...#.#.......#.........#...#.#...#
#.#.#######.#.###.#.#.#.#.#.###.#.#.###########.###.###.###.#.#####.#######.#####.#####.###.###.#########.###.#.#################.#.#.#.###.#
#.#...###...#...#.#...#...#...#.#.#.........#...###.#...#...#.....#...#.....#...#.#.....#...#...###...###...#.#.#.................#.#.#.#...#
#.###.###.#####.#.###########.#.#.#########.#.#####.#.###.#######.###.#.#####.#.#.#.#####.###.#####.#.#####.#.#.#.#################.#.#.#.###
#...#...#...#...#...........#.#.#.#...#...#.#.#...#.#.....#.......#...#...#...#.#.#.....#...#.#...#.#...#...#.#.#...............###.#...#...#
###.###.###.#.#############.#.#.#.#.#.#.#.#.#.#.#.#.#######.#######.#####.#.###.#.#####.###.#.#.#.#.###.#.###.#.###############.###.#######.#
###...#.....#...#...###...#.#.#.#...#...#.#.#.#.#.#.#...#...#.....#.....#...#...#...#...#...#...#.#...#...#...#.#.........#...#.....#.......#
#####.#########.#.#.###.#.#.#.#.#########.#.#.#.#.#.#.#.#.###.###.#####.#####.#####.#.###.#######.###.#####.###.#.#######.#.#.#######.#######
#...#.......#...#.#...#.#.#.#.#.........#.#.#...#.#.#.#...###...#.....#.....#.....#.#...#...#.....###.....#.###.#.#.....#...#.......#.#...###
#.#.#######.#.###.###.#.#.#.#.#########.#.#.#####.#.#.#########.#####.#####.#####.#.###.###.#.###########.#.###.#.#.###.###########.#.#.#.###
#.#.#...#...#...#...#.#.#.#.#.###.......#.#.....#...#.......###.....#...#...#.....#...#.###.#.#...###...#.#.....#.#.#...###...#...#...#.#...#
#.#.#.#.#.#####.###.#.#.#.#.#.###.#######.#####.###########.#######.###.#.###.#######.#.###.#.#.#.###.#.#.#######.#.#.#####.#.#.#.#####.###.#
#.#...#.#.....#.....#...#...#...#.......#.....#...#.........#.......#...#...#.......#.#.#...#.#.#...#.#.#.#.......#.#.....#.#.#.#.....#...#.#
#.#####.#####.#################.#######.#####.###.#.#########.#######.#####.#######.#.#.#.###.#.###.#.#.#.#.#######.#####.#.#.#.#####.###.#.#
#.....#.#...#.................#.###...#.#.....#...#.........#...#...#...#...#.......#.#...#...#...#.#.#.#.#.#.......#.....#.#.#.#.....#...#.#
#####.#.#.#.#################.#.###.#.#.#.#####.###########.###.#.#.###.#.###.#######.#####.#####.#.#.#.#.#.#.#######.#####.#.#.#.#####.###.#
#...#.#...#.....#.............#...#.#.#.#.#...#.....#.......###...#...#.#.#...#.....#.....#.#...#.#...#...#...#.....#.....#.#.#.#.#...#...#.#
#.#.#.#########.#.###############.#.#.#.#.#.#.#####.#.###############.#.#.#.###.###.#####.#.#.#.#.#############.###.#####.#.#.#.#.#.#.###.#.#
#.#.#.........#.#.............#...#.#.#.#.#.#.#...#.#.#...###...#...#.#.#.#.###...#.#...#.#.#.#.#.....#.........###.#.....#.#.#.#.#.#.#...#.#
#.#.#########.#.#############.#.###.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#####.#.#.#.#.#.#.#.#####.#.###########.#.#####.#.#.#.#.#.#.###.#
#.#...#.......#...............#.....#.#.#.#.#.#.#.#.#.#.#...#.#.#.#.#.#...#...#...#.#.#.#.#.#.#...#...#...#...#...#...#...#.#.#.#...#...#...#
#.###.#.#############################.#.#.#.#.#.#.#.#.#.###.#.#.#.#.#.#######.#.###.#.#.#.#.#.###.#.#####.#.#.#.#.#####.#.#.#.#.#########.###
#...#.#.........#.....#.....#.......#...#.#.#.#.#...#.#.#...#.#.#.#.#.#...#...#...#.#.#.#.#.#.#...#...###...#.#.#.###...#...#...#...#...#...#
###.#.#########.#.###.#.###.#.#####.#####.#.#.#.#####.#.#.###.#.#.#.#.#.#.#.#####.#.#.#.#.#.#.#.#####.#######.#.#.###.###########.#.#.#.###.#
#...#.###...#...#.#...#...#...#.....#.....#.#.#.....#...#...#.#...#.#...#.#...#...#...#...#.#.#.......#.......#.#.....#.......#...#...#.....#
#.###.###.#.#.###.#.#####.#####.#####.#####.#.#####.#######.#.#####.#####.###.#.###########.#.#########.#######.#######.#####.#.#############
#...#.....#...#...#.#...#.#.....#...#.....#.#.#...#...#.....#.#.....#...#.#...#.........#...#.#.......#.........#.....#.....#.#.#.....#.....#
###.###########.###.#.#.#.#.#####.#.#####.#.#.#.#.###.#.#####.#.#####.#.#.#.###########.#.###.#.#####.###########.###.#####.#.#.#.###.#.###.#
###...#...#...#...#...#...#...#...#.....#.#.#.#.#.#...#...#...#.....#.#.#.#...#...#...#.#...#.#...#...###...#.....###...#...#.#...#...#.#...#
#####.#.#.#.#.###.###########.#.#######.#.#.#.#.#.#.#####.#.#######.#.#.#.###.#.#.#.#.#.###.#.###.#.#####.#.#.#########.#.###.#####.###.#.###
#...#.#.#.#.#.#...#.........#...#.......#...#.#.#.#.....#.#.#.......#.#.#...#.#.#.#.#.#.###...#...#.......#.#.........#.#.#...#...#.....#...#
#.#.#.#.#.#.#.#.###.#######.#####.###########.#.#.#####.#.#.#.#######.#.###.#.#.#.#.#.#.#######.###########.#########.#.#.#.###.#.#########.#
#.#.#...#...#...###.......#.#...#...........#.#.#.#...#.#.#.#...#...#.#.....#...#.#.#.#.#.....#.#.....#...#.#.........#...#.#...#.#...#...#.#
#.#.#####################.#.#.#.###########.#.#.#.#.#.#.#.#.###.#.#.#.###########.#.#.#.#.###.#.#.###.#.#.#.#.#############.#.###.#.#.#.#.#.#
#.#.#...###...............#...#...#.......#.#.#.#.#.#.#.#...#...#.#.#.....###...#...#...#...#...#.#...#.#.#.#.............#.#.###...#.#.#...#
#.#.#.#.###.#####################.#.#####.#.#.#.#.#.#.#.#####.###.#.#####.###.#.###########.#####.#.###.#.#.#############.#.#.#######.#.#####
#.#...#...#.....................#.#.....#...#...#.#.#.#.....#.....#.....#.....#.#...........#.....#.....#.#...............#.#.......#.#...###
#.#######.#####################.#.#####.#########.#.#.#####.###########.#######.#.###########.###########.#################.#######.#.###.###
#.......#.###...#.........#.....#.....#...#...###...#.#...#.#...#.......#.....#.#.#...........#.......#...#...............#.........#...#...#
#######.#.###.#.#.#######.#.#########.###.#.#.#######.#.#.#.#.#.#.#######.###.#.#.#.###########.#####.#.###.#############.#############.###.#
#.......#.....#.#.......#...#.......#.#...#.#.#...###...#.#...#.#.....#...#...#.#...#...#...###.....#.#.....#...#.........#...###...###...#.#
#.#############.#######.#####.#####.#.#.###.#.#.#.#######.#####.#####.#.###.###.#####.#.#.#.#######.#.#######.#.#.#########.#.###.#.#####.#.#
#.............#.........#...#.#.....#.#.....#...#.......#.#...#.#.....#...#...#.#...#.#...#.........#.........#...#.....#...#.....#.....#.#.#
#############.###########.#.#.#.#####.#################.#.#.#.#.#.#######.###.#.#.#.#.#############################.###.#.#############.#.#.#
#...........#.....#.....#.#...#.#...#...........#...#...#...#.#.#.#...#...###...#.#.#.....#...#...#...#.........###...#.#.#.............#.#.#
#.#########.#####.#.###.#.#####.#.#.###########.#.#.#.#######.#.#.#.#.#.#########.#.#####.#.#.#.#.#.#.#.#######.#####.#.#.#.#############.#.#
#...#.....#...###.#.###...#...#...#...#...#...#.#.#.#.....#...#.#.#.#.#...#...#...#.....#...#...#...#...#.....#.#.....#...#.............#...#
###.#.###.###.###.#.#######.#.#######.#.#.#.#.#.#.#.#####.#.###.#.#.#.###.#.#.#.#######.#################.###.#.#.#####################.#####
#...#.###...#.#...#...###...#.........#.#...#.#...#...#...#.#...#.#.#...#.#.#...#.....#...###...#.....###...#.#.#.#.........#...........#...#
#.###.#####.#.#.#####.###.#############.#####.#######.#.###.#.###.#.###.#.#.#####.###.###.###.#.#.###.#####.#.#.#.#.#######.#.###########.#.#
#.....#.....#...#.....#...#.............#...#.......#.#.###...#...#...#.#.#.....#.###...#.....#.#...#.......#...#.#.#...###...#...###...#.#.#
#######.#########.#####.###.#############.#.#######.#.#.#######.#####.#.#.#####.#.#####.#######.###.#############.#.#.#.#######.#.###.#.#.#.#
#...###...........#.....#...#.............#...#.....#...#...###.......#...#...#...#...#.......#.....#.....#...#...#...#.......#.#.#...#...#.#
#.#.###############.#####.###.###############.#.#########.#.###############.#.#####.#.#######.#######.###.#.#.#.#############.#.#.#.#######.#
#.#.................#...#.#...#.............#...#...###...#.....#.........#.#.#...#.#.#...###.......#.#...#.#.#.#.............#.#.#...#.....#
#.###################.#.#.#.###.###########.#####.#.###.#######.#.#######.#.#.#.#.#.#.#.#.#########.#.#.###.#.#.#.#############.#.###.#.#####
#.#...........#...#...#.#.#...#.#...........#.....#.....#.......#.......#...#...#...#...#.....#...#...#.....#...#.#...#.......#.#.###.#.....#
#.#.#########.#.#.#.###.#.###.#.#.###########.###########.#############.#####################.#.#.###############.#.#.#.#####.#.#.###.#####.#
#...#.........#.#.#.###...###...#.............#.....#.....#.....###...#.....................#...#.....#.....#...#...#...#.....#.#.....#.....#
#####.#########.#.#.###########################.###.#.#####.###.###.#.#####################.#########.#.###.#.#.#########.#####.#######.#####
#...#.......#...#.#.#...#...###...#...........#...#...#.....#...#...#...#...................#.......#.#...#...#...#...#...#...#...#.....#...#
#.#.#######.#.###.#.#.#.#.#.###.#.#.#########.###.#####.#####.###.#####.#.###################.#####.#.###.#######.#.#.#.###.#.###.#.#####.#.#
#.#.###...#...###...#.#...#...#.#...#...#...#.....###...#...#.....#.....#...........#...#...#.#.....#...#.......#...#...#...#...#.#.......#.#
#.#.###.#.###########.#######.#.#####.#.#.#.#########.###.#.#######.###############.#.#.#.#.#.#.#######.#######.#########.#####.#.#########.#
#.#.#...#.....#...###.....#...#.......#...#.....#...#.#...#.........###.............#.#.#.#...#.......#.......#.###...#...#.....#.#.......#.#
#.#.#.#######.#.#.#######.#.###################.#.#.#.#.###############.#############.#.#.###########.#######.#.###.#.#.###.#####.#.#####.#.#
#.#.#.....#...#.#.....#...#.....#.......#.......#.#.#.#.#.........#...#...........#...#...###...#...#.#.....#.#...#.#.#.#...#...#.#.....#...#
#.#.#####.#.###.#####.#.#######.#.#####.#.#######.#.#.#.#.#######.#.#.###########.#.#########.#.#.#.#.#.###.#.###.#.#.#.#.###.#.#.#####.#####
#.#.....#.#.###.....#...#.....#.#...###...#...###.#...#.#.#.......#.#.###.....###...#.........#...#.#...#...#.....#.#.#.#.....#...#.....#...#
#.#####.#.#.#######.#####.###.#.###.#######.#.###.#####.#.#.#######.#.###.###.#######.#############.#####.#########.#.#.###########.#####.#.#
#...#...#.#...#...#.......###.#...#.........#...#.#...#.#.#.....#...#...#.#...#...###.......#.....#.......#...###...#...#...#...#...###...#.#
###.#.###.###.#.#.###########.###.#############.#.#.#.#.#.#####.#.#####.#.#.###.#.#########.#.###.#########.#.###.#######.#.#.#.#.#####.###.#
#...#...#.#...#.#.........#...#...#.......#...#...#.#...#...#...#.#.....#.#.###.#.#######S#...#...#.........#.....#...#...#...#.#.....#...#.#
#.#####.#.#.###.#########.#.###.###.#####.#.#.#####.#######.#.###.#.#####.#.###.#.#######.#####.###.###############.#.#.#######.#####.###.#.#
#.#...#...#...#.........#.#...#.....#...#...#.......###.....#.#...#.#.....#.#...#.#######.#.....#...#.........#.....#.#.#...###.....#.....#.#
#.#.#.#######.#########.#.###.#######.#.###############.#####.#.###.#.#####.#.###.#######.#.#####.###.#######.#.#####.#.#.#.#######.#######.#
#.#.#.#...#...#...#...#.#.....#.......#.....#...#.....#...#...#...#.#...#...#...#.#######.#.......###.....###...###...#...#...#...#.......#.#
#.#.#.#.#.#.###.#.#.#.#.#######.###########.#.#.#.###.###.#.#####.#.###.#.#####.#.#######.###############.#########.#########.#.#.#######.#.#
#.#.#...#.#.....#.#.#.#.#...#...#...........#.#.#.#...###.#.#...#.#...#.#.#...#.#.#######...###.......###.........#...#.....#...#...#...#...#
#.#.#####.#######.#.#.#.#.#.#.###.###########.#.#.#.#####.#.#.#.#.###.#.#.#.#.#.#.#########.###.#####.###########.###.#.###.#######.#.#.#####
#.#.#.....#.....#...#...#.#.#.###...#...###...#.#.#.#...#.#.#.#.#...#.#.#.#.#.#.#.#########...#.....#.............###...#...#.....#...#.....#
#.#.#.#####.###.#########.#.#.#####.#.#.###.###.#.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.###########.#####.#####################.###.###.#########.#
#...#.#...#.#...#.....#...#.#.#...#...#.....#...#.#.#.#.#.#.#.#...#.#.#.#.#.#.#.#.#########...###...#.................###.#...###.#.........#
#####.#.#.#.#.###.###.#.###.#.#.#.###########.###.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#.#########.#####.###.###############.###.#.#####.#.#########
#.....#.#.#.#...#...#.#...#...#.#.#...#.....#...#.#.#.#.#.#.#...#.#.#.#.#.#.#.#.#.#########.....#...#.#.............#...#...###...#.........#
#.#####.#.#.###.###.#.###.#####.#.#.#.#.###.###.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#.#.#############.###.#.#.###########.###.#######.###########.#
#.#...#.#.#...#...#.#.#...#.....#...#...###.....#.#...#.#.#.#...#.#.#.#.#.#.#...#.#########.....###...#...........#...#.......#...#...#...#.#
#.#.#.#.#.###.###.#.#.#.###.#####################.#####.#.#.#.###.#.#.#.#.#.#####.#########.#####################.###.#######.###.#.#.#.#.#.#
#.#.#.#.#.#...###...#...###...#.....#...#...#...#...#...#.#.#.#...#.#.#.#.#.#.....#########.###...###...#.........###.......#...#.#.#...#...#
#.#.#.#.#.#.#################.#.###.#.#.#.#.#.#.###.#.###.#.#.#.###.#.#.#.#.#.#############.###.#.###.#.#.#################.###.#.#.#########
#.#.#...#...#.......###...#...#.###...#.#.#.#.#.#...#.#...#.#.#.#...#.#.#.#.#.#.....#######...#.#...#.#.#.......#.....#...#.#...#.#.........#
#.#.#########.#####.###.#.#.###.#######.#.#.#.#.#.###.#.###.#.#.#.###.#.#.#.#.#.###.#########.#.###.#.#.#######.#.###.#.#.#.#.###.#########.#
#...###...#...#...#...#.#.#.....#.......#.#.#.#.#.#...#...#.#.#...#...#.#.#.#.#.#...#########...#...#.#...#...#...#...#.#.#...###...........#
#######.#.#.###.#.###.#.#.#######.#######.#.#.#.#.#.#####.#.#.#####.###.#.#.#.#.#.###############.###.###.#.#.#####.###.#.###################
#.......#...#...#...#...#.......#.......#.#.#.#.#.#...#...#.#.....#...#.#.#.#...#...#######.......#...###.#.#.#...#...#.#.............#...###
#.###########.#####.###########.#######.#.#.#.#.#.###.#.###.#####.###.#.#.#.#######.#######.#######.#####.#.#.#.#.###.#.#############.#.#.###
#.......#...#...###...#...#...#.......#.#.#.#.#.#...#.#.###.#.....###...#.#.......#.#E#####.#...#...#.....#.#.#.#...#...#.....#.....#...#...#
#######.#.#.###.#####.#.#.#.#.#######.#.#.#.#.#.###.#.#.###.#.###########.#######.#.#.#####.#.#.#.###.#####.#.#.###.#####.###.#.###.#######.#
#.......#.#...#.#.....#.#...#...#...#...#.#.#.#.....#.#...#...#...........#.......#.#.#####.#.#.#.###...#...#.#.###...#...###...#...#...#...#
#.#######.###.#.#.#####.#######.#.#.#####.#.#.#######.###.#####.###########.#######.#.#####.#.#.#.#####.#.###.#.#####.#.#########.###.#.#.###
#.#...#...#...#.#.......#...###...#.#...#.#.#.......#.#...#...#...........#.......#.#...###...#.#...#...#...#.#...#...#.........#...#.#.#...#
#.#.#.#.###.###.#########.#.#######.#.#.#.#.#######.#.#.###.#.###########.#######.#.###.#######.###.#.#####.#.###.#.###########.###.#.#.###.#
#.#.#.#.###...#.#.....#...#.........#.#.#.#.#.......#.#.....#.#...........#...#...#...#.......#.#...#.#...#.#.#...#.#.....#...#...#...#.#...#
#.#.#.#.#####.#.#.###.#.#############.#.#.#.#.#######.#######.#.###########.#.#.#####.#######.#.#.###.#.#.#.#.#.###.#.###.#.#.###.#####.#.###
#.#.#...#...#...#...#.#...#.......#...#.#.#.#.......#...#.....#.........#...#.#.#####.#.......#...#...#.#.#.#.#.#...#...#.#.#...#...#...#.###
#.#.#####.#.#######.#.###.#.#####.#.###.#.#.#######.###.#.#############.#.###.#.#####.#.###########.###.#.#.#.#.#.#####.#.#.###.###.#.###.###
#.#...#...#.###.....#.....#.#.....#.#...#.#.#...#...#...#...#...........#.###.#...#...#.......#.....#...#.#.#.#.#...#...#.#.#...#...#...#...#
#.###.#.###.###.###########.#.#####.#.###.#.#.#.#.###.#####.#.###########.###.###.#.#########.#.#####.###.#.#.#.###.#.###.#.#.###.#####.###.#
#.#...#...#.#...#.......#...#.#...#.#...#.#...#.#...#.#...#.#.....#...#...#...#...#...#...#...#.#...#...#.#.#.#.###.#.###...#...#.###...#...#
#.#.#####.#.#.###.#####.#.###.#.#.#.###.#.#####.###.#.#.#.#.#####.#.#.#.###.###.#####.#.#.#.###.#.#.###.#.#.#.#.###.#.#########.#.###.###.###
#...#.....#.#.....#.....#.#...#.#.#.#...#...#...#...#.#.#.#.#.....#.#.#...#.#...###...#.#.#.#...#.#.#...#.#.#.#...#.#.....#.....#...#...#...#
#####.#####.#######.#####.#.###.#.#.#.#####.#.###.###.#.#.#.#.#####.#.###.#.#.#####.###.#.#.#.###.#.#.###.#.#.###.#.#####.#.#######.###.###.#
#.....#...#...###...#...#.#.#...#...#...#...#.....###.#.#.#.#.#.....#.#...#.#.#...#.....#.#.#.#...#.#.###.#.#.#...#.#.....#...#...#...#.....#
#.#####.#.###.###.###.#.#.#.#.#########.#.###########.#.#.#.#.#.#####.#.###.#.#.#.#######.#.#.#.###.#.###.#.#.#.###.#.#######.#.#.###.#######
#.......#...#.#...#...#.#.#.#...#.....#.#.###...#...#.#.#.#.#.#...#...#.#...#...#...#...#.#.#.#.#...#...#.#.#...#...#.....#...#.#...#.......#
###########.#.#.###.###.#.#.###.#.###.#.#.###.#.#.#.#.#.#.#.#.###.#.###.#.#########.#.#.#.#.#.#.#.#####.#.#.#####.#######.#.###.###.#######.#
#...........#...#...#...#.#.....#...#...#.....#...#.#...#.#.#...#.#...#.#.#...#...#...#.#...#...#.#...#.#.#.....#...#.....#...#...#.#.....#.#
#.###############.###.###.#########.###############.#####.#.###.#.###.#.#.#.#.#.#.#####.#########.#.#.#.#.#####.###.#.#######.###.#.#.###.#.#
#.#.............#...#...#.#.......#.#...#.....#...#...###...###...###...#.#.#...#.#...#...###...#...#.#.#...#...#...#.......#...#.#...#...#.#
#.#.###########.###.###.#.#.#####.#.#.#.#.###.#.#.###.###################.#.#####.#.#.###.###.#.#####.#.###.#.###.#########.###.#.#####.###.#
#...#...#.......#...###.#.#.#...#...#.#...###.#.#...#.....#...#...#...###.#.....#.#.#...#.#...#.....#.#.#...#...#...#.......###.#.....#...#.#
#####.#.#.#######.#####.#.#.#.#.#####.#######.#.###.#####.#.#.#.#.#.#.###.#####.#.#.###.#.#.#######.#.#.#.#####.###.#.#########.#####.###.#.#
#.....#...#...#...#.....#.#.#.#.#...#.....#...#.#...#...#.#.#...#...#.....#...#.#.#.#...#...#.....#.#.#.#...#...#...#.......#...#...#...#.#.#
#.#########.#.#.###.#####.#.#.#.#.#.#####.#.###.#.###.#.#.#.###############.#.#.#.#.#.#######.###.#.#.#.###.#.###.#########.#.###.#.###.#.#.#
#...........#...###.......#...#...#.......#.....#.....#...#.................#...#...#.........###...#...###...###...........#.....#.....#...#
#############################################################################################################################################
"""

from collections import deque

grid = [list(row) for row in input.strip().split('\n')]
rows = len(grid)
cols = len(grid[0])

dists = [[-1] * cols for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            break
    else:
        continue
    break

q = deque([(r, c)])
dists[r][c] = 0

while q:
    cr, cc = q.popleft()
    for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
        if grid[nr][nc] == '#': continue
        if dists[nr][nc] != -1: continue
        dists[nr][nc] = dists[cr][cc] + 1
        q.append((nr, nc))

count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '#': continue
        for radius in range(2, 21):
            for dr in range(radius + 1):
                dc = radius - dr
                for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                    if grid[nr][nc] == '#': continue
                    if dists[r][c] - dists[nr][nc] >= 100 + radius: count += 1
            
print(count)