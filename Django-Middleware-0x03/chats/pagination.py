from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,  # total number of items
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
