import json
from dataclasses import dataclass
import subprocess


@dataclass
class PhysicalSize:
    width: int
    height: int


@dataclass
class OutputMode:
    width: int
    height: int
    refresh: float
    preferred: bool
    current: bool


@dataclass
class OutputPosition:
    x: int
    y: int


@dataclass
class Output:
    name: str
    description: str
    make: str
    model: str
    serial: str
    physical_size: PhysicalSize
    enable: bool
    modes: list[OutputMode]
    position: OutputPosition
    transform: str
    scale: float
    adaptive_sync: bool


@dataclass
class Outputs:
    outputs: list[Output]


def wlr_randr() -> Outputs:
    cp = subprocess.run(
        ["wlr-randr", "--json"],
        capture_output=True,
    )
    data = json.loads(cp.stdout)
    return Outputs(**data)
