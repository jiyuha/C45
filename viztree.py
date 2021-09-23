from graphviz import Digraph


def viztree(leaf_list, root):
    leaf_id = list(map(lambda x: [x.id, x.branchAttribute, x.parent, x.classes, x.decision], leaf_list))
    dot = Digraph(comment='Visualization', format='svg')
    for i in leaf_id:
        bar = 'gray98;' + str(i[4][0] / sum(i[4])) + ':mistyrose;' + str(i[4][1] / sum(i[4]))
        if i[1] is None:
            dot.node(i[0], str(i[4][0])+' / '+str(i[4][1]), color='aquamarine3',shape='oval',fontname = 'Arial',style='filled',fillcolor='lightyellow',fontcolor='aquamarine3')
        else:
            dot.node(i[0], i[1] + '\n[good:' + str(i[4][0]) + ' / bad:'+str(i[4][1])+ ']',color='antiquewhite4',shape='box',fontname='Arial',style='striped',fillcolor=bar,fontcolor='antiquewhite4')

        dot.edge(i[2], i[0], i[3],color='grey73',fontname = 'Arial',arrowhead='normal')
    dot.node('1', root.branchAttribute, color='antiquewhite4',shape='box',fontname = 'Arial',style='filled',fillcolor='gray98',fontcolor='antiquewhite4')

    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render('test-output/Visualization.gv', view=True)