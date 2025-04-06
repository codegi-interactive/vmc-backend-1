from django.db import models


# 雞群批次管理
class ChickenFlockInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    batch_name = models.CharField(max_length=255, verbose_name="批次名稱")
    incubation_date = models.CharField(max_length=255, null=True, blank=True, verbose_name="孵化日期")
    chicken_seedling_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="雞苗數量")
    vaccine_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="疫苗ID")
    vaccine_manufacturers = models.CharField(max_length=255, null=True, blank=True, verbose_name="疫苗供應商")
    d1 = models.CharField(max_length=255, null=True, blank=True, verbose_name="d1")
    d2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="d2")
    d3 = models.CharField(max_length=255, null=True, blank=True, verbose_name="d3")
    data_version = models.IntegerField(verbose_name="數據版本")
    status = models.CharField(max_length=2, verbose_name="狀態[0:已關閉,1:活動中]")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        unique_together = (("id", "data_version"),)
        db_table = "chicken_flock_info"



class ChickenFlockToInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    farmName = models.CharField(max_length=32, verbose_name="農場名稱")
    batch_name = models.CharField(max_length=255, verbose_name="批次名稱")
    incubation_date = models.CharField(max_length=255, null=True, blank=True, verbose_name="孵化日期")
    chicken_seedling_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="雞苗數量")
    vaccine_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="疫苗ID")
    vaccine_manufacturers = models.CharField(max_length=255, null=True, blank=True, verbose_name="疫苗供應商")
    d1 = models.CharField(max_length=255, null=True, blank=True, verbose_name="d1")
    d2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="d2")
    d3 = models.CharField(max_length=255, null=True, blank=True, verbose_name="d3")
    data_version = models.IntegerField(verbose_name="數據版本")
    status = models.CharField(max_length=2, verbose_name="狀態[0:已關閉,1:活動中]")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")