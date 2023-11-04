import json
from typing import Any


with open("config.json", "r") as fp:
    config: dict[Any, Any] = json.load(fp)


def feature_enabled(feature_name: str) -> bool:
    return config["FEATURES"][feature_name] if feature_name in config["FEATURES"] else False