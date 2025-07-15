// frappe.listview_settings['Utility Function'] = {
//     onload: function(listview){
//         listview.page.add_inner_button('Utility',()=>{
//             frappe.call({
//                 method: 'learning_frappe.learning_frappe.doctype.utility_function.utility_function.my_method',
//                 callback:(r)=>{
//                     if(r.message){
//                         frappe.msgprint(`Current Time: ${r.message}`)
//                     }
//                 }
//             })
//         })
//     }
// }

// frappe.listview_settings['Utility Function'] = {
//     onload: function(listview){
//         listview.page.add_inner_button('Utility', () => {
//             // Open the URL directly in a new tab
//             window.open('/api/method/learning_frappe.learning_frappe.doctype.utility_function.utility_function.simple_pdf');
//         });
//     }
// }
