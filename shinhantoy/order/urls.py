from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderListView.as_view()),
    path("/<int:ord_id>", views.OrderDetailView.as_view()),
    path("/<int:pk>/comment", views.CommentView.as_view()),
    #path("/comment", views.CommentCreateView.as_view()),
]