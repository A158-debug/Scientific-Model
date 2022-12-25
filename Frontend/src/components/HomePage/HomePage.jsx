import React , {useContext} from "react";
import {stateContext} from '../context/ContextProvider'
import {useNavigate } from "react-router-dom";
import Form from "../Form";
import axios from 'axios';
import './HomePage.css'

const HomePage2 = () => {
    const navigate = useNavigate();
    const {setGdata, fileData} = useContext(stateContext);

    const handleOnClick = async (e) => {
      e.preventDefault();
      // console.log(fileData);
      // if(!fileData){
      //     return alert('Please select a file')
      // }
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ filedata: fileData }),
      };
      const response = await axios.post("http://127.0.0.1:5000/file-data",requestOptions)
      if(response){
        setGdata(response?.data?.output)
        navigate("/template1");
      }
      else alert('Something went wrong')
    };
  return (
    <section className="background-img homePage">
      <div className="homePageContent flex self-center justify-center">
        <div className="flex flex-col justify-center content-center">
          <h1 className="homePageHeading font-sans text-5xl p-3 font-semibold md:text-8xl md:p-0 md:font-semibold  text-sky-700">Welcome To Our Website</h1>
          <p className="text-xl p-5">
            A highly scalable, fast and secure platform for calculation of
            G-Optimization. Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </p>
         <Form/>
          <div className="text-center my-5">
            <button href="/" className="get-started-button" onClick={handleOnClick}>Get Started</button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HomePage2;
