from graphviz import Digraph


def viztree(leaf_list, root):
    leaf_id = list(map(lambda x: [x.id, x.branchAttribute, x.parent, x.classes, x.decision], leaf_list))
    dot = Digraph(comment='Visualization', format='svg')
    for i in leaf_id:
        if sum(i[4]) > 0:
            bar = 'slategray1;' + str(i[4][0] / sum(i[4])) + ':mistyrose;' + str(i[4][1] / sum(i[4]))
        else:
            bar = 'slategray1;0.5:mistyrose;0.5'
        if i[1] is None:
            if i[4][0] >= i[4][1]:
                decision = 'True'
                label = 'True:' + str(i[4][0]) + ' / ' + 'False:' + str(i[4][1]) + '\n'
                dot.node(i[0], "<"+label+"<font color='blue'><br/>"+decision+"<br/></font>>",fontcolor='antiquewhite4',color='antiquewhite4', fontname='Arial')
                '<<FONT COLOR="RED" POINT-SIZE="24.0" FACE="ambrosia">line4</FONT> and then more stuff>'
                print()
            else:
                decision = 'False'
                label = 'True:' + str(i[4][0]) + ' / ' + 'False:' + str(i[4][1]) + '\n'
                dot.node(i[0], "<"+label+"<font color='red'><br/>"+decision+"<br/></font>>",fontcolor='antiquewhite4',color='antiquewhite4', fontname='Arial')
        else:
            dot.node(i[0], i[1] + '\n[True:' + str(i[4][0]) + ' / False:' + str(i[4][1]) + ']',
                     color='antiquewhite4',shape='box', fontname='Arial', style='striped', fillcolor=bar, fontcolor='antiquewhite4')
        if i[2] is '1':
            dot.edge(i[2], i[0], i[3], fontname='Arial', arrowhead='normal',color='antiquewhite4')
        else:
            dot.edge(i[2].id, i[0], i[3], fontname='Arial', arrowhead='normal',color='antiquewhite4')

    # ===========================================================

    root_bar = 'slategray1;' + str(root.decision[0] / sum(root.decision)) + ':mistyrose;' + str(
        root.decision[1] / sum(root.decision))
    dot.node('1', root.branchAttribute + '\n[True:' + str(root.decision[0]) + ' / False:' + str(root.decision[1]) + ']',
             color='antiquewhite4', shape='box', fontname='Arial', style='striped', fillcolor=root_bar,
             fontcolor='antiquewhite4')

    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render('test-output/Visualization.gv', view=True)