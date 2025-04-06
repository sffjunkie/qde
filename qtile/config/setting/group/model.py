from pydantic import BaseModel


class GroupDefinition(BaseModel):
    name: str
    layout: str
    matches: list[str] | None


GroupDefinitions = list[GroupDefinition]


class GroupConfiguration(BaseModel):
    layout: str
    decoration: str | None
    groups: GroupDefinitions
