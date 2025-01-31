from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'prev': self.page.has_previous(),
            'next': self.page.has_next(),
            'data': data
        })
