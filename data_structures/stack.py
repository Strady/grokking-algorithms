import dataclasses
import typing

StackType = typing.TypeVar('StackType')


class EmptyStackError(Exception):
    """Raised on attempt to pop from empty stack"""


@dataclasses.dataclass
class StackElement(typing.Generic[StackType]):
    value: StackType
    previous: 'typing.Optional[StackElement[StackType]]'


class Stack(typing.Generic[StackType]):

    def __init__(self):
        self._top: typing.Optional[StackElement] = None

    def push(self, value: StackType) -> None:
        self._top = StackElement(value=value, previous=self._top)

    def pop(self) -> StackElement:
        if self.empty:
            raise EmptyStackError('Stack is empty')
        value = self._top.value
        self._top = self._top.previous
        return value

    @property
    def empty(self) -> bool:
        return self._top is None

    def print_stack(self):
        if self.empty:
            print('Stack is empty')
        elements = []
        current: StackElement = self._top
        while current:
            elements.append(current.value)
            current = current.previous
        print('->'.join(elements))


stack: Stack[str] = Stack()

stack.push('some')
stack.push('random')
stack.push('elements')
stack.push('set')
stack.print_stack()
while not stack.empty:
    print(stack.pop())
    stack.print_stack()

try:
    stack.pop()
except EmptyStackError as e:
    print(e)
