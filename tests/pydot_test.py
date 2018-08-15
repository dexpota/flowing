import sys
import os
from flowing.dotif import if_commands
from flowing.pydot import visit
from flowing.pydot import import_filter
from flowing.pydot import Flowchart
import ast


def print_format(args):
    return " ".join(args)


if __name__ == "__main__":
    testContent = open("input/function.py").read()

    tree = ast.parse(testContent)
    commands = Flowchart()
    last_nodes = visit("start", tree.body, commands, [], {"print": print_format})
    for node in last_nodes:
        commands.append("\"{}\" -> end;".format(node))
    commands.add_node_attributes(fillcolor="#006699")
    commands.add_node_attributes(style="filled")
    commands.add_node_attributes(fontcolor="white")
    commands.add_node_attributes(shape="rect")
    if not os.path.isdir("./output"):
        os.mkdir("./output")

    fp = open("./output/algorithm.dot", "w")
    fp.write(commands.to_string())
    fp.close()

    exit()

    commands1 = if_commands("if a", "clean a", "ask for b", edge_path1=EDGE_DIRECTION_CW, edge_path2=EDGE_DIRECTION_COUNTER_CW);
    commands2 = if_commands("if b", "clean b", "ask for c", edge_path1=EDGE_DIRECTION_CW, edge_path2=EDGE_DIRECTION_COUNTER_CW);

    fp = open("algorithm.dot", "w")
    fp.write("digraph {\n splines=line; rank=TB;\n")
    fp.write("node[fillcolor=\"#006699\"; fontcolor=\"white\"; style=filled; shape=rect];\n")
    fp.write("\n".join(commands1))
    fp.write("\n".join(commands2))
    fp.write("\"ask for b\" -> \"if b\"\n")
    fp.write("}")
    fp.close()