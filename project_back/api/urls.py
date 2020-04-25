from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views import category_list, products_list, UserAPIView, product_detail, categoryproducts, OrdersListAPIView

urlpatterns = [
     path('login/', obtain_jwt_token),


     path('categories/', category_list),
     path('categories/<int:category_id>/products', categoryproducts),



     path('products/', products_list),
     path('products/<int:product_id>/', product_detail),


     path('users/', UserAPIView.as_view()),

     path('orders/', OrdersListAPIView.as_view()),
     path('orders/', OrdersListAPIView.as_view()),

     # path('login/', LoginView.as_view()),
     # path('logout/', LogoutView.as_view()),
]
