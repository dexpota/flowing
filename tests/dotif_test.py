import sys
import os
from itertools import product
from flowing.dotif import POSITION_SAME_RIGHT, POSITION_SAME_LEFT, POSITION_ABOVE, POSITION_BELOW
from flowing.dotif import EDGE_DIRECTION_COUNTER_CW, EDGE_DIRECTION_DIRECT, EDGE_DIRECTION_CW
from flowing.dotif import if_commands

if __name__ == "__main__":
    def generate_arguments_combinations(*vargs):
        arguments_values = []
        for values in vargs:
            arguments_values.append(values)
        return product(*arguments_values)

    position_values = [POSITION_ABOVE, POSITION_BELOW, POSITION_SAME_LEFT, POSITION_SAME_RIGHT]
    direction_values = [EDGE_DIRECTION_CW, EDGE_DIRECTION_COUNTER_CW, EDGE_DIRECTION_DIRECT]

    if not os.path.isdir("./output"):
        os.mkdir("./output")

    for i, c in enumerate(generate_arguments_combinations(position_values, position_values, direction_values, direction_values)):
        try:
            node1 = {
                "name": "True",
                "position": c[0],
                "direction": c[2]
            }

            node2 = {
                "name": "True",
                "position": c[1],
                "direction": c[3]
            }
            commands = if_commands("if something", node1, node2)

            fp = open("./output/if{}.dot".format(i), "w")
            fp.write("digraph {\n splines=line; rank=TB;\n")
            fp.write("node[fillcolor=\"#006699\"; fontcolor=\"white\"; style=filled; shape=rect];\n")
            fp.write("\n".join(commands))
            fp.write("\nlabel = \"" + c[0] + ", " + c[2] + ", secondo " + c[1] + ", " + c[3] + "\"")
            fp.write("}")
            fp.close()
        except ValueError as e:
            print("Arguments not valid: {}".format(c))