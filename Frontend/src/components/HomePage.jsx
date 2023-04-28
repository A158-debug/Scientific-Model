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
      body: JSON.stringify({fileData}),
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
    <section className="background-img homePage">
      <div className="flex flex-col text-center p-5 mt-10">
        <div className="flex flex-col justify-center content-center">
          <h1 className="text-5xl font-semibold md:text-8xl md:p-0 md:font-semibold">
          EMCD Calculation
          </h1>
          <p className="text-xl p-3">
            In this website you can predict optimal Bragg spot G for
            measurements of energy-loss magnetic chiral dichroism (EMCD) in a
            two-beam orientation.
          </p>
        </div>
        <FileInput />
        <div className="mt-5">
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
