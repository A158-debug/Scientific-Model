import React from "react";

const FormInput = ({name, type, value}) => {
  return (
    <>
      <div className="flex flex-row justify-between p-3 ">   
        <div><p className="text-lg text-black-400">{name}</p></div>    
        <div className="">
          <input type={type} className="border rounded-md ml-3 px-2 py-1 " value={value}/>
        </div>
      </div>
    </>
  );
};

export default FormInput;
