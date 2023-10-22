from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR


class ReportHandler:
    """Класс с необходимыми атрибутами (парсинг, сохранения и обновления)"""

    def __init__(self, parse_table, save_report, update_report):
        self.load_data = parse_table
        self.save_report = save_report
        self.update_report = update_report

    def create_report(self, path):
        """Метод создания записи в бд"""

        file_path = os.path.join(BASE_DIR, path)
        data = self.load_data(file_path)
        self.save_report(data)
        self.update_report()
