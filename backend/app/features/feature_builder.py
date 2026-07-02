from app.features.feature_build_input import FeatureBuildInput
from app.features.feature_extractor import FeatureExtractor
from app.features.feature_normalizer import FeatureNormalizer
from app.features.feature_vector import FeatureVector


class FeatureBuilder:
    """
    Builds a normalized FeatureVector.

    Coordinates extraction and normalization.
    """

    def __init__(self):
        self.extractor = FeatureExtractor()
        self.normalizer = FeatureNormalizer()

    def build(
        self,
        feature_input: FeatureBuildInput,
    ) -> FeatureVector:

        features = self.extractor.extract(
            candidate=feature_input.candidate,
            retrieval_scores=feature_input.retrieval_scores,
            intelligence_scores=feature_input.intelligence_scores,
        )

        return self.normalizer.normalize(features)