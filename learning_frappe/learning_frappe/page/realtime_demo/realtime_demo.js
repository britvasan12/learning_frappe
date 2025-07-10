// frappe.pages['realtime-demo'].on_page_load = function (wrapper) {
// 	let page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Realtime Chart Demo',
// 		single_column: true
// 	});

// 	wrapper.innerHTML += `<div id="mychart" style="margin-top: 20px; height: 300px;"></div>`;

// 	let data = {
// 		labels: [],
// 		datasets: [{
// 			name: 'Leave Count',
// 			values: []
// 		}]
// 	};

// 	let chart = new frappe.Chart('#mychart', {
// 		title: 'Leave Count Realtime',
// 		data: data,
// 		type: 'line',
// 		height: 300,
// 		colors: ["#36a2eb"]
// 	});

// 	frappe.realtime.on('leave_count_realtime', (data_point) => {
// 		const label = data_point.label;
// 		const value = data_point.points;

// 		if (typeof value !== 'number') {
// 			console.warn("Invalid value received:", value);
// 			return;
// 		}

// 		chart.data.labels.push(label);
// 		chart.data.datasets[0].values.push(value);

// 		if (chart.data.labels.length > 10) {
// 			chart.data.labels.shift();
// 			chart.data.datasets[0].values.shift();  
// 		}

// 		chart.update();
// 	});
// };



// frappe.pages['realtime-demo'].on_page_load = function(wrapper){
// 	let page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Realtime Chart Demo',
// 		single_column: true
// 	});

// 	wrapper.innerHTML += `<div id="chart" style="margin-top: 20px; height: 300px;"></div>`;
// 	let data = {
// 		labels: [],
// 		datasets: [
// 			{
// 				name: 'Leave Count',
// 				values: []
// 			}
// 		]
// 	};
// 	// if (typeof value !== 'number') {
// 	// 		console.warn("Invalid value received:", value);
// 	// 		return;
// 	// 	}
// 	let my_chart = new frappe.ui.RealtimeChart('#chart','leave_count_realtime', 8,{
// 		title: 'Leave Data Chart',
// 		data: data,
// 		type: 'line',
// 		height: 250,
// 		colors: ['#7cd6fd']
// 	})
	

// 	my_chart.start_updating();

// 	frappe.realtime.on("leave_count_realtime", (data) => {
// 		console.log(data);

// 		my_chart.add_data_point(data.label, data.points);
// });

// }




// frappe.pages['realtime-demo'].on_page_load = function (wrapper) {
// 	let page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Realtime Chart Demo',
// 		single_column: true
// 	});

// 	wrapper.innerHTML += `<div id="mychart" style="margin-top: 20px; height: 300px;"></div>`;

// 	let data = {
// 		labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
// 		datasets: [{
// 			name: 'Leave Count',
// 			values: []  
// 		}]
// 	};

// 	let chart = new frappe.Chart('#mychart', {
// 		title: 'Leave Count Realtime (Mon-Sat)',
// 		data: data,
// 		type: 'bar',
// 		height: 300,
// 		colors: ["#36a2eb"]
// 	});

// 	frappe.realtime.on('leave_count_realtime', (data_point) => {
// 		const label = data_point.label;
// 		const value = data_point.points;

// 		const index = chart.data.labels.indexOf(label);
// 		if (index !== -1) {
// 			chart.data.datasets[0].values[index] = value;
			
// 		}

// 		chart.update();
// 	});
// };


frappe.pages['realtime-demo'].on_page_load = function(wrapper){
	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Realtime Chart Demo',
		single_column: true
	});
	
	wrapper.innerHTML += `<div id="chart" style="margin-top: 20px; height: 300px;"></div>`;

	let data = {
		labels: [],  
		datasets: [
			{
				name: 'Leave Count',
				values: []
			}
		]
	};

	let my_chart = new frappe.ui.RealtimeChart('#chart', 'leave_count_realtime', 10, {
		title: 'Leave Data Chart',
		data: data,
		type: 'line',
		height: 250,
		colors: ['#7cd6fd']
	});

	my_chart.start_updating();
}
