from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'per_page'

    def paginated_response(self, data):
        return {
            "success": True,
            "message": "OK",
            "total_count": self.page.paginator.count,
            "page": self.page.number,
            "page_count": self.page.paginator.num_pages,
            "per_page": self.page.paginator.per_page,
            "results": data
        }

    def paginated_queryset(self, qs, request):
        return super(CustomPagination, self).paginate_queryset(qs, request)