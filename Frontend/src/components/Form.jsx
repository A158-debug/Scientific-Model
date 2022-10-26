import React from "react";
import file from './file.svg'

const Form = () => {
    const uploadFile = (e) => {
        let file = e.target.files[0];
        var reader = new FileReader();
        reader.readAsText(file);
        reader.onload = (event) => {
          let data = event.target.result
          console.log(data)
          const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'filedata': data })
          };
          const response = fetch('http://127.0.0.1:5000/file-data', requestOptions)
          response.then((responseData) => { console.log(responseData) }).catch((error) => { console.log(error) })
        };
        e.target.value = null;
      }
  return (
    <div>
      <form className="flex items-center space-x-6 mt-10 ml-10">
        <div classname="shrink-0">
          <img
            className="h-16 w-16 object-cover rounded-full"
            src={file}
            alt=""
          />
        </div>
        <label className="block ">
          <input
            type="file"
            className="block w-full text-sm text-slate-500
         file:mr-4 file:py-2 file:px-4
         file:rounded-full file:border-0
         file:text-sm file:font-semibold
        file:bg-violet-50 file:text-violet-700
        hover:file:bg-violet-100 cursor-pointer"

            onChange={uploadFile}
          />
        </label>
      </form>
    </div>
  );
};

export default Form;
