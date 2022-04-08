from dataclasses import dataclass, field


@dataclass
class ValidationResponse:
    status: str
    details: str = ""
