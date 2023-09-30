// pages/index.tsx
"use client"
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Table from '../components/Table';

// "use client"
const HomePage = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/project-management/api/v1/projects?page=0&limit=100');
        console.log(response);
        setData(response.data.data); // Update to access the 'data' property in the API response
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Projects Table</h1>
      <Table data={data} />
    </div>
  );
};

export default HomePage;
