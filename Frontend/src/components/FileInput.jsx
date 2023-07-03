import React, { useContext } from "react";
import { stateContext } from "../context/ContextProvider";

const FileInput = () => {
  const { setfileData } = useContext(stateContext);
  const uploadFile = (e) => {
    let file = e.target.files[0];
    var reader = new FileReader();
    reader.readAsText(file);
    reader.onload = (event) => {
      let filedata = event.target.result;
      //console.log(filedata);
      setfileData(filedata);
    };
  };
  return (
    <div className="cursor-pointer">
      <form className="flex justify-center items-center space-x-6 mt-5 ml-5">
        <label className="block">
          <input
            type="file"
            className="block w-full text-sm text-slate-500
         file:mr-4 file:py-2 file:px-4
         file:rounded-full file:border-0
         file:text-sm file:font-semibold
        file:bg-violet-50 file:text-violet-700
        hover:file:bg-violet-100 "
            onChange={uploadFile}
          />
        </label>
      </form>
    </div>
  );
};

export default FileInput;
