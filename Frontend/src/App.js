import React from 'react'
import HomePage from './components/HomePage/HomePage'
import Template1 from './components/Templates/Template1';
import Template2 from './components/Templates/Template2';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
const App = () => {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/template1" element={<Template1 />} />
          <Route path="/template2" element={<Template2 />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App