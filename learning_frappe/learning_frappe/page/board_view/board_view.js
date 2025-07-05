frappe.pages['board-view'].on_page_load = function (wrapper) {
	let boardName = frappe.get_route()[1];

	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: __("Kanban Board"),
		single_column: true
	});

	let kanbanRoot = $('<div id="kanban-root" class="p-6"></div>').appendTo(page.body);

	// Listen for task updates
	frappe.realtime.on('task_update', ({ task, status, assignee, by, board: b }) => {
		if (b !== boardName) return;
		updateTaskCard(task, status, assignee);
		frappe.show_alert(`${by} moved ${task} → ${status}`);
	});

	loadBoard(boardName);
};

function loadBoard(name) {
	if (!name) {
		frappe.msgprint("Board name not provided");
		return;
	}

	frappe.call({
		method: "learning_frappe.api.tasks.get_tasks",
		args: { board: name },
		callback: (res) => {
			if (res.message) {
				renderKanban(res.message);
			} else {
				frappe.msgprint("No tasks found for this board.");
			}
		}
	});
}

function renderKanban(tasks) {
	const stages = ["Backlog", "Todo", "In Progress", "Review", "Done"];
	const root = $("#kanban-root").empty();
	const row = $('<div class="flex space-x-4 overflow-x-auto pb-4"></div>');

	stages.forEach(stage => {
		const key = stage.toLowerCase().replace(/\s+/g, '-');

		const column = $(`
			<div class="kanban-col bg-gray-100 rounded-lg shadow-md p-4" id="col-${key}">
				<h3 class="text-md font-semibold text-gray-700 mb-3 border-b pb-1">${stage}</h3>
				<div class="task-list space-y-2"></div>
			</div>
		`);

		row.append(column);
	});

	root.append(row);

	tasks.forEach(task => {
		const key = task.status.toLowerCase().replace(/\s+/g, '-');
		const card = getTaskCardHTML(task);
		$(`#col-${key} .task-list`).append(card);
	});
}

function getTaskCardHTML(task) {
	return `
		<div class="task-card bg-white p-4 rounded-lg shadow hover:shadow-md transition" id="task-${task.name}">
			<div class="font-medium text-gray-900 mb-1">📝 ${task.subject}</div>
			<div class="text-xs text-gray-500">📅 Due: ${task.due_date || "N/A"}</div>
			<div class="text-xs text-gray-500">⚡ Priority: <span class="font-semibold">${task.priority}</span></div>
			<div class="assignee text-xs text-blue-600">👤 Assigned: ${task.assignee || "Unassigned"}</div>
		</div>
	`;
}

function updateTaskCard(taskId, newStatus, newAssignee) {
	const card = $(`#task-${taskId}`);
	if (!card.length) return;

	const key = newStatus.toLowerCase().replace(/\s+/g, '-');
	$(`#col-${key} .task-list`).append(card);

	card.find('.assignee').text(`👤 Assigned: ${newAssignee || "Unassigned"}`);
} 