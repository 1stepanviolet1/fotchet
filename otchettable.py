from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side


class OtchetTable(Workbook):
    A1_L1 = 'Отчет о результатах самостоятельной работы обучающегося по дисциплинам\n"Физическая культура" или "Элективные курсы по физической культуре и спорту"'

    A3 = '''Студ. билет'''

    B3_E3 = '''ФИО'''

    F3 = '''Группа'''

    G3_I3 = '''Спортивное отделение'''

    J3_L3 = '''Преподаватель'''

    def __init__(self, iso_dates=False) -> None:
        super().__init__(iso_dates=iso_dates)

        _sheet = self.active

        _sheet.row_dimensions[1].height = 55
        _sheet.row_dimensions[3].height = 25

        _sheet.column_dimensions['A'].width = 15
    
    def init_A1_L1(self):
        _sheet = self.active

        _sheet.merge_cells("A1:L1")

        _sheet["A1"].font = Font(size=14, bold=True)
        _sheet["A1"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["A1"].value = self.A1_L1
    
    def init_A3(self):
        _sheet = self.active

        _sheet["A3"].font = Font(size=11, bold=True)
        _sheet["A3"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["A3"].value = self.A3

        _sheet["A4"].alignment = Alignment(horizontal="center", vertical="center")
    
    def init_B3_E3(self):
        _sheet = self.active

        _sheet.merge_cells("B3:E3")
        _sheet.merge_cells("B4:E4")

        _sheet["B3"].font = Font(size=11, bold=True)
        _sheet["B3"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["B3"].value = self.B3_E3

        _sheet["B4"].alignment = Alignment(horizontal="center", vertical="center")
    
    def init_F3(self):
        _sheet = self.active

        _sheet["F3"].font = Font(size=11, bold=True)
        _sheet["F3"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["F3"].value = self.F3

        _sheet["F4"].alignment = Alignment(horizontal="center", vertical="center")

    def init_G3_I3(self):
        _sheet = self.active

        _sheet.merge_cells("G3:I3")
        _sheet.merge_cells("G4:I4")
        
        _sheet["G3"].font = Font(size=11, bold=True)
        _sheet["G3"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["G3"].value = self.G3_I3

        _sheet["G4"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["G4"].value = "Шахматы"
    
    def init_J3_L3(self):
        _sheet = self.active

        _sheet.merge_cells("J3:L3")
        _sheet.merge_cells("J4:L4")
        
        _sheet["J3"].font = Font(size=11, bold=True)
        _sheet["J3"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["J3"].value = self.J3_L3

        _sheet["J4"].alignment = Alignment(horizontal="center", vertical="center")
        _sheet["J4"].value = "Иванов С.В."
    
    def set_borders(self):
        _sheet = self.active

        for col in "ABCDEFGHIJK":
            _sheet[f'{col}3'].border = Border(
                left=Side(style='dashed'),
                right=Side(style='dashed'),
                top=Side(style='medium'),
                bottom=Side(style='dashed')
            )

            _sheet[f'{col}4'].border = Border(
                left=Side(style='dashed'),
                right=Side(style='dashed'),
                top=Side(style='dashed'),
                bottom=Side(style='medium')
            )
        
        _sheet['L3'].border = Border(
            left=Side(style='dashed'),
            right=Side(style='medium'),
            top=Side(style='medium'),
            bottom=Side(style='dashed')
        )

        _sheet['L4'].border = Border(
            left=Side(style='dashed'),
            right=Side(style='medium'),
            top=Side(style='dashed'),
            bottom=Side(style='medium')
        )
    
    def set_student_id(self, _val):
        self.active["A4"].value = int(_val)

    def set_fio(self, _val):
        self.active["B4"].value = _val
    
    def set_group(self, _val):
        self.active["F4"].value = int(_val)

    def make_intro(self, *, student_id, fio):
        self.init_A1_L1()
        self.init_A3()
        self.init_B3_E3()
        self.init_F3()
        self.init_G3_I3()
        self.init_J3_L3()

        self.set_student_id(student_id)
        self.set_fio(fio)
        self.set_group(student_id[:4])

        self.set_borders()
