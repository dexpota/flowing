from uuid import uuid4
import numpy as np

POSITION_BELOW = "below"
POSITION_ABOVE = "above"
POSITION_SAME_LEFT = "same_left"
POSITION_SAME_RIGHT = "same_right"
EDGE_DIRECTION_DIRECT = "direct"
EDGE_DIRECTION_CW = "cw"
EDGE_DIRECTION_COUNTER_CW = "counter_cw"


def if_commands(if_node, node1, node2=None):
    """
    Return a set of graphviz command representing the if statement and branches.
    :param if_node: if node name and label
    :param node_name1: node1 name and label
    :param node_name2: node2 name and label
    :param position1: node1 position, one between 'below' (default), 'above', 'same_left' and 'same_right'
    :param position2: node2 position, one between 'below' (default), 'above', 'same_left' and 'same_right'
    :param edge_path1: node1 edge direction, one between 'direct' (default), 'cw', and 'counter_cw'
    :param edge_path2: node2 edge direction, one between 'direct' (default), 'cw', and 'counter_cw'
    :return A list of graphviz command:
    """

    node_name1 = node1["name"]
    if "position" in node1:
        position1 = node1["position"]
    else:
        position1 = "below"

    if "direction" in node1:
        edge_path1 = node1["direction"]
    else:
        edge_path1 = "direct"

    positions = [position1]
    directions = [edge_path1]
    names = [node_name1]

    if node2:
        node_name2 = node2["name"]
        if "position" in node2:
            position2 = node2["position"]
        else:
            position2 = "below"

        if "direction" in node2:
            edge_path2 = node2["direction"]
        else:
            edge_path2 = "direct"

        positions.append(position2)
        directions.append(edge_path2)
        names.append(node_name2)

    matrices = [np.ones((3, 3)), np.ones((3, 3))]

    for i, position, edge in zip([0, 1], positions, directions):
        if edge == "cw":
            matrices[i][0, 0] = 0
            matrices[i][1, 0] = 0
        elif edge == "counter_cw":
            matrices[i][0, 2] = 0
            matrices[i][1, 2] = 0

        if position == "same_left":
            matrices[i] = np.rot90(matrices[i])
        elif position == "below":
            matrices[i] = np.rot90(matrices[i], 2)
        elif position == "same_right":
            matrices[i] = np.rot90(matrices[i], 3)

    compatible = np.all(np.logical_or(matrices[0], matrices[1]))

    if not compatible:
        raise ValueError()

    subgraph_commands = []
    subgraph_commands.append("\"{if_node}\"[shape=diamond, label=\"{if_node}\"];".format(if_node=if_node))
    subgraph_commands.append("\"{node1}\"[label=\"{node1}\"];".format(node1=node_name1))
    if node2:
        subgraph_commands.append("\"{node2}\"[label=\"{node2}\"];".format(node2=node_name2))

    same_rank = ["\"{}\"".format(if_node)]

    for node_name, position, edge_path in zip(names, positions, directions):
        if edge_path != "counter_cw" and edge_path != "cw":
            if position == "below":
                subgraph_commands.append("\"{if_node}\" -> \"{node}\";".format(if_node=if_node, node=node_name))
            elif position == "above":
                subgraph_commands.append("\"{node}\" -> \"{if_node}\"[dir=back];".format(if_node=if_node, node=node_name))
            elif position == "same_right":
                subgraph_commands.append("\"{if_node}\" -> \"{node}\"".format(if_node=if_node, node=node_name))
                same_rank.append("\"{}\"".format(node_name))
            elif position == "same_left":
                subgraph_commands.append("\"{node}\" -> \"{if_node}\"[dir=back];".format(if_node=if_node, node=node_name))
                same_rank.append("\"{}\"".format(node_name))

    for node, position, edge_path in zip(names, positions, directions):
        temp_name = "_" + uuid4().hex
        if edge_path == "cw":
            if position == "below":
                subgraph_commands.append("\"{if_node}\" -> {temp} [dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("{temp} -> \"{node}\";".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point, ];".format(temp=temp_name))
                same_rank.append("{temp}".format(temp=temp_name))
            elif position == "above":
                subgraph_commands.append("{temp} -> \"{if_node}\"[dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("\"{node}\" -> {temp}[dir=back];".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point];".format(temp=temp_name))
                same_rank.append("{temp}".format(temp=temp_name))
            elif position == "same_right":
                subgraph_commands.append("{temp} -> \"{if_node}\"[dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("{temp} -> \"{node}\";".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point, ];".format(temp=temp_name))
                subgraph_commands.append("{{ rank=same; {temp}; \"{node}\";}}".format(node=node, temp=temp_name))
            elif position == "same_left":
                subgraph_commands.append("\"{if_node}\" -> {temp}[dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("\"{node}\" -> {temp} [dir=back];".format(node=node, temp=temp_name))
                subgraph_commands.append("{{ rank=same; {temp}; \"{node}\";}}".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point, ];".format(temp=temp_name))
        elif edge_path == "counter_cw":
            if position == "below":
                subgraph_commands.append("{temp} -> \"{if_node}\"[dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("{temp} -> \"{node}\";".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point, ];".format(temp=temp_name))
                same_rank.append("{temp}".format(temp=temp_name))
            elif position == "above":
                subgraph_commands.append("\"{if_node}\" -> {temp}[dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("\"{node}\" -> {temp}[dir=back];".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point, ];".format(temp=temp_name))
                same_rank.append("{temp}".format(temp=temp_name))
            elif position == "same_left":
                subgraph_commands.append("{temp} -> \"{if_node}\"[dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("\"{node}\" -> {temp}[dir=back];".format(node=node, temp=temp_name))
                subgraph_commands.append("{{ rank=same; {temp}; \"{node}\";}}".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point, ];".format(temp=temp_name))
            elif position == "same_right":
                subgraph_commands.append("\"{if_node}\" -> {temp}[dir=none];".format(if_node=if_node, temp=temp_name))
                subgraph_commands.append("{temp} -> \"{node}\";".format(node=node, temp=temp_name))
                subgraph_commands.append("{temp}[shape=point, ];".format(temp=temp_name))
                subgraph_commands.append("{{ rank=same; {temp}; \"{node}\";}}".format(node=node, temp=temp_name))

    subgraph_commands.append("{{rank=same; {} }}".format(";".join(same_rank)))

    return subgraph_commands
