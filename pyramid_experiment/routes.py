def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    # home
    config.add_route('home', '/')
    config.add_route('home_dashboard', '/home/dashboard')

    # customer routes
    config.add_route('customer_list', 'customers/list')
    config.add_route('customer_new', 'customers/new')
    config.add_route('customer_search', 'customers/search')

    #country routes
    config.add_route('country_list', 'countries/list')
    config.add_route('country_new', 'countries/new')

    #category routes
    config.add_route('category_list', 'categories/list')
    config.add_route('category_new', 'categories/new')

