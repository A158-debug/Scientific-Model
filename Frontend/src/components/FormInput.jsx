import React from "react";

const FormInput = ({name, type, value}) => {
  return (
    <>
      <div className="flex flex-row justify-between p-2 border">   
        <p className="text-lg text-black-400 font-semibold">{name}</p>    
        <input type={type} className="border rounded-md px-2 py-1" value={value}/>
      </div>
    </>
  );
};

export default FormInput;
