"""
Company Taxonomy

Groups companies into categories that provide
useful signals during ranking.
"""

from collections import defaultdict


class CompanyTaxonomy:
    def __init__(self):
        self.graph = defaultdict(set)
        self._build()

    def _add(self, category: str, company: str):
        self.graph[category].add(company)

    def _build(self):

        # Big Tech

        for company in [
            "Google",
            "Microsoft",
            "Amazon",
            "Meta",
            "Apple",
            "Netflix"
        ]:
            self._add("Big Tech", company)

        # AI Research

        for company in [
            "OpenAI",
            "Anthropic",
            "DeepMind",
            "Cohere",
            "Hugging Face"
        ]:
            self._add("AI Research", company)

        # Semiconductor / AI Hardware

        for company in [
            "NVIDIA",
            "AMD",
            "Intel",
            "Qualcomm"
        ]:
            self._add("AI Hardware", company)

        # Cloud Providers

        for company in [
            "AWS",
            "Microsoft Azure",
            "Google Cloud"
        ]:
            self._add("Cloud Providers", company)

        # IT Services

        for company in [
            "TCS",
            "Infosys",
            "Wipro",
            "Accenture",
            "Capgemini",
            "Cognizant",
            "HCL"
        ]:
            self._add("IT Services", company)

        # Startups

        for company in [
            "Scale AI",
            "Perplexity",
            "Mistral AI"
        ]:
            self._add("AI Startup", company)

    def companies(self, category: str):
        return sorted(self.graph.get(category, []))

    def all_categories(self):
        return sorted(self.graph.keys())

    def all_companies(self):
        companies = set()

        for values in self.graph.values():
            companies.update(values)

        return sorted(companies)