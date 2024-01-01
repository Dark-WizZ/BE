import graphviz

def create_nfa_diagram():
    # Create a directed graph
    graph = graphviz.Digraph(format='png',graph_attr={'rankdir': 'LR'})

    # Add nodes
    graph.node('q0', shape='circle')  # Initial state
    graph.node(str(1), shape='doublecircle', color='black')  # Accepting state

    # Add edges with label 'a' and loop on 'q0' for 'a*'
    graph.edge('q0', 'q0', label='a')
    graph.edge('q0', str(1), label='e')

    return graph


graph = create_nfa_diagram()
graph.view()
