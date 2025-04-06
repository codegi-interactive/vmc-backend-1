from django.db import models


class OrderInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    number = models.IntegerField(verbose_name="商品數量", null=True, blank=True)
    total_price = models.IntegerField(verbose_name="訂單總價,單位分")
    order_status = models.CharField(max_length=2,
                                    verbose_name="訂單狀態[0:未下單,1:已下單,2:已付款,3:已發貨,4:已收貨,20:訂單正常完成,21:訂單超時完成,22:訂單已取消]")
    order_time = models.CharField(max_length=50, verbose_name="下單時間")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        db_table = "order_info"


class OrderDetails(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    order_id = models.CharField(max_length=32, verbose_name="訂單ID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID")
    commodity_id = models.CharField(max_length=32, verbose_name="商品ID")
    name = models.TextField(verbose_name="商品名稱")
    price = models.IntegerField(verbose_name="商品單價,單位分")
    type = models.CharField(max_length=1, verbose_name="商品類型", null=True, blank=True)
    number = models.IntegerField(verbose_name="商品數量", null=True, blank=True)
    weight = models.IntegerField(verbose_name="商品重量", null=True, blank=True)
    resources_id = models.CharField(max_length=32, verbose_name="資源ID", null=True, blank=True)
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        db_table = "order_details"
