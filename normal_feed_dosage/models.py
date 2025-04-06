from django.db import models


# 普通飼料管理
class NormalFeedDosageInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    chicken_seed_fine_feed_dosage = models.CharField(max_length=32, verbose_name="每月雞苗精料用量")
    chicken_develop_fine_feed_dosage = models.CharField(max_length=32, verbose_name="每月中雞精料用量")
    chicken_mature_fine_feed_dosage = models.CharField(max_length=32, verbose_name="每月大雞精料用量")
    chicken_laying_hens_fine_feed_dosage = models.CharField(max_length=32, verbose_name="每月下單母雞精料用量")
    chicken_later_borrowing_fine_feed_dosage = models.CharField(max_length=32, verbose_name="每月後借母雞精料用量")
    chicken_cock_fine_feed_dosage = models.CharField(max_length=32, verbose_name="每月公雞精料用量")
    data_time = models.CharField(max_length=10, verbose_name="數據時間")
    data_version = models.IntegerField(verbose_name="數據版本")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        unique_together = (("id", "data_time", "data_version"),)
        db_table = "normal_feed_dosage_info"
