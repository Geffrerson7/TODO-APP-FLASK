function deleteTaskConfirmation(event, taskId) {
    event.preventDefault();
    Swal.fire({
      title: "Are you sure?",
      text: "You will not be able to recover this task!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, delete it!",
    }).then((result) => {
      if (result.isConfirmed) {
        fetch(`/delete/${taskId}`, {
          method: "POST",
        })
          .then((response) => {
            if (response.ok) {
              Swal.fire({
                title: "Deleted!",
                text: "Your task has been deleted.",
                icon: "success",
              }).then(() => {
                location.reload();
              });
            } else {
              Swal.fire({
                title: "Error",
                text: "Failed to delete Task",
                icon: "error",
              });
            }
          })
          .catch((error) => console.error("Error:", error));
      }
    });
  }