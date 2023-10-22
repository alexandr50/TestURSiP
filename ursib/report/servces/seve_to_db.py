from django.db.models import Sum
from tqdm import tqdm

from report.models import Report
from report.servces.parse_table import get_random_date


def get_report_data(row):
    report_data = Report(
        company=row['company'],
        fact_qliq_data1=row['fact_qliq_data1'],
        fact_qliq_data2=row['fact_qliq_data2'],
        fact_qoil_data1=row['fact_qoil_data1'],
        fact_qoil_data2=row['fact_qoil_data2'],
        forecast_qliq_data1=row['forecast_qliq_data1'],
        forecast_qliq_data2=row['forecast_qliq_data2'],
        forecast_qoil_data1=row['forecast_qoil_data1'],
        forecast_qoil_data2=row['forecast_qoil_data2'],
        date=get_random_date()
    )
    return report_data


def save_report(data):
    for i, row in tqdm(data.iterrows()):
        res = get_report_data(row)
        res.date = get_random_date()
        res.save()


def update_report():
    totals = Report.objects.values('date').annotate(
        total_qliq=
        Sum('fact_qliq_data1') +
        Sum('fact_qliq_data2') +
        Sum('forecast_qliq_data1') +
        Sum('forecast_qliq_data2'),
        total_qoil=
        Sum('fact_qoil_data1') +
        Sum('fact_qoil_data2') +
        Sum('forecast_qoil_data1') +
        Sum('forecast_qoil_data2')
    )

    for total in tqdm(totals):
        Report.objects.filter(
            date=total['date']).update(total_qliq=total['total_qliq'],
                                       total_qoil=total['total_qoil']
                                       )
