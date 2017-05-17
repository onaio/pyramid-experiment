from pyramid.view import view_config
from pyramid.response import Response

from ..models import Customer

@view_config(route_name='customer_list')
def list(request):
    return Response('OK')

@view_config(route_name='customer_new', renderer='../templates/customer/new.jinja2')
def new(request):
    return Response('OK')

@view_config(route_name='customer_search')
def search(request):
    return Response('OK')

@view_config(route_name='customer_edit')
def edit(request):
    return Response(request.matchdict['id'])

@view_config(route_name='customer_delete')
def delete(request):
    return Response(request.matchdict['id'])