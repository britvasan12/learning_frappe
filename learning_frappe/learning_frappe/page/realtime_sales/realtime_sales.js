// frappe.pages['realtime-sales'].on_page_load = function (wrapper) {
// 	let page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Realtime Sales Monitor',
// 		single_column: true
// 	});

// 	wrapper.innerHTML += `<div id="sales-chart" style="margin-top: 20px; height: 300px;"></div>`;

// 	let chart_data = {
// 		labels: [],
// 		datasets: [
// 			{
// 				name: 'Sales ($)',
// 				values: []
// 			}
// 		]
// 	};

// 	let sales_chart = new frappe.ui.RealtimeChart('#sales-chart', 'sales_realtime_event', 10, {
// 		title: 'Live Sales Data',
// 		data: chart_data,
// 		type: 'line',
// 		height: 250,
// 		colors: ['#ff5858']
// 	});

// 	sales_chart.start_updating();

// 	frappe.realtime.on("sales_realtime_event", (data) => {
//     console.log("Received:", data);

//     const label = data.label;
//     const points = data.points;

//     if (sales_chart.data.labels.length >= 10) {
//         sales_chart.data.labels.shift();
//         sales_chart.data.datasets[0].values.shift(); 
//     }

//     sales_chart.data.labels.push(label);
//     sales_chart.data.datasets[0].values.push(points);

//     sales_chart.refresh();  
// });
// };
