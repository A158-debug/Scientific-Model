import React from 'react'
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <>
      <div className="p-5 flex flex-row app__navbar">
          <div className="basis-4/12">
            <img
              src="https://assets.website-files.com/613e7a6e19fd8f65b8d29b8e/613fff34608e624b738e4035_logo.svg"
              loading="lazy" alt="" className="cursor-pointer logoImage" height="150px"width="150px"></img>
          </div>
          <div className="basis-8/12 self-center flex flex-row">
            <Link to="/" className="p-2 rounded">
              <p className="text-xl hover:text-sky-400  mx-3">Home</p>
            </Link>
            <Link to="/" className="p-2 rounded">
              <p className="text-xl hover:text-sky-400  mx-3">About</p>
            </Link>
          </div>
      </div>
    </>
  )
}

export default Navbar