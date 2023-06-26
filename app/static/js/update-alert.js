function updateTask(event, taskId) {
    event.preventDefault();
  
    const form = event.target;
    const formData = new FormData(form);
  
    fetch(`/update-task/${taskId}`, {
      method: "PUT",
      body: formData,
    }).then((response) => {
      if (response.ok) {
        Swal.fire({
          title: "Success",
          text: "Task updated successfully",
          icon: "success",
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = `/task/${taskId}`;
          }
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