from django.db import models


class MsgInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name="UUID")
    send_id = models.CharField(max_length=32, verbose_name="發送人ID")
    send_name = models.CharField(max_length=255, verbose_name="發送人名稱")
    accept_id = models.CharField(max_length=32, verbose_name="接受人ID")
    msg_id = models.CharField(max_length=32, verbose_name="消息ID")
    msg_type = models.CharField(default="1", max_length=32, verbose_name="消息類型")
    msg_value = models.CharField(max_length=255, verbose_name="消息内容")
    timestamp = models.CharField(max_length=255, verbose_name="消息接收時間")
    send_success = models.CharField(default="0", max_length=1, verbose_name="是否以發送给對應的用户")

    class Meta:
        db_table = "chat_msg_info"
