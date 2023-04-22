import React,  { createContext, useState } from 'react'

export const stateContext = createContext()

const ContextProvider = ({children}) => {
    const [Gdata, setGdata] = useState({})
    const [magneticAtoms, setmagneticAtoms] = useState({})
    const [fileData, setfileData] = useState()

    const value = {Gdata, setGdata,fileData, setfileData,magneticAtoms, setmagneticAtoms}
    
  return (
    <stateContext.Provider value={value}>
        {children}
    </stateContext.Provider>
  )
}

export default ContextProvider