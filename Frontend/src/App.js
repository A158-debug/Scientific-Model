import React from 'react'
import HomePage from './components/HomePage'
import FileInfo from './pages/FileInfo';
import AtomicPosition from './pages/AtomicPosition';
import OptimumValues from './pages/OptimumValues';

import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
const App = () => {

  return (
    <>
      <section className="parent_app">
        <BrowserRouter>
          <Navbar />
          <Routes>
            <Route path="/" forceRefresh={true} element={<HomePage />} />
            <Route path="/fileinfo" element={<FileInfo />} />
            <Route path="/atomicPosition" element={<AtomicPosition />} />
            <Route path="/optimumvalues" element={<OptimumValues />} />
          </Routes>
        </BrowserRouter>
      </section>
    </>
  )
}

export default App