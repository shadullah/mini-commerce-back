from django.urls import path,include

from .views import  CartListView, CartByUserView, CartItemUpdateDelete

urlpatterns = [
    path("user/", CartListView.as_view(), name="user-cart-list"),
    path("user/<int:user_id>/", CartByUserView.as_view(), name="user-cart"),
    path("user/<int:user_id>/cartItems/<int:cartItem_id>/", CartItemUpdateDelete.as_view(), name="user-cart-update-delete"),
]
