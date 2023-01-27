from rest_framework import pagination

class OrderLargePagination(pagination.PageNumberPagination):
    # pass라고 두면 pagination 기본값으로 설정됨
    page_size = 10

class CommentPagination(pagination.PageNumberPagination):
    # pass라고 두면 pagination 기본값으로 설정됨
    page_size = 5