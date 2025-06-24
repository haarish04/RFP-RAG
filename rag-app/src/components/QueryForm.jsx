import React, { useState } from 'react';
import "../styles/QueryForm.css"
function QueryForm() {
 const [question, setQuestion] = useState('');
 const [results, setResults] = useState([]);
 const [enhancedAnswer, setEnhancedAnswer] = useState('');
 const [loading, setLoading] = useState(false);
 const [error, setError] = useState('');
 const handleSubmit = async (e) => {
   e.preventDefault();
   if (!question.trim()) {
     setError('Please enter a question.');
     return;
   }
   setLoading(true);
   setError('');
   setResults([]);
   setEnhancedAnswer('');
   try {
     const res = await fetch('http://localhost:8090/query', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify({ question }),
     });
     const data = await res.json();
     console.log('Response from backend:', data);
     if (res.ok) {
       // Use correct backend key
       setResults(data["matches"] || []);
       setEnhancedAnswer(data["LLM answer"] || '');
     } else {
       setError(data.detail || 'Something went wrong.');
     }
   } catch (err) {
     setError('Failed to connect to server.');
   } finally {
     setLoading(false);
   }
 };
 return (
<div className="query-form-container">
<h2>Ask a Question</h2>
<form onSubmit={handleSubmit}>
<input
         type="text"
         placeholder="Enter your question"
         value={question}
         onChange={(e) => setQuestion(e.target.value)}
       />
<button type="submit" disabled={loading}>
         {loading ? 'Searching...' : 'Submit'}
</button>
</form>
     {error && <p className="error">{error}</p>}
     {results.length > 0 && (
<div className="results">
<h3>Top Matches:</h3>
         {results.map((item, idx) => (
<div key={idx} className="result-item">
<strong>Question: </strong> {item.metadata.question || 'N/A'} <br />
<strong>Answer: </strong> {item.metadata.answer || 'N/A'} <br />
<strong>Similarity: </strong> {item.similarity || 'NA'}
</div>
         ))}
</div>
     )}
     {enhancedAnswer && (
<div className="llm-answer">
<h3>Enhanced Answer:</h3>
<p>{enhancedAnswer}</p>
</div>
     )}
</div>
 );
}
export default QueryForm;