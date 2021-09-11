from src.irules import ICheckCubeCondition

class CheckIfCubeFull(ICheckCubeCondition):
    def __init__(self, cube):
        self.__cube = cube

    def check_cube(self):
        return self.__cube.is_full
