from graphviz import Digraph


def viztree(leaf_list, root):
    leaf_id = list(map(lambda x: [x.id, x.branchAttribute, x.parent, x.classes, x.decision], leaf_list))
    dot = Digraph(comment='Visualization', format='svg')
    for i in leaf_id:
        if sum(i[4]) > 0:
            bar = 'gray98;' + str(i[4][0] / sum(i[4])) + ':mistyrose;' + str(i[4][1] / sum(i[4]))
        else:
            bar = 'gray98;0.5:mistyrose;0.5'
        if i[1] is None:
            if i[4][0] >= i[4][1]:
                decision = 'Good'
            else:
                decision = 'Bad'
            dot.node(i[0], 'Good : ' + str(i[4][0]) + ' / ' + 'Bad : ' + str(i[4][1]) + '\n' + decision,
                     color='aquamarine3',
                     shape='oval', fontname='Arial', style='filled', fillcolor='gray98', fontcolor='aquamarine3')
        else:
            dot.node(i[0], i[1] + '\n[good:' + str(i[4][0]) + ' / bad:' + str(i[4][1]) + ']', color='antiquewhite4',
                     shape='box', fontname='Arial', style='striped', fillcolor=bar, fontcolor='antiquewhite4')
        if i[2] is '1':
            dot.edge(i[2], i[0], i[3], color='grey73', fontname='Arial', arrowhead='normal')
        else:
            dot.edge(i[2].id, i[0], i[3], color='grey73', fontname='Arial', arrowhead='normal')

    # ===========================================================

    root_bar = 'gray98;' + str(root.decision[0] / sum(root.decision)) + ':mistyrose;' + str(
        root.decision[1] / sum(root.decision))
    dot.node('1', root.branchAttribute + '\n[good:' + str(root.decision[0]) + ' / bad:' + str(root.decision[1]) + ']',
             color='antiquewhite4', shape='box', fontname='Arial', style='striped', fillcolor=root_bar,
             fontcolor='antiquewhite4')

    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render('test-output/Visualization.gv', view=True)
