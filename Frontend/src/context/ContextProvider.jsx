import React,  { createContext, useState } from 'react'

export const stateContext = createContext()

const ContextProvider = ({children}) => {
    const [Gdata, setGdata] = useState({})
    const [fileData, setfileData] = useState()
    
  return (
    <stateContext.Provider value={{Gdata, setGdata,fileData, setfileData}}>
        {children}
    </stateContext.Provider>
  )
}

export default ContextProvider