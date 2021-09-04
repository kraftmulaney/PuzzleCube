import matplotlib.colors as mcolors
import numpy as np

class CubePrettyPrinter():
    # Static parameters
    __print_divider = "  |  "
    __print_divider_footer = "__|__"
    __print_cell_width = 8

    def __init__(self, side_len):
        self.__side_len = side_len

    def __print_header(self):
        return "_" * ((self.__side_len * self.__side_len * CubePrettyPrinter.__print_cell_width)
            + len(CubePrettyPrinter.__print_divider) * 2) + "\n"

    def __print_emptyrow(self):
        result = ""
        for z in range(0, self.__side_len - 1):
            result = result + " " * (CubePrettyPrinter.__print_cell_width * self.__side_len)
            result = result + CubePrettyPrinter.__print_divider

        result = result + "\n"
        return result

    def __print_footer(self):
        result = ""
        for z in range(0, self.__side_len):
            result = result + "_" * (CubePrettyPrinter.__print_cell_width * self.__side_len)
            if (z != self.__side_len - 1):
                result = result + CubePrettyPrinter.__print_divider_footer

        return result

    def __print_cube_row(self, row, z, cube_values):
        result = ""
        for x in range(0, self.__side_len):
            color = cube_values[x, row, z]
            color = "." if (color == "") else color
            result = result + \
                color[0:CubePrettyPrinter.__print_cell_width].ljust(CubePrettyPrinter.__print_cell_width)
        return result

    def __print_all_rows(self, row, cube_values):
        result = ""
        for z in range(0, self.__side_len):
            result = result + self.__print_cube_row(row, z, cube_values)
            if (z != self.__side_len - 1):
                result = result + CubePrettyPrinter.__print_divider
        return result

    def pretty_print_cube(self, cube_values):
        result = self.__print_header()
        result = result + self.__print_emptyrow()
        for y in range(0, self.__side_len):
            result = result + self.__print_all_rows(y, cube_values)
            if (y != self.__side_len - 1):
                result = result + "\n" + self.__print_emptyrow()

        result = result + "\n" + self.__print_footer()
        return result
