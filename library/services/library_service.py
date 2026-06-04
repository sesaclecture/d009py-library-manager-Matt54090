from __future__ import annotations
from typing import Iterable, List
from library.models.book import Book
from library.services.base_service import BaseService

"""
TODO:
      - 내부 상태를 캡슐화하기 위해 _books(list[Book])를 사용
      - add_book/remove_book/list_books/find_book 구현
      - 존재하지 않는 책 삭제/검색 시 ValueError 발생
"""

class LibraryService(BaseService):
    """도서 목록을 메모리에서 관리하는 서비스.
    [상속] LibraryService(BaseService)
    - 괄호 안의 BaseService를 '부모'로 물러받음
    - 부모는 추상 클래스라 add_book, remove_book, list_book, find_book
      4개를 구현하라고 약속한 상태
    - 그래서 자식 클래스가 위의 4개를 실제 동작으로 각각 채움(다형성)
    """
    # 객체가 처음 만들어질 때, 내부 상태를 준비
    def __init__(self) -> None:
        # TODO: 내부 리스트 초기화
        """[캡슐화]
        - 책들을 리스트로 묶은 이유 : 넣는 순서가 그대로 유지되기 때문
        """
        # 빈 리스트로 시작함
        self._books: list[book] = []    # 변수 앞 밑줄 : 클래스 내부에만 쓰는 값

    def add_book(self, book: Book) -> None:
        """책 한 권을 목록 '맨 뒤'에다 추가함
        - list.append()는 리스트 끝에 ()의 인자를 붙임. 넣는 순서가 유지
        """
        # TODO: 책 추가
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        """
        - 처음부터 목록을 보면서 제목이 같은 책을 찾음
        - 찾은 책을 리스트에서 제거/종료
        - 끝까지 책을 못 찾으면, ValueError 
        """
        # TODO: 제목으로 책 삭제 (없으면 ValueError)
        # enumerate(목록) : 순서(번호 index와 값 book)쌍을 하나씩 꺼냄
        for index, book in enumerate(self._books):
            if book.title == title:
                del self._books[index]  # 해당 위치의 항목(제목 일치O)을 리스트에서 삭제
                return                  # 작업 종료
        raise ValueError(f"삭제할 책을 찾을 없습니다: {title}")

    # 현재 가지고 있는 책의 목록을 되돌려줌
    def list_books(self) -> Iterable[Book]:
        """[복사본] 주는 이유는?
        - self._books 그대로 하여 리스트를 수정하는 경우 서비스 내부의 진짜 목록까지
          함께 바뀌기 때문에 -> '캡슐화' 깨짐
        - list()로 새 리스트를 만들면, 내부 원본은 보호하면서 따로 설정 가능하기 때문
        """
        # TODO: 책 목록 반환 (복사본 반환 권장)
        return list(self._books)

    # 제목이 일치하는 책을 찾아서 돌려줌. 없으면 ValueError
    def find_book(self, title: str) -> Book:
        """
        - 목록을 쭉 살피면서 같은 제목의 책을 찾으면 즉시 해당 책을 반환함
        - 만약 끝까지 못 찾으면 ValueError
        """
        # TODO: 제목으로 책 찾기 (없으면 ValueError)
        for book in self._books:
            if book.title == title:
                return book
        raise ValueError(f"책을 찾을 수 없습니다: {title}")