import React , {useContext} from "react";
import {stateContext} from '../context/ContextProvider'
import { Link } from "react-router-dom";
import Form from "../Form";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import './HomePage.css'

const HomePage2 = () => {
    const navigate = useNavigate();
    const {setGdata, fileData} = useContext(stateContext);
    const handleOnClick = async (e) => {
      e.preventDefault();
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ filedata: fileData }),
      };
      const response = await axios.post("http://127.0.0.1:5000/file-data",requestOptions)
      // console.log(response)
      setGdata(response?.data?.output)
      if(response) navigate("/template1");
      else navigate("/")
    };
  return (
    <div className="background-img">
      <div className="nav-bar p-5">
        <div className="flex flex-row">
          <div className="basis-4/12">
            <img
              src="https://assets.website-files.com/613e7a6e19fd8f65b8d29b8e/613fff34608e624b738e4035_logo.svg"
              loading="lazy"
              alt=""
              className="cursor-pointer "
              height="150px"
              width="150px"
            ></img>
          </div>
          <div className="basis-8/12 self-center flex flex-row">
            <Link to="/" className="hover:bg-amber-200 p-2 rounded">
              <p className="text-xl text-amber-900 font-semibold mx-3">Home</p>
            </Link>
            <Link to="/" className="hover:bg-amber-200 p-2 rounded">
              <p className="text-xl text-amber-900 font-semibold mx-3">
                About Us
              </p>
            </Link>
          </div>
        </div>
      </div>
      <div className="flex flex-row">
        <div className="flex flex-col justify-center items-center basis-1/2  mt-10">
          <p className="heading-homePage font-sans font-semibold text-red-700">
            Welcome To Our Website
          </p>
          <p className="paragraph-large my-5 px-5 ">
            A highly scalable, fast and secure platform for calculation of
            G-Optimization. Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </p>
          <div>
            <Form />
          </div>
          <div className="mt-8">
            <button
              href="/"
              className="get-started-button"
              onClick={handleOnClick}
            >
              Get Started
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage2;
