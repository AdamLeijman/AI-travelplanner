// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    destination: '',
    start_date: '',
    end_date: '',
    interests: '',
    budget: ''
  });

  const [loading, setLoading] = useState(false);
  const [itinerary, setItinerary] = useState('');

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setItinerary('');

    try {
      const response = await axios.post('http://localhost:8000/generate', {
        ...formData,
        interests: formData.interests.split(',').map(i => i.trim())
      });
      setItinerary(response.data.plan);
    } catch (error) {
      alert("Something went wrong: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>AI Travel Planner</h1>
      <form onSubmit={handleSubmit}>
        <input name="destination" placeholder="Destination" onChange={handleChange} required />
        <input name="start_date" type="date" onChange={handleChange} required />
        <input name="end_date" type="date" onChange={handleChange} required />
        <input name="interests" placeholder="Interests (comma separated)" onChange={handleChange} required />
        <input name="budget" type="number" placeholder="Budget (SEK)" onChange={handleChange} required />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Itinerary"}
        </button>
      </form>
      <div className="result">
        <pre>{itinerary}</pre>
      </div>
    </div>
  );
}

export default App;
