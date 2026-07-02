from app.knowledge.role_ontology import RoleOntology


def test_role_ontology():
    ontology = RoleOntology()

    print()

    print("AI Roles")
    print(ontology.children("Artificial Intelligence Engineer"))

    print()

    print("Software Roles")
    print(ontology.children("Software Engineer"))

    print()

    print("Total Nodes")
    print(len(ontology.all_nodes()))