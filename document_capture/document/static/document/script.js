document.getElementById('uploadForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const formData = new FormData();
  const documentPdf = document.getElementById('documentPdf').files[0];
  formData.append('document_pdf', documentPdf);

  try {
    const response = await fetch('http://localhost:8000/api/aadhar/', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error('Failed to upload document.');
    }

    const data = await response.json();

    document.getElementById('aadharNumber').textContent = data.aadhar_number;
    document.getElementById('extractedData').classList.remove('hidden');

  } catch (error) {
    console.error(error.message);
  }
});
