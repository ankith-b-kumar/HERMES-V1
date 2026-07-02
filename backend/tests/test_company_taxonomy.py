from app.knowledge.company_taxonomy import CompanyTaxonomy


def test_company_taxonomy():

    taxonomy = CompanyTaxonomy()

    print()

    print("Big Tech")
    print(taxonomy.companies("Big Tech"))

    print()

    print("AI Research")
    print(taxonomy.companies("AI Research"))

    print()

    print("Categories")
    print(taxonomy.all_categories())

    print()

    print("Companies")
    print(len(taxonomy.all_companies()))