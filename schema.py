from collections.abc import Iterable, Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DimExplanation:
    """维度的不同等级的解释"""
    L: str
    M: str
    H: str



@dataclass(frozen=True, slots=True)
class DimThreshold:
    """判定维度属于 L/M/H 的阈值"""
    lowMax: int
    midMax: int



@dataclass(frozen=True, slots=True)
class Dimension:
    """维度定义"""
    id: str  # 维度ID
    name: str  # 维度中文名
    model: str  # 维度模型归类
    explanation: DimExplanation  # 维度的不同等级的解释
    thresholds: DimThreshold = DimThreshold(3, 4)  # 判定维度属于 L/M/H 的阈值


@dataclass(frozen=True, slots=True)
class Option:
    """选项定义"""
    label: str  # 选项文本
    value: int  # 选项的分值


def options(*labels: str) -> list[Option]:
    """
    生成选项，分值为 1, 2, 3, ...
    :param labels: 选项的文本
    :return: 生成的选项
    """
    return [Option(label, i + 1) for i, label in enumerate(labels)]


@dataclass(frozen=True, slots=True)
class QuestionDependency:
    """问题依赖，用于在特定问题回答特定选项后展示本问题"""
    questionId: str
    answerValue: int


@dataclass(frozen=True, slots=True)
class Question:
    """问题定义"""
    id: str
    dim: str | None # 维度的 ID
    text: str
    options: Iterable[Option]
    dependsOn: QuestionDependency | None = None


_q_counter = 0


def qauto():
    """
    自动生成递增的问题 ID
    :return: 生成的ID
    """
    global _q_counter
    _q_counter += 1
    return f'q{_q_counter}'


@dataclass(frozen=True, slots=True)
class Type:
    """人格类型"""
    code: str # 类型的编码
    cn: str # 类型中文名
    intro: str # 类型简介
    desc: str # 类型描述
    image: str # 类型图片
    pattern: str # 类型的维度模式


@dataclass(frozen=True, slots=True)
class Xxbi:
    dimensions: Sequence[Dimension]
    questions: Sequence[Question]
    types: Sequence[Type]
