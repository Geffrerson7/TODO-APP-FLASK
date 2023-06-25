const taskId = document.querySelector("#taskId").value;
const taskSection = document.querySelector("#task_section");
const editButton = taskSection.querySelector("a.btn");

function edit() {
  const spanUser = document.querySelector("#taskUser");
  const taskUser = spanUser.innerText;

  const spanStartingPoint = document.querySelector("#taskStartingPoint");
  const taskStartingPoint = spanStartingPoint.innerText;

  const spanEndPoint = document.querySelector("#taskEndPoint");
  const taskEndPoint = spanEndPoint.innerText;

  const inputUser = `User: <input type="text" id="inputUser" class="form-control d-inline" placeholder="${taskUser}" value="${taskUser}">`;
  const inputStartingPoint = `Starting Point: <input type="text" id="inputStartingPoint" class="form-control d-inline" placeholder="${taskStartingPoint}" value="${taskStartingPoint}">`;
  const inputEndPoint = `End point: <input type="text" id="inputEndPoint" class="form-control d-inline" placeholder="${taskEndPoint}" value="${taskEndPoint}">`;
  
  const btnSave = `<a href="javascript: save();" class="btn btn-primary">guardar</a>`;
  taskSection.innerHTML = inputUser + inputStartingPoint + inputEndPoint + btnSave;
}

function save() {
  const user = document.querySelector("#inputUser").value;
  const startingPoint = document.querySelector("#inputStartingPoint").value;
  const endPoint = document.querySelector("#inputEndPoint").value;

  const formData = new FormData();
  formData.append("user", user);
  formData.append("startingPoint", startingPoint);
  formData.append("endPoint", endPoint);
  // XHR : PUT
  fetch("/update/" + taskId, {
    method: "PUT",
    body: formData,
  })
    .then((response) => response.json())
    .then(
      (data) =>
        (taskSection.innerHTML = `
		<h1 class="display-4 mt-3">
		<input id="taskId" type="hidden" value="${data.id}" />
		<span id="taskUser">${data.user}</span>
		</h1>
    <h1 class="display-4 mt-3">
		<input id="taskId" type="hidden" value="${data.id}" />
		<span id="taskStartingPoint">${data.startingPoint}</span>
		</h1>
    <h1 class="display-4 mt-3">
		<input id="taskId" type="hidden" value="${data.id}" />
		<span id="taskEndPoint">${data.endPoint}</span>
		</h1>
		<a class="btn btn-secondary" href="javascript: edit(this);">editar</a>`)
    );
}
