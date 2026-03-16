from typing import Any

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

class LRBuilder:
    def build(self, params: dict) -> LogisticRegression:
        model = LogisticRegression(**params)
        return model

class RFBuilder:
    def build(self, params: dict) -> RandomForestClassifier:
        model = RandomForestClassifier(**params)
        return model

class XGBBuilder:
    def build(self, params: dict) -> XGBClassifier:
        model = XGBClassifier(**params)
        return model


class ModelFactory:
    _builders = {
        "RandomForest": RFBuilder(),
        "XGBoost": XGBBuilder(),
        "LogisticRegression": LRBuilder()
    }

    @classmethod
    def create_model(cls, model_name: str, params: dict) -> Any:
        """
        model name에 해당하는 모델에 params 적용하여 모델 객체 생성 후 반환
        """
        builder = cls._builders.get(model_name)
        if not builder:
            raise ValueError(f"❌ 지원하지 않는 모델입니다: {model_name}")
        return builder.build(params)