from pyramid.httpexceptions import (HTTPFound, HTTPForbidden)
from pyramid.view import view_config

from ..models import User

@view_config(route_name='home')
def home(request):
    """home """
    return HTTPFound(location = request.route_url('home_dashboard'))

@view_config(route_name='home_dashboard', renderer='../templates/dashboard.jinja2')
def dashboard(request):
    """dashboard """

    user = request.user
    if user is None or user.role not in ('editor', 'basic'):
    	raise HTTPForbidden

    return {"dashboard": "Dashboard"}