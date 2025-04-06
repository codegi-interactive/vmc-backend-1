from django.db import models


# 問卷得分
class QuestionnaireScoreInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="數據ID")
    farm_id = models.CharField(max_length=32, verbose_name="農場ID,問卷歸屬人ID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID,答題人ID")
    total_score = models.IntegerField(verbose_name="總得分")
    data_version = models.IntegerField(verbose_name="數據版本")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")
    class Meta:
        db_table = "questionnaire_score_info"


class QuestionnaireScoreQueryInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="數據ID")
    farm_id = models.CharField(max_length=32, verbose_name="農場ID,問卷歸屬人ID")
    user_id = models.CharField(max_length=32, verbose_name="用户ID,答題人ID")
    username = models.CharField(max_length=32,
                                verbose_name="用户名稱,答題人賬號,數據庫没有對應鍵,sql進行查詢")
    total_score = models.IntegerField(verbose_name="總得分")
    data_version = models.IntegerField(verbose_name="數據版本")
    create_time = models.CharField(max_length=50, verbose_name="新增時間")
    create_by = models.CharField(max_length=32, verbose_name="新增人")
    update_time = models.CharField(max_length=50, verbose_name="更新時間")
    update_by = models.CharField(max_length=32, verbose_name="更新人")
    deleted = models.BooleanField(max_length=32, default=0, verbose_name="數據是否已删除[0:未删除,1:已删除]")
