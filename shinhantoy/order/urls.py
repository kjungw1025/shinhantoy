from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderListView.as_view()),
    path("/<int:ord_no>", views.OrderDetailView.as_view()),
    path("/<int:ord_no>/comment", views.CommentListView.as_view()),
    path("/comment", views.CommentCreateView.as_view()),
]