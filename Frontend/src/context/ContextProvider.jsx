import React,  { createContext, useState } from 'react'

export const stateContext = createContext()

const ContextProvider = ({children}) => {
    const [Gdata, setGdata] = useState({})
    const [magneticAtoms, setmagneticAtoms] = useState({})
    const [fileData, setfileData] = useState()
    
  const [otherPara, setOtherPara] = useState({
    Material_Thickness: "",
    accelerating_volt: "",
    h_para: "",
    k_para: "",
    l_para: "",
  });

    const value = {Gdata, setGdata,fileData, setfileData,magneticAtoms, setmagneticAtoms,otherPara,setOtherPara}
    
  return (
    <stateContext.Provider value={value}>
        {children}
    </stateContext.Provider>
  )
}

export default ContextProvider