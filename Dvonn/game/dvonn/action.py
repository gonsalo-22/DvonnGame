class DvonnAction:
    __org__col: int
    __org__row: int
    __dst__col: int
    __dst__row: int

    def __init__(self, org_col: int, org_row: int, dst_col: int, dst_row: int):
        self.__org__col = org_col
        self.__org__row = org_row
        self.__dst__row = dst_row
        self.__dst__col = dst_col

    def get_org_col(self):
        return self.__org__col

    def get_org_row(self):
        return self.__org__row

    def get_dst_col(self):
        return self.__dst__col

    def get_dst_row(self):
        return self.__dst__row
