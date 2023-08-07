document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('images');
    const fileLabel = document.getElementById('file-label');
  
    fileInput.addEventListener('change', (event) => {
      const filesSelected = event.target.files;
      if (filesSelected.length > 0) {
        fileLabel.textContent = `${filesSelected.length} file(s) selected`;
      } else {
        fileLabel.textContent = 'Click to choose Images';
      }
    });
  });
  
