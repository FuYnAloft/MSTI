from collections.abc import Iterable, Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DimExplanation:
    L: str
    M: str
    H: str


@dataclass(frozen=True, slots=True)
class DimThreshold:
    lowMax: int
    midMax: int


@dataclass(frozen=True, slots=True)
class Dimension:
    id: str
    name: str
    model: str
    explanation: DimExplanation
    thresholds: DimThreshold = DimThreshold(3, 4)


@dataclass(frozen=True, slots=True)
class Option:
    label: str
    value: int


def options(*labels: str) -> list[Option]:
    return [Option(label, i + 1) for i, label in enumerate(labels)]


@dataclass(frozen=True, slots=True)
class QuestionDependency:
    questionId: str
    answerValue: int


@dataclass(frozen=True, slots=True)
class Question:
    id: str
    dim: str | None
    text: str
    options: Iterable[Option]
    dependsOn: QuestionDependency | None = None


@dataclass(frozen=True, slots=True)
class Type:
    code: str
    cn: str
    intro: str
    desc: str
    image: str
    pattern: str


@dataclass(frozen=True, slots=True)
class Xxbi:
    dimensions: Sequence[Dimension]
    questions: Sequence[Question]
    types: Sequence[Type]
