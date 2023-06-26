function createTask(event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  fetch("/new-task", {
    method: "POST",
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
            window.location.href = "/";
          }
        });
      });
    } else {
      Swal.fire({
        title: "Error",
        text: "Failed to create task",
        icon: "error",
      });
    }
  });
}
