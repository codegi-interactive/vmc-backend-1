from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    res = exception_handler(exc, context)
    if res:
        # 說明是drf的異常，它處理了
        if isinstance(res.data, dict):
            detail = res.data.pop('detail1', 'error')
        else:
            detail = res.data[0]
        return Response({'code': -1, 'msg': detail}, status=res.status_code)
    # 說明是其它異常，它没有處理
    return Response({
        'code': 0,
        'msg': str(exc)
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
