from django.db import models


# 用藥記錄
class MedicationUseInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    chicken_flock_id = models.CharField(max_length=32, verbose_name="雞群ID")
    chicken_name = models.CharField(max_length=32, verbose_name="雞群ID")
    medication_name = models.CharField(max_length=32, verbose_name="藥物名稱")
    medication_dose = models.CharField(max_length=32, verbose_name="藥物劑量")
    medication_measure = models.CharField(max_length=32, verbose_name="藥物用量")
    usage_duration = models.CharField(max_length=32, verbose_name="使用天數")
    data_time = models.CharField(max_length=10, verbose_name="數據時間")
    data_version = models.IntegerField(verbose_name="數據版本")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        unique_together = (("id", "data_time", "data_version"),)
        db_table = "medication_use_info"
