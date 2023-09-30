import Image from 'next/image'
import HomePage from './pages/index'; // Import the index.tsx file
import Table from './components/Table'; 

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
      {/* <Table data={customData} /> */}
      {/* <hr className="my-6" /> */}
      <HomePage /> {/* Render the HomePage component */}
    </div>
    </main>
  )
}
