import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/vaccines/')
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Travel Vaccines by Country</h1>
      <ul>
        {Object.entries(data).map(([country, vaccines]) => (
          <li key={country}>
            <strong>{country}</strong>
            <ul>
              {vaccines.map(vaccine => (
                <li key={vaccine}>{vaccine}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;