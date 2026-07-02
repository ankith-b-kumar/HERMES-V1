from app.knowledge.skill_graph import SkillGraph


def test_skill_graph():

    graph = SkillGraph()

    print()

    print("Python")
    print(graph.children("Python"))

    print()

    print("Deep Learning")
    print(graph.children("Deep Learning"))

    print()

    print("AWS")
    print(graph.children("AWS"))

    print()

    print("Total Nodes")
    print(len(graph.all_nodes()))