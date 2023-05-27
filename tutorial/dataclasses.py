{
    "field": "name",
    "limit": 10,
    "offset": 10,
    "filter": {
        "keyword": "John Doe",
        "case_sensitive": True,
    },
}
from dataclasses import dataclass
from typing import Optional

@dataclass
class FilterObject:
    keyword: str
    case_sensitive: Optional[bool] = True

    @classmethod
    def from_json(cls, data:dict):
        return cls(
            keyword = data.get('keyword'),
            case_sensitive = data.get('case_sensitive')
        )


@dataclass
class TutorialRequestBody:
    field: str
    filter: FilterObject
    limit: Optional[int] = 10
    offset: Optional[int] = 10

    @classmethod
    def from_json(cls, data:dict):
        return cls(
            field = data.get('field'),
            limit = data.get('limit'),
            offset = data.get('offset'),
            filter = FilterObject.from_json(data.get('filter'))
        )