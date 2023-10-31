import openpyxl
from .models import SkillHive

def upload_courses_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Перебор строк, начиная со второй строки
        title, description, cover_photo_path = row
        course = SkillHive.objects.create(title=title, description=description)
        course.cover_photo.save(cover_photo_path, open(cover_photo_path, 'rb'), save=True)
