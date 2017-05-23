from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
)
from pyramid.security import (
    Allow,
    Everyone,
)

from .models import Customer

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # login routes
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    # home
    config.add_route('home', '/')
    config.add_route('home2', '/')
    config.add_route('home_dashboard', '/home/dashboard')

    # customer routes
    config.add_route('customer_list', 'customers/list')
    config.add_route('customer_search', 'customers/search')
    config.add_route('customer_new', 'customers/new')
    config.add_route('customer_edit', 'customers/{id}/edit', factory=edit_customer_factory)
    config.add_route('customer_delete', 'customers/{id}/delete')

    #country routes
    config.add_route('country_list', 'countries/list')
    config.add_route('country_search', 'countries/search')
    config.add_route('country_new', 'countries/new')
    config.add_route('country_edit', 'country/{id}/edit')
    config.add_route('country_delete', 'country/{id}/delete')

    #category routes
    config.add_route('category_list', 'categories/list')
    config.add_route('category_search', 'category/search')
    config.add_route('category_new', 'categories/new')
    config.add_route('category_edit', 'category/{id}/edit')
    config.add_route('category_delete', 'category/{id}/delete')

def edit_customer_factory(request):
    customer_id = request.matchdict['id']

    page = request.dbsession.query(Customer).filter_by(id=customer_id).first()
    if page is None:
        next_url = request.route_url('customer_edit', customer_id=customer_id)
        raise HTTPNotFound
    return EditCustomer(page)

class EditCustomer(object):
    def __init__(self, page):
        self.page = page

    def __acl__(self):
        return [
            (Allow, 'role:editor', 'edit'),
            (Allow, 'role:basic', 'view'),
        ]
