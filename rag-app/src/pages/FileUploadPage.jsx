import React from 'react';
import FileUpload from '../components/FileUpload';
import { useNavigate } from 'react-router-dom';

function FileUploadPage() {
    const navigate= useNavigate();

 return (
    <div>
        <FileUpload />
        <div className="box" onClick={() => navigate('/query')} style = {{marginLeft:'600px', marginTop:'100px'}}>
            <p>Query</p>
        </div>
    </div>
    );
}
export default FileUploadPage;