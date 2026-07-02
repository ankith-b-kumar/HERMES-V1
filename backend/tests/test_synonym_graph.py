from app.knowledge.synonym_graph import SynonymGraph


def test_synonym_graph():

    graph = SynonymGraph()

    print()

    print(graph.normalize("ML"))
    print(graph.normalize("LLM"))
    print(graph.normalize("CV"))
    print(graph.normalize("GenAI"))
    print(graph.normalize("K8s"))

    print()

    print("Entries")
    print(graph.size())