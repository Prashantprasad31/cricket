from django.urls import path
from match import views

urlpatterns = [
    path('view/',views.view_match),
    path('add/',views.add_match),
    path('delete/<int:matchid>',views.delete_match),
    path('update/<int:matchid>',views.update_product),
]