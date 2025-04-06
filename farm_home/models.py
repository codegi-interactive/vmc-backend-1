from django.db import models


class FarmHomeInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True,
                          verbose_name="UUID,一條數據有多個版本，和data_version共同组成一份唯一數據")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    breeding_quota = models.CharField(max_length=32, verbose_name="養殖額度")
    chicken_seedlings_type = models.TextField(max_length=10000, verbose_name="雞苗種類")
    breeding_methods = models.CharField(max_length=100, verbose_name="養殖方式")
    chicken_seedlings_number1 = models.CharField(max_length=100, verbose_name="雞苗數量1")
    chicken_seedlings_number2 = models.CharField(max_length=100, verbose_name="雞苗數量2")
    chicken_seedlings_number3 = models.CharField(max_length=100, verbose_name="雞苗數量3")
    chicken_seedlings_volume1 = models.CharField(max_length=100, verbose_name="雞苗體積1")
    chicken_seedlings_volume2 = models.CharField(max_length=100, verbose_name="雞苗體積2")
    chicken_seedlings_volume3 = models.CharField(max_length=100, verbose_name="雞苗體積3")
    data_version = models.CharField(max_length=3, verbose_name="數據版本")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        unique_together = (("id", "data_version"),)
        db_table = "farm_home_info"
