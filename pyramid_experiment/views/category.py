from pyramid.view import view_config
from pyramid.response import Response

from ..models import Category

@view_config(route_name='category_list')
def list(request):
    return Response('OK')

@view_config(route_name='category_new')
def new(request):
    return Response('OK')

@view_config(route_name='category_search')
def search(request):
    return Response('OK')

@view_config(route_name='category_edit')
def edit(request):
    return Response(request.matchdict['id'])

@view_config(route_name='category_delete')
def delete(request):
    return Response(request.matchdict['id'])