from django.db import models


class Report(models.Model):
    company = models.CharField(max_length=30)
    fact_qlid_data1 = models.IntegerField()
    fact_qlid_data2 = models.IntegerField()
    fact_qoil_data1 = models.IntegerField()
    fact_qoil_data2 = models.IntegerField()
    forecast_qlid_data1 = models.IntegerField()
    forecast_qlid_data2 = models.IntegerField()
    forecast_qoil_data1 = models.IntegerField()
    forecast_qoil_data2 = models.IntegerField()
    total_qlid = models.IntegerField(null=True)
    total_qoil = models.IntegerField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'
