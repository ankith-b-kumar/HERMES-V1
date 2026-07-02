from app.ranking.behavior_adjustment import BehaviorAdjustment
from app.ranking.behavior_assessment import BehaviorAssessment


def test_behavior_bonus():

    adjustment = BehaviorAdjustment()

    score = adjustment.apply(
        0.80,
        BehaviorAssessment(
            score=1.0,
            leadership=1.0,
            ownership=1.0,
            communication=1.0,
            impact=1.0,
        ),
    )

    assert abs(score - 0.84) < 1e-6


def test_zero_behavior_bonus():

    adjustment = BehaviorAdjustment()

    score = adjustment.apply(
        0.80,
        BehaviorAssessment(
            score=0.0,
            leadership=0.0,
            ownership=0.0,
            communication=0.0,
            impact=0.0,
        ),
    )

    assert abs(score - 0.80) < 1e-6