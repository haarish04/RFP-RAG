import { useNavigate } from 'react-router-dom';
import tableImage from "../assets/table.png"
import aiImage from "../assets/ai.png"

import "../styles/Home.css"
function Home() {

  const navigate= useNavigate();
  return (
    <div className="home-container">
      <div className="box" onClick={() => navigate('/fileUpload')}>
        <img src={tableImage} alt="Upload" />
        <p>Upload Files</p>
      </div>
      <div className="box" onClick={() => navigate('/query')}>
        <img src={aiImage} alt="Query" />
        <p>Query</p>
      </div>
    </div>
  )
}

export default Home;
