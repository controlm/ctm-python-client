import graphviz
from aapi import Folder, SubFolder, SimpleFolder
from ctm_python_client.core.workflow import BaseWorkflow


def get_subgraph(obj, name, current_path):
    if not(
        isinstance(obj, Folder) or
        isinstance(obj, SubFolder) or
        isinstance(obj, SimpleFolder)
    ):
        return
    sgraph = graphviz.Digraph(name, graph_attr={'label':obj.object_name}, node_attr={'shape':'oval'})
    for o in obj.job_list:
        sgraph.node(f'{current_path}/{o.object_name}', o.object_name)

    for i,o in enumerate(obj.sub_folder_list):
        sgraph.subgraph(get_subgraph(o, f'cluster_{current_path}_{i}', current_path+'/'+o.object_name))

    return sgraph

def get_graph(workflow : BaseWorkflow):
    dgraph = graphviz.Digraph(name='root', graph_attr={
        'rankdir': 'LR',
        'compound': 'true'
    },
    node_attr={'shape':'oval'}
    )
    i = 0
    for k, v in workflow._definitions.items():
        if not(
            isinstance(v, Folder) or
            isinstance(v, SubFolder) or
            isinstance(v, SimpleFolder)
        ):
            continue
        cluster = graphviz.Digraph(f'cluster_{i}', graph_attr={
            'label': v.object_name
        })

        for o in v.job_list:
            cluster.node(f'{v.object_name}/{o.object_name}', o.object_name)

        for i,o in enumerate(v.sub_folder_list):
            cluster.subgraph(get_subgraph(o,f'cluster_{v.object_name}/{o.object_name}_{i}',v.object_name+'/'+o.object_name))
        

        dgraph.subgraph(cluster)
        i += 1

    for conn in workflow._connections.values():
        for o in conn:
            dgraph.edge(o[0],o[1])

    return dgraph
