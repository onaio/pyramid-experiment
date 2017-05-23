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
    config.add_route('customer_edit', 'customers/{id}/edit')
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
