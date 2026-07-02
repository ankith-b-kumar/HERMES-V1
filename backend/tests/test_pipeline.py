from app.agents.orchestrator import Orchestrator
from app.models.candidate import Candidate


def test_pipeline():

    candidate = Candidate(
        id="1",
        name="John Doe",
        current_role="Machine Learning Engineer",
        years_of_experience=5,

        skills=[
            "Python",
            "PyTorch",
            "Docker",
            "Git"
        ],

        experience=[
            {
                "company": "ABC AI",
                "title": "ML Engineer"
            },
            {
                "company": "XYZ Labs",
                "title": "Software Engineer"
            }
        ]
    )

    job_description = """
    Looking for a Machine Learning Engineer.

    Required Skills:
    Python
    PyTorch
    Docker
    TensorFlow

    Experience:
    3+ years

    Bachelor's degree preferred.
    """

    orchestrator = Orchestrator()

    result = orchestrator.run(
        {
            "candidate": candidate,
            "job_description": job_description
        }
    )

    print("\n========== JOB PROFILE ==========")
    print(result["job_profile"])

    print("\n========== CAREER PROFILE ==========")
    print(result["career_profile"])

    print("\n========== SKILL PROFILE ==========")
    print(result["skill_profile"])

    print("\n========== FEATURE VECTOR ==========")
    print(result["feature_vector"])
    
    
if __name__ == "__main__":
    test_pipeline()