// components/Table.tsx
import React, { useState } from 'react';

// Helper function to convert a string to PascalCase with spaces
const toPascalCase = (str) => {
  return str.replace(/_([a-z])/g, (_, match) => ` ${match.toUpperCase()}`).replace(/^\w/, (c) => c.toUpperCase());
};

const GalleryView = ({ data }) => {
  const [selectedProject, setSelectedProject] = useState(null);

  const openSidebar = (project) => {
    setSelectedProject(project);
  };

  const closeSidebar = () => {
    setSelectedProject(null);
  };

  if (!data || data.length === 0) {
    return <p>No data available.</p>;
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
      {data.map((item, index) => (
        <div key={index} className="relative p-8 bg-gray-100 border border-gray-300 rounded-md shadow-md ">
          <h3 className="text-xl font-semibold mb-4 text-gray-800">{item.project_title}</h3>
          <div className="mb-4">
            {Object.entries(item).map(([key, value]) => (
              <div key={key} className="mb-2">
                <span className="font-semibold text-gray-700">{toPascalCase(key)}</span>: <span className="text-gray-800">{value}</span>
              </div>
            ))}
          </div>
          <button
            className="absolute bottom-4 left-1/2 transform -translate-x-1/2 bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition"
            onClick={() => openSidebar(item)}
          >
            View Details
          </button>
        </div>
      ))}
      {selectedProject && (
        <div className="fixed inset-0 overflow-hidden z-50 bg-gray-800 bg-opacity-75 flex items-center justify-center">
          <div className="bg-white p-8 rounded-md shadow-md max-w-md w-full">
            <h2 className="text-2xl font-semibold mb-4 text-gray-800">{selectedProject.project_title}</h2>
            {Object.entries(selectedProject).map(([key, value]) => (
              <div key={key} className="mb-2">
                <span className="font-semibold text-gray-700">{toPascalCase(key)}</span>: <span className="text-gray-800">{value}</span>
              </div>
            ))}
            <button
              className="mt-4 bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition"
              onClick={closeSidebar}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default GalleryView;
