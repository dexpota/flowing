from flowing.dotif import if_commands
from flowing.dotif import EDGE_DIRECTION_CW, EDGE_DIRECTION_COUNTER_CW
import ast

graphviz_attributes = {u'charset': u'string', u'tailport': u'portPos', u'labeltarget': u'escString', u'distortion': u'double', u'samehead': u'string', u'shape': u'shape', u'Damping': u'double', u'sametail': u'string', u'peripheries': u'int', u'rotation': u'double', u'layers': u'layerList', u'fontname': u'string', u'imagepath': u'string', u'group': u'string', u'esep': [u'addDouble', u'addPoint'], u'outputorder': u'outputMode', u'fontpath': u'string', u'lp': u'point', u'maxiter': u'int', u'headtooltip': u'escString', u'pad': [u'double', u'point'], u'edgetooltip': u'escString', u'nodesep': u'double', u'nojustify': u'bool', u'headport': u'portPos', u'URL': u'escString', u'gradientangle': u'int', u'mindist': u'double', u'tailclip': u'bool', u'fillcolor': [u'color', u'colorList'], u'compound': u'bool', u'labeldistance': u'double', u'headtarget': u'escString', u'searchsize': u'int', u'tooltip': u'escString', u'edgehref': u'escString', u'dim': u'int', u'dimen': u'int', u'rotate': u'int', u'labelfontcolor': u'color', u'splines': [u'bool', u'string'], u'tailtooltip': u'escString', u'tailURL': u'escString', u'quadtree': [u'quadType', u'bool'], u'mode': u'string', u'sortv': u'int', u'page': [u'double', u'point'], u'dpi': u'double', u'label_scheme': u'int', u'levelsgap': u'double', u'fontnames': u'string', u'labelfloat': u'bool', u'ltail': u'string', u'tailhref': u'escString', u'nslimit': u'double', u'head_lp': u'point', u'quantum': u'double', u'labelloc': u'string', u'scale': [u'double', u'point'], u'fixedsize': [u'bool', u'string'], u'overlap': [u'string', u'bool'], u'label': u'lblString', u'landscape': u'bool', u'imagescale': [u'bool', u'string'], u'voro_margin': u'double', u'penwidth': u'double', u'inputscale': u'double', u'headclip': u'bool', u'bb': u'rect', u'overlap_shrink': u'bool', u'K': u'double', u'mosek': u'bool', u'len': u'double', u'ranksep': [u'double', u'doubleList'], u'concentrate': u'bool', u'layout': u'string', u'constraint': u'bool', u'root': [u'bool', u'string'], u'truecolor': u'bool', u'defaultdist': u'double', u'mclimit': u'double', u'regular': u'bool', u'dir': u'dirType', u'xlp': u'point', u'layersep': u'string', u'comment': u'string', u'tailtarget': u'escString', u'color': [u'color', u'colorList'], u'image': u'string', u'pos': [u'point', u'splineType'], u'rank': u'rankType', u'height': u'double', u'arrowsize': u'double', u'href': u'escString', u'headURL': u'escString', u'size': u'doublepoint', u'showboxes': u'int', u'layerlistsep': u'string', u'tail_lp': u'point', u'area': u'double', u'ordering': u'string', u'skew': u'double', u'sep': [u'addDouble', u'addPoint'], u'labelangle': u'double', u'smoothing': u'smoothType', u'bgcolor': [u'color', u'colorList'], u'stylesheet': u'string', u'start': u'startType', u'labeljust': u'string', u'labelfontname': u'string', u'edgeURL': u'escString', u'weight': [u'int', u'double'], u'headlabel': u'lblString', u'packmode': u'packMode', u'fontsize': u'double', u'viewport': u'viewPort', u'target': [u'escString', u'string'], u'lhead': u'string', u'colorscheme': u'string', u'xdotversion': u'string', u'xlabel': u'lblString', u'decorate': u'bool', u'rects': u'rect', u'pagedir': u'pagedir', u'lheight': u'double', u'z': u'double', u'margin': [u'double',u'point'], u'pack': [u'bool', u'int'], u'remincross': u'bool', u'layer': u'layerRange', u'orientation': u'string', u'pin': u'bool', u'minlen': u'int', u'style': u'style', u'layerselect': u'layerRange', u'lwidth': u'double', u'id': u'escString', u'ratio': [u'double', u'string'], u'diredgeconstraints': [u'string', u'bool'], u'arrowhead': u'arrowType', u'shapefile': u'string', u'labeltooltip': u'escString', u'notranslate': u'bool', u'arrowtail': u'arrowType', u'epsilon': u'double', u'repulsiveforce': u'double', u'fontcolor': u'color', u'labelURL': u'escString', u'normalize': [u'double', u'bool'], u'forcelabels': u'bool', u'_background': u'string', u'labelfontsize': u'double', u'edgetarget': u'escString', u'levels': u'int', u'clusterrank': u'clusterMode', u'samplepoints': u'int', u'sides': u'int', u'taillabel': u'lblString', u'center': u'bool', u'vertices': u'pointList', u'pencolor': u'color', u'labelhref': u'escString', u'rankdir': u'rankdir', u'overlap_scaling': u'double', u'width': u'double', u'model': u'string', u'resolution': u'double', u'headhref': u'escString',}

# TODO http/://www.graphviz.org/doc/info/attrs.html
graphviz_attribute_formatters = {
     u'addDouble': None,
    u'addPoint': None,
     u'arrowType': None,
     u'bool': None,
     u'clusterMode': None,
     u'color': lambda s: "\"{}\"".format(s),
     u'colorList': None,
     u'dirType': None,
     u'double': None,
     u'doubleList': None,
     u'escString': None,
     u'int': None,
     u'layerList': None,
     u'layerRange': None,
     u'lblString': None,
     u'outputMode': None,
     u'packMode': None,
     u'pagedir': None,
     u'point': None,
     u'pointList': None,
     u'splineType': None,
     u'portPos': None,
     u'quadType': None,
     u'rankType': None,
     u'rankdir': None,
     u'rect': None,
     u'shape': lambda s: "{}".format(s),
     u'smoothType': None,
     u'startType': None,
     u'string': lambda s: "\"{}\"".format(s),
     u'style': lambda s: "\"{}\"".format(s),
     u'viewPort': None
 }
# see https://docs.python.org/2/library/ast.html


def _operator_to_string(op):
    if isinstance(op, ast.cmpop):
        if isinstance(op, ast.Eq):
            return "=="
        elif isinstance(op, ast.NotEq):
            return "!="
        elif isinstance(op, ast.Lt):
            return "<"
        elif isinstance(op, ast.LtE):
            return "<="
        elif isinstance(op, ast.Gt):
            return ">"
        elif isinstance(op, ast.GtE):
            return ">="
        elif isinstance(op, ast.Is):
            return "is"
        elif isinstance(op, ast.IsNot):
            return "is not"
        elif isinstance(op, ast.In):
            return "in"
        elif isinstance(op, ast.NotIn):
            return "not in"
    if isinstance(op, ast.unaryop):
        if isinstance(op, ast.Not):
            return "!"


def _compare_to_string(left, operators, comparators):
    if not len(comparators):
        return expr_to_string(left)

    assert len(operators) == len(comparators)
    tail = []
    for operator, expression in zip(operators, comparators):
        tail.append(_operator_to_string(operator) + " " + expr_to_string(expression))
    return expr_to_string(left) + " " + " ".join(tail)


def expr_to_string(expression):
    if isinstance(expression, ast.Compare):
        return _compare_to_string(expression.left, expression.ops, expression.comparators)
    elif isinstance(expression, ast.Name):
        return str(expression.id)
    elif isinstance(expression, ast.Num):
        return str(expression.n)
    elif isinstance(expression, ast.Str):
        return str(expression.s)
    elif isinstance(expression, ast.Call):
        call = expression

        if call.starargs or call.kwargs:
            raise NotImplementedError()

        value = "{}({}, {})".format(
            expr_to_string(call.func),
            map(expr_to_string, call.args),
            map(expr_to_string, call.keywords))
        return value
    elif isinstance(expression, ast.keyword):
        return "{} = {}".format(expression.arg, expr_to_string(expression.value))
    elif isinstance(expression, ast.Attribute):
        return "{}.{}".format(expr_to_string(expression.value), expression.attr)
    elif isinstance(expression, ast.List):
        return str(expression.elts)
    elif isinstance(expression, ast.UnaryOp):
        return "{} {}".format(_operator_to_string(expression.op), expr_to_string(expression.operand))
    elif isinstance(expression, ast.Dict):
        key_values = ["{"]
        for key, value in zip(map(expr_to_string, expression.keys), map(expr_to_string, expression.values)):
            key_values.append("{}: {}".format(key, value))
        key_values.append("}")
        return ", ".join(key_values)
    else:
        raise NotImplementedError("{} not handled.".format(type(expression).__name__))
        return


def stmt_to_string(stmt):
    """

    :param stmt:
    :type stmt: ast.stmt
    :return:
    """
    return "{}:{}:{}".format(type(stmt).__name__, stmt.lineno, stmt.col_offset)


def alias_to_string(alias):
    if alias.asname:
        return "{} as {}".format(alias.name, alias.asname)
    else:
        return "{}".format(alias.name)


def visit_stmt(stmt, commands, filters, node_format):
    if isinstance(stmt, ast.If):
        expression = expr_to_string(stmt.test)

        if stmt.body and stmt.orelse:
            node1 = {
                "name": stmt_to_string(stmt.body[0]),
            }

            node2 = {
                "name": stmt_to_string(stmt.orelse[0]),
            }

            commands += if_commands(stmt_to_string(stmt), node1, node2)
            last_if_1 = visit(None, stmt.body, commands, filters, node_format)
            last_if_2 = visit(None, stmt.orelse, commands, filters, node_format)

            commands.append("\"{}\"[ label=\"{}\" ];".format(stmt_to_string(stmt), expression))
        elif stmt.body:
            node1 = {
                "name": stmt_to_string(stmt.body[0]),
            }

            commands += if_commands(stmt_to_string(stmt), node1)
            commands.append("\"{}\"[ label=\"{}\" ];".format(stmt_to_string(stmt), expression))

            last_if_1 = visit(None, stmt.body, commands, filters, node_format)
            last_if_2 = [stmt_to_string(stmt)]
        else:
            assert False

        return last_if_1 + last_if_2
    elif isinstance(stmt, ast.Assign):
        name = "{} = {}".format(",".join(map(expr_to_string, stmt.targets)), expr_to_string(stmt.value))
        commands.append("\"{}\"[ label=\"{}\" ];".format(stmt_to_string(stmt), name))
        return [stmt_to_string(stmt)]
    elif isinstance(stmt, ast.Print):
        # stmt.dest
        # stmt.nl

        if "print" in node_format:
            label = node_format["print"](map(expr_to_string, stmt.values))
            commands.append("\"{}\"[ label=\"{}\" ];".format(stmt_to_string(stmt), label))
        else:
            label = ", ".join(map(expr_to_string, stmt.values))
            commands.append("\"{}\"[ label=\"print({})\" ];".format(stmt_to_string(stmt), label))
        return [stmt_to_string(stmt)]
    elif isinstance(stmt, ast.Import):
        commands.append("\"{}\"[ label=\"{}\" ];".format(
            stmt_to_string(stmt),
            "import {}".format(map(alias_to_string, stmt.names))))
        return [stmt_to_string(stmt)]
    elif isinstance(stmt, ast.ImportFrom):
        # stmt.level
        commands.append("\"{}\"[ label=\"{}\" ];".format(
            stmt_to_string(stmt),
            "from {} import {}".format(stmt.module, map(alias_to_string, stmt.names))))
        return [stmt_to_string(stmt)]
    elif isinstance(stmt, ast.Expr):
        commands.append("\"{}\" [ label=\"{}\" ];".format(stmt_to_string(stmt),
                                                          expr_to_string(stmt.value).replace('"','\\"')
))
        return [stmt_to_string(stmt)]
    elif isinstance(stmt, ast.FunctionDef):

        print(stmt.name)

        if stmt.args.defaults:
            _args= stmt.args.args
            _defaults = stmt.args.defaults
            args_names = map(expr_to_string, _args)
            args_defaults = map(expr_to_string, _defaults)

            _args_without_defaults = ", ".join(args_names[0:len(args_defaults)])
            _args_with_defaults = ", ".join("{} = {}".format(*k) for k in zip(args_names[-len(args_defaults):], args_defaults))
        else:
            _args_without_defaults = ",".join(map(expr_to_string, stmt.args.args))
            _args_with_defaults = None

        label = "{}({}, {}, *{}, **{})".format(
            stmt.name,
            _args_without_defaults,
            _args_with_defaults,
            stmt.args.vararg,
            stmt.args.kwarg)

        commands.append("\"{}\" [label=\"{}\"];".format(stmt_to_string(stmt), label))

        print(stmt.body)
        print(stmt.decorator_list)
        return [stmt_to_string(stmt)]
    else:
        raise NotImplementedError()
        return [stmt_to_string(stmt)]


def function_filter(node):
    return isinstance(node, ast.FunctionDef)


def import_filter(node):
    return not(isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom))


def visit(root, children, commands, filters=[], node_format={}):
    last_elements = [root]

    if filters != None and len(filters) > 0:
        filtered = filter(lambda x: any([f(x) for f in filters]), children)
    else:
        filtered = children

    for element in filtered:

        for last_element in last_elements:
            if last_element:
                commands.append("\"{last_element}\" -> \"{element}\"".format(
                    last_element=last_element, element=stmt_to_string(element)))

        last_elements = [element]
        if isinstance(element, ast.stmt):
            last_elements = visit_stmt(element, commands, filters, node_format)

    return last_elements

class Flowchart:
    def __init__(self):
        self.nodes = []
        self.commands = []
        self.node_attributes = {}

    def add_node_attributes(self, **kwargs):
        #node[fillcolor =\"#006699\"; fontcolor=\"white\"; style=filled; shape=rect];
        for key, value in kwargs.iteritems():
            self.node_attributes[key] = value
        pass

    def add_node(self, id):
        self.nodes.append({'id': id})
        pass

    def append(self, command):
        self.commands.append(command)

    def __iadd__(self, other):
        self.commands += other
        return self

    def __add__(self, other):
        self.commands += other
        return self

    def __str__(self):
        return "\n".join(self.commands)

    def __iter__(self):
        return iter(self.commands)

    def to_string(self):
        attributes = []
        for key, value in self.node_attributes.iteritems():
            attribute_type = graphviz_attributes[key]
            if isinstance(attribute_type, list):
                # attribute_type is an array of types
                for _type in attribute_type:
                    try:
                        # try to parse the value as type _type
                        value = graphviz_attribute_formatters[_type](value)
                    except:
                        pass

                # we have three possibilites here:
                # 1. none of the conversion function worked
                # 2. one of the conversion function worked
                # 3. more than one conversion function worked

                if not value:
                    raise ValueError()

                attributes.append("{}={}".format(key, value))
            else:
                attributes.append("{}={}".format(key, graphviz_attribute_formatters[attribute_type](value)))


        self.commands = ["digraph {", "node[{}]".format(";".join(attributes))] + self.commands
        self.commands.append("}")
        return "\n".join(self.commands)
