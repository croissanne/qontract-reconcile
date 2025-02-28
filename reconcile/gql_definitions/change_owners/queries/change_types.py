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


DEFINITION = """
query ChangeTypes($name: String) {
  change_types: change_types_v1(name: $name) {
    name
    description
    priority
    contextType
    contextSchema
    disabled
    changes {
      provider
      changeSchema
      ... on ChangeTypeChangeDetectorJsonPathProvider_v1 {
        jsonPathSelectors
        context {
          selector
          when
        }
      }
      ... on ChangeTypeChangeDetectorChangeTypeProvider_v1 {
        changeTypes {
          name
          contextSchema
        }
        ownership_context: context {
          selector
          when
        }
      }
    }
    implicitOwnership {
      provider
      ... on ChangeTypeImplicitOwnershipJsonPathProvider_v1 {
        jsonPathSelector
      }
    }
    inherit {
      name
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union = True
        extra = Extra.forbid


class ChangeTypeChangeDetectorV1(ConfiguredBaseModel):
    provider: str = Field(..., alias="provider")
    change_schema: Optional[str] = Field(..., alias="changeSchema")


class ChangeTypeChangeDetectorContextSelectorV1(ConfiguredBaseModel):
    selector: str = Field(..., alias="selector")
    when: Optional[str] = Field(..., alias="when")


class ChangeTypeChangeDetectorJsonPathProviderV1(ChangeTypeChangeDetectorV1):
    json_path_selectors: list[str] = Field(..., alias="jsonPathSelectors")
    context: Optional[ChangeTypeChangeDetectorContextSelectorV1] = Field(
        ..., alias="context"
    )


class ChangeTypeChangeDetectorChangeTypeProviderV1_ChangeTypeV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    context_schema: Optional[str] = Field(..., alias="contextSchema")


class ChangeTypeChangeDetectorChangeTypeProviderV1_ChangeTypeChangeDetectorContextSelectorV1(
    ConfiguredBaseModel
):
    selector: str = Field(..., alias="selector")
    when: Optional[str] = Field(..., alias="when")


class ChangeTypeChangeDetectorChangeTypeProviderV1(ChangeTypeChangeDetectorV1):
    change_types: list[
        ChangeTypeChangeDetectorChangeTypeProviderV1_ChangeTypeV1
    ] = Field(..., alias="changeTypes")
    ownership_context: ChangeTypeChangeDetectorChangeTypeProviderV1_ChangeTypeChangeDetectorContextSelectorV1 = Field(
        ..., alias="ownership_context"
    )


class ChangeTypeImplicitOwnershipV1(ConfiguredBaseModel):
    provider: str = Field(..., alias="provider")


class ChangeTypeImplicitOwnershipJsonPathProviderV1(ChangeTypeImplicitOwnershipV1):
    json_path_selector: str = Field(..., alias="jsonPathSelector")


class ChangeTypeV1_ChangeTypeV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class ChangeTypeV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    description: str = Field(..., alias="description")
    priority: str = Field(..., alias="priority")
    context_type: str = Field(..., alias="contextType")
    context_schema: Optional[str] = Field(..., alias="contextSchema")
    disabled: Optional[bool] = Field(..., alias="disabled")
    changes: list[
        Union[
            ChangeTypeChangeDetectorJsonPathProviderV1,
            ChangeTypeChangeDetectorChangeTypeProviderV1,
            ChangeTypeChangeDetectorV1,
        ]
    ] = Field(..., alias="changes")
    implicit_ownership: Optional[
        list[
            Union[
                ChangeTypeImplicitOwnershipJsonPathProviderV1,
                ChangeTypeImplicitOwnershipV1,
            ]
        ]
    ] = Field(..., alias="implicitOwnership")
    inherit: Optional[list[ChangeTypeV1_ChangeTypeV1]] = Field(..., alias="inherit")


class ChangeTypesQueryData(ConfiguredBaseModel):
    change_types: Optional[list[ChangeTypeV1]] = Field(..., alias="change_types")


def query(query_func: Callable, **kwargs: Any) -> ChangeTypesQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        ChangeTypesQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return ChangeTypesQueryData(**raw_data)
