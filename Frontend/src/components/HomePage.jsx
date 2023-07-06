import React, { useContext, useState } from "react";

import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";

import { URL } from "../constants";
import FileInput from "./FileInput";
import axios from "axios";

const HomePage2 = () => {
  const navigate = useNavigate();
  const [showAlert, setShowAlert] = useState(false);
  const { setGdata, fileData } = useContext(stateContext);

  const handleOnClick = async (e) => {
    e.preventDefault();
    if (!fileData) {
      setShowAlert(true);
      setTimeout(() => {
        setShowAlert(false);
      }, 3000);
      return;
    }
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ fileData }),
    };
    const response = await axios.post(
      `${URL}/file_data`,
      requestOptions
    );
    if (response) {
      setGdata(response?.data?.output);
      navigate("/fileinfo");
    } else alert("Something went wrong");
  };

  const handleChangeAlert = () => {
    setShowAlert(false);
  };

  return (
    <section className="">
      {showAlert && (
        <div className="my-4 p-4 bg-red-500 text-white rounded w-10/12 flex justify-between items-center mx-auto">
          <span className="text-lg">Please select a file</span>
          <span className=" px-4 py-3" onClick={handleChangeAlert}>
            <svg
              className="fill-current h-6 w-6 text-white-primary"
              role="button"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <title>Close</title>
              <path d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z" />
            </svg>
          </span>
        </div>
      )}
      <div className="flex flex-col p-2 md:p-10 mt-10 w-full md:w-3/5 ">
        <div className="flex flex-col justify-center content-center">
          <h1 className="text-5xl font-semibold md:text-8xl md:p-0 md:font-semibold ">
            Optimized EMCD Scientific Model
          </h1>
          <p className="text-xl text-left my-5 text-slate-200">
            In this website you can finds an optimized thickness and diffraction
            geometry in order to obtain the maximum attainable energy-loss
            magnetic chiral dichroism (EMCD) signal for a given crystal
            structure using Transmission Electron Microscopy.
          </p>
        </div>
        <FileInput />
        <div className="mt-5 text-center">
          <button
            href="/"
            className="get-started-button"
            onClick={handleOnClick}
          >
            Get Started
          </button>
        </div>
      </div>
    </section>
  );
};

export default HomePage2;
