from collections.abc import Iterable, Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Option:
    """选项定义"""
    label: str  # 选项文本
    scores: dict[str, int]  # 对人格类型的加分映射


def options(personality: str | None, *labels: str, descending: bool = False) -> list[Option]:
    """
    生成选项，分值为 1, 2, 3, ...；当 personality 为 None 时不加分。
    :param personality: 人格类型（可为 None）
    :param labels: 选项的文本
    :param descending: 是否递减加分（例如 3, 2, 1）
    :return: 生成的选项
    """
    score_values = list(range(1, len(labels) + 1))
    if descending:
        score_values.reverse()
    result: list[Option] = []
    for i, label in enumerate(labels):
        score_map = {personality: score_values[i]} if personality else {}
        result.append(Option(label=label, scores=score_map))
    return result


@dataclass(frozen=True, slots=True)
class QuestionDependency:
    """问题依赖，用于在特定问题回答特定选项后展示本问题"""
    questionId: str
    answerValue: int


@dataclass(frozen=True, slots=True)
class Question:
    """问题定义"""
    id: str
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
    code: str  # 类型的编码
    cn: str  # 类型中文名
    intro: str  # 类型简介
    desc: str  # 类型描述
    image: str  # 类型图片


@dataclass(frozen=True, slots=True)
class Xxbi:
    topN: int
    questions: Sequence[Question]
    types: Sequence[Type]
