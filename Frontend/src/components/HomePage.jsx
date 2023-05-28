import React, { useContext } from "react";
import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";
import FileInput from "./FileInput";
import axios from "axios";


const HomePage2 = () => {
  const navigate = useNavigate();
  const { setGdata, fileData } = useContext(stateContext);

  const handleOnClick = async (e) => {
    e.preventDefault();
    if (!fileData) {
      return alert("Please select a file");
    }
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ fileData }),
    };
    const response = await axios.post(
      "http://127.0.0.1:5000/file_data",
      requestOptions
    );
    if (response) {
      setGdata(response?.data?.output);
      navigate("/fileinfo");
    } else alert("Something went wrong");
  };
  return (
    <section className="">
      <div className="flex flex-col  p-5 mt-10 w-full md:w-3/5">
        <div className="flex flex-col justify-center content-center">
          <h1 className="text-5xl font-semibold md:text-8xl md:p-0 md:font-semibold">
            EMCD Calculation
          </h1>
          <p className="text-xl p-3 text-left">
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
