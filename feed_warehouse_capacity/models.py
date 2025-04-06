from django.db import models


class FeedWarehouseCapacityInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    mixed_feed_frequency = models.CharField(max_length=32, verbose_name="每月混合飼料次數")
    mixed_feed_containers_frequency = models.CharField(max_length=32, verbose_name="飼料混合器數量")
    chicken_seed_mixed_feed_containers_frequency = models.CharField(max_length=100, verbose_name="雞苗飼料混合器數量")
    chicken_develop_mixed_feed_containers_frequency = models.CharField(max_length=100,
                                                                       verbose_name="中雞至大雞飼料混合器容量")
    chicken_mature_mixed_feed_containers_frequency = models.CharField(max_length=100, verbose_name="大雞飼料混合器容量")
    feed_tower_capacity = models.CharField(max_length=100, verbose_name="料塔容量")
    feed_tower_number = models.CharField(max_length=100, verbose_name="料塔數量")
    mixed_feed_clear_number = models.CharField(max_length=100, verbose_name="每月飼料混合器清理數量")
    feed_tower_clear_number = models.CharField(max_length=100, verbose_name="每月料塔清理數量")
    data_time = models.CharField(max_length=10, verbose_name="數據時間")
    data_version = models.IntegerField(verbose_name="數據版本")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        unique_together = (("id", "data_time", "data_version"),)
        db_table = "feed_warehouse_capacity_info"
