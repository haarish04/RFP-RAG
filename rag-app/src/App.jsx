import HomePage from './pages/HomePage.jsx'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import FileUploadPage from './pages/FileUploadPage.jsx'
import QueryPage from './pages/QueryPage.jsx'

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/fileUpload" element={<FileUploadPage/>}/>
        <Route path="/query" element={<QueryPage/>}/>
      </Routes>
    </Router>
  )
}

export default App
