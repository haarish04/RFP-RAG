import React from 'react';
import QueryForm from '../components/QueryForm';
import { useNavigate } from 'react-router-dom';

function QueryPage() {
    const navigate = useNavigate();
 return(
    <div>
        <QueryForm />
        <div className="box" onClick={() => navigate('/fileUpload')} style = {{marginLeft:'600px', marginTop:'100px'}}>
            <p>Upload File</p>
        </div>
    </div>
 );
}
export default QueryPage;