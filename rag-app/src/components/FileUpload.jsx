import React, { useState } from 'react';
import "../styles/FileUpload.css"

function FileUpload() {
 const [file, setFile] = useState(null);
 const [status, setStatus] = useState('');
 const handleChange = (e) => {
   setFile(e.target.files[0]);
   setStatus('');
 };

 const handleUpload = async () => {
   if (!file) {
     setStatus('Please upload a file.');
     return;
   }
   const formData = new FormData();
   formData.append('file', file);
   try {
     setStatus('Uploading...');
     const response = await fetch('http://localhost:8090/ingest', {
       method: 'POST',
       body: formData,
     });
     if (!response.ok) {
       throw new Error('Upload failed');
     }
     setStatus('Upload successful!');
   } catch (err) {
     setStatus('Upload failed. Please try again.');
     console.log(err)
   }
 };
 return (
    <div className="file-upload-container">
    <h2>Upload Excel or CSV File</h2>
    <input type="file" accept=".csv,.xlsx" onChange={handleChange} />
    <button onClick={handleUpload}>Upload</button>
        {status && <p className="status">{status}</p>}
    </div>
    );
}
export default FileUpload;