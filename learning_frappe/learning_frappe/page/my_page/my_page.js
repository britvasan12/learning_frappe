frappe.pages['my-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'My Page',
		single_column: true
	});

	page.set_indicator('Sparkie', 'green')

	let $btn = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus')
	let $btn1 = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')

};

