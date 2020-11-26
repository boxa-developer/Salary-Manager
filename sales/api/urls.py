from django.urls import path
from .views import *

urlpatterns = [
    path('user/add', AddAccount.as_view(), name='add_user'),
    path('user/update', UpdateAccount.as_view(), name='update_user'),
    path('user/delete', DeleteAccount.as_view(), name='delete_user'),

    path('position/add', AddPosition.as_view(), name='add_position'),
    path('position/update', UpdatePosition.as_view(), name='update_position'),
    path('position/delete', DeletePosition.as_view(), name='delete_position'),

    path('extra/add', AddExtra.as_view(), name='add_extra'),
    path('extra/update', UpdateExtra.as_view(), name='update_extra'),
    path('extra/delete', DeleteExtra.as_view(), name='delete_extra'),

    path('payment/add', AddTransaction.as_view(), name='add_payment'),
    path('payment/update', UpdateTransaction.as_view(), name='update_payment'),
    path('payment/delete', DeleteTransaction.as_view(), name='delete_payment'),
]
