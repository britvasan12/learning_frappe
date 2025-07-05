frappe.listview_settings['Ticket Booking'] = {
    onload: listview => {
        listview.columns.forEach(col => {
            if (col.df) {
                if (col.df.fieldname === 'paid') {
                    col.df.formatter = function(value, df, options, doc){
                        return value ? `<span style="color:green;font-weight:bold;">Yes</span>` :
                            `<span style="color:green;font-weight:bold;">No</span>`
                    };
                }
            }
        });

        listview.columns.forEach(col =>{
            if(col.df){
                if (col.df.fieldname === 'customer_name'){
                    col.df.formatter = function(value, df, options, doc){
                        return `<span style="color:red;font-weight:bold;">${value}</span>`
                    }
                }
            }
        });

        listview.columns.forEach(col =>{
            if(col.df){
                if(col.df.fieldname === 'movie_name'){
                    col.df.formatter = function(value, df, options, doc){
                        return `<span style="color:orange;font-weight:bold;">${value}</span>`
                    }
                }
            }
        })
    }
}