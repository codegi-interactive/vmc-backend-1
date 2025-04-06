"""
URL configuration for vmc_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 資源
    path("resources/", include("resources.urls")),
    # 聊天
    path("chat/", include("chat.urls")),
    # 商品
    path("commodity/", include("commodity.urls")),
    # 訂單
    path("order/", include("order.urls")),
    # 購物車
    path("cart/", include("shopp_cart.urls")),
    # 用户
    path("user/", include("user.urls")),
    # 農場首頁
    path("farm/", include("farm_home.urls")),
    # 農場其他信息
    path("farmOtherAttributes/", include("farm_other_attributes.urls")),
    # 最新消息
    path("notice/", include("notice.urls")),
    # 清理程序
    path("clear/", include("clear.urls")),
    # 免疫程序
    path("immunization/", include("immunization.urls")),
    # 飼料管用量
    path("normal/", include("normal_feed_dosage.urls")),
    # 精料用量
    path("fine/", include("fine_feed_dosage.urls")),
    # 飼料容器
    path("feed/", include("feed_warehouse_capacity.urls")),
    # 雞群
    path("chicken/", include("chicken_flock.urls")),
    # 死淘率
    path("obituary/", include("obituary.urls")),
    # 用藥記錄
    path("medication/", include("medication_use.urls")),
    # 問卷得分
    path("score/", include("questionnaire_score.urls")),
    # 字典
    path("dict/", include("dict_info.urls")),
]
