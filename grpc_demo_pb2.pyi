from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateItemSchema(_message.Message):
    __slots__ = ["title"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Item(_message.Message):
    __slots__ = ["created_at", "id", "title"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    created_at: str
    id: str
    title: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., created_at: _Optional[str] = ...) -> None: ...

class ItemId(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListItemsPagination(_message.Message):
    __slots__ = ["page", "page_length"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_length: int
    def __init__(self, page: _Optional[int] = ..., page_length: _Optional[int] = ...) -> None: ...

class ListItemsSchema(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class UpdateItemSchema(_message.Message):
    __slots__ = ["id", "title"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
