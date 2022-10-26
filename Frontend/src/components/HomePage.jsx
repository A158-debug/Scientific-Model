import React from "react";
import "./HomePage.css";
import Form from "./Form"

const HomePage = () => {
  return (
    <div
      className="h-screen text-white flex justify-center flex-col"
      style={{
        backgroundColor: "#0B0B45",
      }}
    >
      <div className="nav-bar p-5">     
        <img
          src="https://assets.website-files.com/613e7a6e19fd8f65b8d29b8e/613fff34608e624b738e4035_logo.svg"
          loading="lazy"
          alt=""
          class="logo">
        </img>
      </div>
      <div className="h-screen text-white flex justify-center items-center flex-col ">
        <p className="heading-hero font-sans font-semibold">
          Welcome To Our Website
        </p>
        <p className="paragraph-large my-5">
          A highly scalable, fast and secure platform for calculation of
          G-Optimization
        </p>
        <div><Form/></div>
        <div className="mt-8"><a href="/get-started" class="get-started-button">Get Started</a></div>
      </div>
    </div>
  );
};

export default HomePage;
