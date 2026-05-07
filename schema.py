from collections.abc import Iterable, Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Option:
    """
    选项定义
    :param label: 选项的文本内容
    :param scores: 对人格类型的加分映射，格式为 {人格代码: 分值}
    """
    label: str
    scores: dict[str, int]


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
    """
    问题依赖，用于在特定问题回答特定选项后展示本问题
    :param questionId: 依赖的问题 ID
    :param answerValue: 依赖的问题的选项序号
    """
    questionId: str
    answerValue: int


@dataclass(frozen=True, slots=True)
class Question:
    """
    问题定义
    :param id: 问题 ID，必须唯一
    :param text: 问题文本
    :param options: 选项列表
    :param dependsOn: 可选的依赖定义，如果存在则只有在满足依赖条件时才展示该问题
    """
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
    """
    人格类型
    :param code: 人格类型的编码，必须唯一
    :param cn: 人格类型的中文名称
    :param intro: 人格类型的简介
    :param desc: 人格类型的详细描述
    :param image: 人格类型的图片 URL
    """
    code: str
    cn: str
    intro: str
    desc: str
    image: str


@dataclass(frozen=True, slots=True)
class Xxbi:
    topN: int
    questions: Sequence[Question]
    types: Sequence[Type]
