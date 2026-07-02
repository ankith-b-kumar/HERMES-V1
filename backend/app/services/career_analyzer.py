from app.models.candidate import Candidate
from app.models.career_profile import CareerProfile


class CareerAnalyzer:

    def analyze(self, candidate: Candidate) -> CareerProfile:

        profile = CareerProfile()

        profile.total_experience_years = candidate.years_of_experience

        profile.current_role = candidate.current_role

        profile.number_of_roles = len(candidate.experience)

        companies = []
        titles = []

        for exp in candidate.experience:

            if "company" in exp:
                companies.append(exp["company"])

            if "title" in exp:
                titles.append(exp["title"])

        profile.companies = companies
        profile.job_titles = titles

        profile.number_of_companies = len(set(companies))

        return profile