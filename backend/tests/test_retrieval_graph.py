from app.knowledge.retrieval_graph import RetrievalGraph


def test_retrieval_graph():

    graph = RetrievalGraph()

    print()

    print("Machine Learning Engineer")
    print(graph.related("Machine Learning Engineer"))

    print()

    print("Generative AI Engineer")
    print(graph.related("Generative AI Engineer"))

    print()

    print("Total Nodes")
    print(len(graph.all_nodes()))