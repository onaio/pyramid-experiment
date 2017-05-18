from pyramid.view import view_config
from pyramid.response import Response
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response
from webhelpers import paginate
from webhelpers.paginate import Page
from formencode import Schema, validators

from ..models import Customer, Category, Country


class CustomerForm(Schema):

    """ customer form schema for validation """

    filter_extra_fields = True
    allow_extra_fields = True
    company_name = validators.String(not_empty=True)
    category_id = validators.Int()
    contact_title = validators.String()
    contact_first_name = validators.String(not_empty=True)
    contact_last_name = validators.String(not_empty=True)
    address = validators.String()
    city = validators.String()
    region = validators.String()
    postal_code = validators.String()
    country_id = validators.Int()
    mobile = validators.String()
    email = validators.String()
    notes = validators.String()


@view_config(route_name='customer_list')
def list(request):
    search = request.params.get('search', '')

    sort = 'company_name'
    if request.GET.get('sort') and request.GET.get('sort') \
        in ['company_name', 'contact_first_name', 'contact_last_name',
            'category']:
        sort = request.GET.get('sort')
    if sort == 'category':
        sort = 'category.name'

    direction = 'asc'
    if request.GET.get('direction') and request.GET.get('direction') \
        in ['asc', 'desc']:
        direction = request.GET.get('direction')

    # query db

    query = \
        request.dbsession.query(Customer).join(Category).filter(Customer.company_name.like(search
            + '%')).order_by(sort + ' ' + direction)

    # pagination

    page_url = paginate.PageURL_WebOb(request)
    customers = Page(query, page=int(request.params.get('page', 1)),
                     items_per_page=10, url=page_url)
    if 'partial' in request.params:
        return render_to_response('../templates/customer/listPartial.jinja2'
                                  , {'customers': customers},
                                  request=request)
    else:
        return render_to_response('../templates/customer/list.jinja2',
                                  {'customers': customers},
                                  request=request)


@view_config(route_name='customer_new',
             renderer='../templates/customer/new.jinja2')
def new(request):
    """ add new customer """

    categories = get_categories(request)
    countries = get_countries(request)

    form = Form(request, schema=CustomerForm)
    if 'form_submitted' in request.POST and form.validate():
        customer = form.bind(Customer())
        dbsession.add(customer)
        return HTTPFound(location=request.route_url('customer_list'))
    return dict(form=FormRenderer(form), categories=categories,
                countries=countries,
                action_url=request.route_url('customer_new'))


@view_config(route_name='customer_search')
def search(request):
    return Response('OK')


@view_config(route_name='customer_edit')
def edit(request):
    return Response(request.matchdict['id'])


@view_config(route_name='customer_delete')
def delete(request):
    return Response(request.matchdict['id'])


def get_countries(request):
    """ Get all countries with name and id value pairs """

    countries_q = \
        request.dbsession.query(Country).order_by(Country.name)
    countries = [(country.id, country.name) for country in
                 countries_q.all()]

    return countries


def get_categories(request):
    categories_q = \
        request.dbsession.query(Category).order_by(Category.name)
    categories = [(category.id, category.name) for category in
                  categories_q.all()]

    return categories
