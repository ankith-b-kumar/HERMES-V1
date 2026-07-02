from copy import deepcopy

from app.features.feature_schema import FEATURE_SCHEMA
from app.features.feature_vector import FeatureVector


class FeatureNormalizer:
    """
    Schema-driven feature normalization.
    """

    @staticmethod
    def _clip(value: float) -> float:
        return max(0.0, min(1.0, value))

    @staticmethod
    def _min_max(value: float, minimum: float, maximum: float) -> float:
        if maximum <= minimum:
            return 0.0

        return max(
            0.0,
            min(
                1.0,
                (value - minimum) / (maximum - minimum),
            ),
        )

    def normalize(
        self,
        features: FeatureVector,
    ) -> FeatureVector:

        normalized = deepcopy(features)

        for feature_name, config in FEATURE_SCHEMA.items():

            value = getattr(normalized, feature_name)

            method = config["method"]

            if method == "clip":

                value = self._clip(value)

            elif method == "min_max":

                value = self._min_max(
                    value,
                    config["min"],
                    config["max"],
                )

            setattr(
                normalized,
                feature_name,
                value,
            )

        return normalized