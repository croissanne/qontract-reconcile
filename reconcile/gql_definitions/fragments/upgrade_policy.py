"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterUpgradePolicyConditionsV1(ConfiguredBaseModel):
    mutexes: Optional[list[str]] = Field(..., alias="mutexes")
    soak_days: Optional[int] = Field(..., alias="soakDays")
    sector: Optional[str] = Field(..., alias="sector")


class ClusterUpgradePolicy(ConfiguredBaseModel):
    workloads: list[str] = Field(..., alias="workloads")
    schedule: str = Field(..., alias="schedule")
    conditions: ClusterUpgradePolicyConditionsV1 = Field(..., alias="conditions")
