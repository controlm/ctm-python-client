from ctm_python_client.core.bmc_control_m import CmJobFlow
from graphviz import Digraph


class DisplayDAG:
    def __init__(self, cm_job_flow: CmJobFlow):
        self.flow = cm_job_flow

    def display_graphviz(self):
        print("=========== Jobflow Details ===================")
        print("Application: ", self.flow.application)
        print("Sub Application: ", self.flow.sub_application)
        print("Folder Name: {0} \n\n\n".format(self.flow.folders[0][0]))

        nodes, edges = self.flow.get_nodes_and_edges()

        graph = Digraph("G", filename="temp.gv")
        # self.g.attr(rankdir='LR', size='8,5',  shape='rectangle')
        graph.attr(shape="ellipse")
        for node in nodes:
            graph.node(node[0])
        for edge in edges:
            graph.edge(edge[0], edge[1], style=edge[2])
            print(edge)
        return graph
