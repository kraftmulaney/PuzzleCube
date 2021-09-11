from abc import ABC, abstractmethod

class ICheckCubeCondition(ABC):
    def __init__(self, cube):
        super().__init__(cube)

    @abstractmethod
    def check_cube(self) -> bool:
        pass
