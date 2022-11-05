import React, { useContext } from "react";
import FormInput from "../FormInput";
import temp1svg from "../images/temp1svg.svg";
import { stateContext } from "../context/ContextProvider";
import { Link } from "react-router-dom";

const Template2 = () => {
  const { Gdata } = useContext(stateContext);
  // "Mult_List": "['4', '4']",
  // "X_Coordinate_List": ['0.13500000', '0.63500000', '0.86500000', '0.36500000', '0.84200000', '0.34200000', '0.15800000', '0.65800000'],
  // "Y_Coordinate_List": ['0.13500000', '0.36500000', '0.63500000', '0.86500000', '0.84200000', '0.65800000', '0.34200000', '0.15800000'],
  // "Z_Coordinate_List": ['0.13500000', '0.86500000', '0.36500000', '0.63500000', '0.84200000', '0.15800000', '0.65800000', '0.34200000']
  const coordinates = ()=>{
    for(let i=0;i<Gdata.Mult_List.length;i++){
      let atom=[]
        for(let j=0;j<parseInt(Gdata.Mult_List[i]); j++){
              atom.push(parseInt(Gdata.X_Coordinate_List[i]))
              atom.push(parseInt(Gdata.Y_Coordinate_List[i]))
              atom.push(parseInt(Gdata.Z_Coordinate_List[i]))
        }
    }
  }
  return (
    <>
      <div className="template1-background flex flex-col content-center ">
        <div className="nav-bar p-5">
          <div className="flex flex-row">
            <div className="basis-1/2">
              <img
                src="https://assets.website-files.com/613e7a6e19fd8f65b8d29b8e/613fff34608e624b738e4035_logo.svg"
                loading="lazy"
                alt=""
                className="cursor-pointer "
                height="150px"
                width="150px"
              ></img>
            </div>
            <div className="basis-1/2 self-center flex flex-row">
              <Link to="/" className="hover:bg-amber-200 p-2 rounded">
                <p className="text-xl text-amber-900 font-semibold mx-3">
                  Home
                </p>
              </Link>
              <Link to="/" className="hover:bg-amber-200 p-2 rounded">
                <p className="text-xl text-amber-900 font-semibold mx-3">
                  About Us
                </p>
              </Link>
            </div>
          </div>
        </div>
        <div className="div flex flex-row">
          <div className="basis-4/12 flex flex-row justify-center content-center">
            <img src={temp1svg} alt="" className="" />
          </div>
          </div>
        {/* <div className="basis-8/12 justify-center content-center m-3 p-3">
          <form action="" className="border p-3">
            <div className="flex flex-col">
              <div className="container">
                <label className="block ">
                  <span className="text-lg block font-normal text-slate-700 ml-3">
                    Fe &nbsp; :
                  </span>
                  <div classname="flex flex-row my-1">
                    <div className="ml-2 my-2">
                      <FormInput name="x" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="y" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="z" type="text" />
                    </div>
                  </div>
                  <div className="flex flex-row my-1">
                    <div className="ml-2">
                      <FormInput name="x" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="y" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="z" type="text" />
                    </div>
                  </div>
                  <div className="flex flex-row my-1">
                    <div className="ml-2">
                      <FormInput name="x" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="y" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="z" type="text" />
                    </div>
                  </div>
                  <div className="flex flex-row my-1">
                    <div className="ml-2">
                      <FormInput name="x" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="y" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="z" type="text" />
                    </div>
                  </div>
                </label>
                <label className="block ">
                  <span classname="text-lg block font-normal text-slate-700 ml-3">
                    Ge &nbsp; :
                  </span>
                  <div className="flex flex-row my-1">
                    <div className="ml-2">
                      <FormInput name="x" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="y" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="z" type="text" />
                    </div>
                  </div>
                  <div className="flex flex-row my-1">
                    <div className="ml-2">
                      <FormInput name="x" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="y" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="z" type="text" />
                    </div>
                  </div>
                  <div className="flex flex-row my-1">
                    <div className="ml-2">
                      <FormInput name="x" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="y" type="text" />
                    </div>
                    <div className="ml-2">
                      <FormInput name="z" type="text" />
                    </div>
                  </div>
                </label>
              </div>

              <div classname="flex flex-row justify-between mt-3">
                <div classname="">
                  <button classname="rounded bg-red-400 text-white p-2 w-20">
                    Exit
                  </button>
                </div>
                <div classname="">
                  <button classname="rounded bg-blue-400 text-white p-2 w-20">
                    Next
                  </button>
                </div>
              </div>
            </div>
          </form>
        </div> */}
      </div>
    </>
  );
};

export default Template2;
