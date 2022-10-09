import React from 'react'

const App = () => {
  const uploadFile = (e) => {
    let file = e.target.files[0];
    var reader = new FileReader();
    reader.readAsText(file);
    reader.onload = (event) => {
      let data = event.target.result
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({'filedata':data})
      };
      const response = fetch('http://127.0.0.1:5000/file-data', requestOptions)
      console.log(response)
    };
    e.target.value = null;
  }

  return (
    <div className="main-app">
      <p className="main-heading text-white"> Welcome To ElectronNova</p>
      <div className="input-group">
        <input type="file" className="form-control" id="inputGroupFile02" onChange={uploadFile} />
        <label className="input-group-text" htmlFor="inputGroupFile02">Upload</label>
      </div>
    </div>
  )
}

export default App