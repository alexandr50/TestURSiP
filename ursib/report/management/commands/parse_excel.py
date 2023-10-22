from django.core.management.base import BaseCommand, CommandError

from report.servces.parse_table import parse_table
from report.servces.report_handler import ReportHandler
from report.servces.seve_to_db import save_report, update_report


class Command(BaseCommand):

    def add_arguments(self, parser):
        """Метод добавления пути к файлу"""

        parser.add_argument("--path",
                            type=str,
                            default=r'report/data_files//Приложение_к_заданию_бек_разработчика.xlsx',
                            )

    def handle(self, *args, **options):
        file_path = options.get('path')
        report = ReportHandler(
            parse_table,
            save_report,
            update_report
        )
        report.create_report(file_path)

