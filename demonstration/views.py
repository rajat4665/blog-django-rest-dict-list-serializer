from rest_framework import viewsets
from django.db.models import Prefetch
from django.db import connection

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # this function display number of sql queries on this class
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        total_queries = connection.queries
        print('# of Queries: {}'.format(len(total_queries)))
        for query in total_queries:
            print()
            print('*'*20)
            print(query)

        return response
