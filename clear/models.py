from django.db import models


class ClearProcedureInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    period_validity = models.CharField(max_length=32, verbose_name="有效期")
    detergent = models.CharField(max_length=100, verbose_name="清潔劑")
    dentifrices = models.CharField(max_length=100, verbose_name="滅鼠劑")
    pesticide = models.CharField(max_length=100, verbose_name="殺蟲劑")
    parasites_internal = models.CharField(max_length=100, verbose_name="内寄生蟲殺蟲劑")
    parasites_external = models.CharField(max_length=100, verbose_name="外寄生蟲殺蟲劑")
    data_time = models.CharField(max_length=10, verbose_name="數據時間")
    data_version = models.IntegerField(verbose_name="數據版本")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        unique_together = (("id", "data_time", "data_version"),)
        db_table = "clear_procedure_info"
