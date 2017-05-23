import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import Country, Category, Customer, User


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        customer = Customer(
            company_name=u'Tech Services LTD',
            category_id=200)
        dbsession.add(customer)

        country = Country(
            code=u'+254',
            name=u'Kenya')
        dbsession.add(country)

        category = Category(name=u'Reseller')
        dbsession.add(category)


        editor = User(name='editor', role='editor')
        editor.set_password('editor')
        dbsession.add(editor)

        basic = User(name='basic', role='basic')
        basic.set_password('basic')
        dbsession.add(basic)