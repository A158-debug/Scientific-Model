import React  from 'react'

const App = () => {
  // const[fileData, setFiledata] = useState("");
  
  const uploadFile = (e) => {
    let file = e.target.files[0];
    var reader = new FileReader();
    reader.readAsText(file);
    reader.onload = (event)=>{
      console.log(event.target.result)

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