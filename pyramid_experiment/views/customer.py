from pyramid.view import view_config
from pyramid.response import Response
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from pyramid.httpexceptions import HTTPFound
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
    return Response('OK')

@view_config(route_name='customer_new', renderer='../templates/customer/new.jinja2')
def new(request):
	""" add new customer """

	form = Form(request, schema=CustomerForm)
	if "form_submitted" in request.POST and form.validate():
		customer = form.bind(Customer())
		dbsession.add(customer)
		return HTTPFound(location = request.route_url("customer_list"))
	return dict(form=FormRenderer(form),
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

def get_countries(self):
	""" Get all countries with name and id value pairs """
	country_q = dbsession.query(Country).order_by(Country.name)
	countries = [(country.id, country.name) for country in countries_q.all()]

	return countries

def get_categories():
	categories_q = dbsession.query(Category).order_by(Category.name)
	categories = [(category.id, category.name) for category in categories_q.all()]

	return categories