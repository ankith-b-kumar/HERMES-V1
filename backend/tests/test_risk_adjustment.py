from app.ranking.risk_adjustment import RiskAdjustment
from app.ranking.risk_assessment import RiskAssessment


def test_no_risk():

    adjustment = RiskAdjustment()

    score = adjustment.apply(
        0.8,
        RiskAssessment(
            score=0.0,
        ),
    )

    assert abs(score - 0.8) < 1e-6


def test_full_risk():

    adjustment = RiskAdjustment()

    score = adjustment.apply(
        1.0,
        RiskAssessment(
            score=1.0,
            reasons=[
                "Multiple inconsistencies"
            ],
        ),
    )

    assert abs(score - 0.8) < 1e-6


def test_half_risk():

    adjustment = RiskAdjustment()

    score = adjustment.apply(
        1.0,
        RiskAssessment(
            score=0.5,
            reasons=[
                "Employment gap"
            ],
        ),
    )

    assert abs(score - 0.9) < 1e-6