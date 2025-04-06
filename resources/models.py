from django.db import models


class ResourcesInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    name = models.CharField(verbose_name="資源名稱", max_length=255, null=True, blank=True)
    path = models.TextField(verbose_name="資源存放路徑")
    resources_type = models.CharField(max_length=2, verbose_name="資源類型[0:消息附件],1:表格附件")
    file_type = models.CharField(max_length=50, verbose_name="文件類型", null=True, blank=True)
    person = models.CharField(max_length=32, verbose_name="所屬管理員ID")
    remarks = models.TextField(verbose_name="備注", null=True, blank=True)
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")

    class Meta:
        db_table = "resources_info"
