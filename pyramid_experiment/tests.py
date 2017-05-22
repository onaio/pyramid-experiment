import unittest
import transaction

from pyramid import testing

def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('.models')
        settings = self.config.get_settings()

        from .models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from .models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from .models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)

    def setup_test_data(self):
        # add new customers
        from .models.customer import Customer
        customer1 = Customer(id=5,
                             company_name= u'Hirazi',
                             category_id=23,
                             address=67652,
                             city=u'Dodoma',
                             country=u'Tanzania')
        customer2 = Customer(id=6,
                             company_name= u'Isuzu',
                             category_id=44,
                             address=63739,
                             city=u'Nairobi',
                             country=u'Kenya')



class TestMyViewSuccessCondition(BaseTest):

    def setUp(self):
        super(TestMyViewSuccessCondition, self).setUp()
        self.init_database()

        from .models import MyModel
        model = MyModel(name='one', value=55)
        self.session.add(model)

    def test_passing_view(self):
        from .views.default import my_view
        info = my_view(dummy_request(self.session))
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'pyramid-experiment')


class TestMyViewFailureCondition(BaseTest):

    def test_failing_view(self):
        from .views.default import my_view
        info = my_view(dummy_request(self.session))
        self.assertEqual(info.status_int, 500)

class TestDashboardView(BaseTest):

    def test_success_view(self):
        from .views.home import dashboard
        info = dashboard(dummy_request(self.session))
        self.assertEqual(info, {'dashboard': 'Dashboard'})

class CustomerViewTest(BaseTest):

    def setUp(self):
        super(CustomerViewTest, self).setUp()
        self.init_database()
        from .models import Customer
        customer = Customer(company_name=u'Itech', category_id=109)
        self.session.add(customer)
        self.config.add_route('customer_new', 'customers/new')

    def test_new_customer_view(self):

        from .views.customer import new
        info = new(dummy_request(self.session))
        self.assertEqual(info['action_url'], 'http://example.com/customers/new')
