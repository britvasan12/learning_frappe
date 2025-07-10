// Copyright (c) 2025, Brit and contributors
// For license information, please see license.txt


// This code is set the values to the corresponding link fields like linkedin, github and other


// frappe.ui.form.on("Scanner API", {
//     refresh(frm) {
//         frm.add_custom_button('QR Scanner', () => {
//             new frappe.ui.Scanner({
//                 dialog: true,
//                 multiple: false,
//                 on_scan(data) {
//                     const scanned_value = data.decodedText;
//                     console.log('Raw Scanned Values', scanned_value);

//                     link_type = 'other';

//                     if (scanned_value.includes('linkedin.com')) {
//                         frm.set_value('linkedin_link', scanned_value)
//                         link_type = 'linkedin';
//                     } else if (scanned_value.includes('github.com')) {
//                         frm.set_value('github_link', scanned_value)
//                         link_type = 'github';
//                     } else {
//                         frm.set_value('other_link', scanned_value)
//                     }

//                     // let external = scanned_value.startsWith('http');
//                     // console.log(external);
                    
//                     let go_to_link = '';
//                     if(link_type !== 'other' && scanned_value.startsWith('http')){
//                         go_to_link = `<a href="${scanned_value}" ${external ? 'target="_blank"':''} style="color:blue; text-decoration:underline;">Go to link</a>`
//                     }

//                     frappe.msgprint({   
//                         title: 'Navigate to the Link',
//                         indicator: 'green',
//                         message: `Scanned Value: <b>${scanned_value}</b></br> ${go_to_link}`
//                     })
//                 }
//             })
//         })
//     },
// });

// -------------------------------------------------------------------------------------------------

// This code above as same here added to find the duplicate qr's which are already scanned?

// frappe.ui.form.on("Scanner API", {
//     refresh(frm) {
//         // Set to store already scanned links
//         if (!frm.scanned_links) {
//             frm.scanned_links = new Set();
//         }

//         frm.add_custom_button('QR Scanner', () => {
//             new frappe.ui.Scanner({
//                 dialog: true,
//                 multiple: false,
//                 on_scan(data) {
//                     const scanned_value = data.decodedText;
//                     console.log('Raw Scanned Value:', scanned_value);

//                     // Check Pannuthu already scanned ah nu??
//                     if (frm.scanned_links.has(scanned_value)) {
//                         frappe.msgprint({
//                             title: 'Duplicate Scan',
//                             indicator: 'red',
//                             message: 'This QR code was already scanned.'
//                         });
//                         return; 
//                     }

//                     // Already scanned ah illana below operation works!!

//                     frm.scanned_links.add(scanned_value);

//                     let link_type = 'other';

//                     if (scanned_value.includes('linkedin.com')) {
//                         frm.set_value('linkedin_link', scanned_value);
//                         link_type = 'linkedin';
//                     } else if (scanned_value.includes('github.com')) {
//                         frm.set_value('github_link', scanned_value);
//                         link_type = 'github';
//                     } else {
//                         frm.set_value('other_link', scanned_value);
//                     }

//                     let go_to_link = '';
//                     if (link_type !== 'other' && scanned_value.startsWith('http')) {
//                         go_to_link = `<br><a href="${scanned_value}" target="_blank" style="color:blue; text-decoration:underline;">Go to link</a>`;
//                     }

//                     frappe.msgprint({
//                         title: 'Navigate to the Link',
//                         indicator: 'green',
//                         message: `Scanned Value: <b>${scanned_value}</b>${go_to_link}`
//                     });
//                 }
//             });
//         });
//     }
// });

// -------------------------------------------------------------------------------------------

