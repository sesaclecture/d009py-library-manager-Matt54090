
from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, Dict, Any

# 필드 자동 처리
@dataclass
class Book:
    """책 정보를 표현하는 데이터 클래스.
    TODO: 아래 요구사항을 만족하도록 구현을 보완하세요.
    - 인스턴스 변수: title(str), author(str), year(int)
    - 클래스 변수: book_count(int) — 생성될 때마다 +1
    - __str__는 "{title} by {author} ({year})" 형식 반환
    - @classmethod from_dict(cls, data: Dict[str, Any]) -> Book 구현
    """
    # -- 인스턴스 변수(필드) --
    title: str
    author: str
    year: int

    # TODO: 클래스 변수 book_count 선언 및 증가 로직 추가
    # 모든 객체가 따로 카운트를 갖는 것이 아닌, 클래스 전체가 공유헤야 하는 변수로 설정
    book_count: ClassVar[int] = 0

    def __post_init__(self) -> None:
        """@dataclass가 만든 __init__이 끝나고, 자동 호출되는 특별 메서드.
        여기에서 책이 새로 만들어지면 공유 카운터 +1.
        - book.book_count 는 클래스가 지닌 "하나뿐인" 값이라, 어떤 객체를 만들던지 같은 값이 함께 올라감.
        """
        # 공유 카운터 +1
        Book.book_count += 1
    
    # TODO: 생성 시 book_count 증가
    # book_count: int = 0  # 힌트: dataclass의 필드가 아닌 클래스 속성으로 선언
    
    ## @dataclass가 제목,작가,출시연도 받는 __init__ 생성하는데, 이 비어있는 __init__이 덮어써는 문제발생.
    # def __init__(self):
    #     pass

    def __str__(self) -> str:
        # TODO: 지정된 문자열 포맷 반환
        # e.g. 책이름 by 지은이 (2001)
        """str(book)이나 print(book) 했을 때 보여주는 읽기 편한 문자열
           지정된 형식: "{제목} by {지은이} ({연도})"
           예시: "책 이름 by 지은이 (1999)"
        """
        return f"{self.title} by {self.author} ({self.year})"


    # 첫 번째 인자로 self(객체)가 아닌 클래스 자신을 받음
    @classmethod
    # 딕셔너리를 받아서 Book의 객체를 만듦
    def from_dict(cls, data: Dict[str, Any]) -> "Book": # cls == Book
        # 나중에 Book 상속하는 자식 클래스가 from_dict 호출하면 그 '자식 타입으로 만들어 줘서
        # TODO: dict에서 title/author/year를 읽어 Book 생성
        return cls(
            title = data["title"],
            author = data["author"],
            year = data["year"],
        )
