import pandas as pd
from django.core.exceptions import ValidationError
from django.shortcuts import render
from pandas import DataFrame

from report.models import Report
from report.servces.parse_table import parse_table
from report.servces.seve_to_db import save_report, update_report


def create_report(request):
    context = {}
    if request.method == 'POST':
        name_file = request.FILES.get('name_file')
        file_extension = str(name_file).split('.')[-1]
        try:
            file_extension in ['.xls', '.xlsx']
        except (ValueError, ValidationError) as err:
            return render(request, 'report/create_report.html', {'errors': 'Формат файла должен быть .xls, .xlsx'})
        try:
            data_df: DataFrame = parse_table(name_file)
            save_report(data_df)
            update_report()
        except (ValueError, ValidationError) as err:
            return render(request, 'report/create_report.html', {'errors': err})
        df_to_html = data_df.to_html()
        context = {'df_to_html': df_to_html, 'title': 'Create Report'}

    return render(request, 'report/create_report.html', context)


def get_all_reports(request):
    reports = Report.objects.all()
    if reports:
        try:
            db_df = pd.DataFrame.from_records(reports.values())
            db_df = db_df.drop('id', axis=1)
            df_to_html = db_df.to_html()
            context = {'title': 'Список отчетов', 'reports': df_to_html}
            return render(request, 'report/list_reports.html', context)
        except Exception as err:
            return render(request, 'report/list_reports.html', {'error_message': err})
    context = {'title': 'Список отчетов'}
    return render(request, 'report/list_reports.html', context)
