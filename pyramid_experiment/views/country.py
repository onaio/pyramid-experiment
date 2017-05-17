from pyramid.view import view_config
from pyramid.response import Response

from ..models import Country

@view_config(route_name='country_list')
def list(request):
    return Response('OK')

@view_config(route_name='country_new')
def new(request):
    return Response('OK')

@view_config(route_name='country_search')
def search(request):
    return Response('OK')

@view_config(route_name='country_edit')
def edit(request):
    return Response(request.matchdict['id'])

@view_config(route_name='country_delete')
def delete(request):
    return Response(request.matchdict['id'])
