function updateTask(event, taskId) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  fetch(`/update-task/${taskId}`, {
    method: "PUT",
    body: formData,
  }).then((response) => {
    if (response.ok) {
      response.json().then((data) => {
        Swal.fire({
          title: "Success",
          text: data.message,
          icon: "success",
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = `/task/${taskId}`;
          }
        });
      });
    } else {
      Swal.fire({
        title: "Error",
        text: "Failed to update task",
        icon: "error",
      });
    }
  });
}
