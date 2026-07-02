from app.knowledge.ai_ontology import AIOntology


def test_ai_ontology():

    ontology = AIOntology()

    print()

    print("AI Children")
    print(ontology.children("Artificial Intelligence"))

    print()

    print("Deep Learning")
    print(ontology.children("Deep Learning"))

    print()

    print("Total Nodes")
    print(len(ontology.all_nodes()))