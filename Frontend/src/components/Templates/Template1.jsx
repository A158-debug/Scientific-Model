import React, { useContext, useState } from "react";
import FormInput from "../FormInput";
import temp1svg from "../images/temp1svg.svg";
import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
const Template1 = () => {
  const { Gdata } = useContext(stateContext);
  const navigate = useNavigate();
  const [otherPara, setOtherPara] = useState({
    Material_Thickness: "",
    accelerating_volt: "",
    alpha_Para: "",
    beta_Para: "",
    gamma_Para: "",
  });

  const handleOnTemplate2 = () => {
    navigate("/template2");
  };
  // console.log(Gdata);

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
          <div className="basis-8/12">
            <div className="justify-center content-center m-2 p-3 glass-background">
              <form action="" className="border p-3">
                <div className="flex flex-col">
                  <div className="flex flex-row justify-between">
                    <FormInput name="Title :" value={Gdata.Material_Name} />
                    <FormInput name="Lattice  :" value={Gdata.Lattice_Type} />
                  </div>

                  <div className="container mt-2">
                    <div className="mt-5 ml-3 flex flex-row content-center">
                      <p className="text-lg text-black-400 basis-5/12">
                        Material Thickness :
                      </p>
                      <div className="basis-7/12">
                        <input
                          name="Material thickness :"
                          value={otherPara.Material_Thickness}
                          onChange={(e) =>
                            setOtherPara({
                              ...otherPara,
                              Material_Thickness: e.target.value,
                            })
                          }
                          placeholder="Default value is 10nm"
                          className="border rounded-md  px-2 py-1 w-7/12"
                        />
                      </div>
                    </div>
                    <div className="mt-5 ml-3 flex flex-row content-center">
                      <p className="text-lg text-black-400 basis-5/12">
                        Accelerating voltage :
                      </p>
                      <div className="basis-7/12">
                        <input
                          name="Material thickness :"
                          value={otherPara.accelerating_volt}
                          onChange={(e) =>
                            setOtherPara({
                              ...otherPara,
                              accelerating_volt: e.target.value,
                            })
                          }
                          placeholder="Voltage"
                          className="border rounded-md  px-2 py-1 w-7/12"
                        />
                      </div>
                    </div>
                    <div className="mt-5 ml-3 flex flex-row content-center">
                      <p className="text-lg text-black-400 basis-5/12">
                        Inequivalent atoms :
                      </p>
                      <div className="basis-7/12">
                        <input
                          name="Material thickness :"
                          value={Gdata.Inequivalent_Atoms}
                          className="border rounded-md  px-2 py-1 w-7/12"
                        />
                      </div>
                    </div>
                    
                    <label className="block mt-3">
                      <span className="text-lg block font-normal  ml-3">
                        Lattice Parameters &nbsp; :
                      </span>
                      <div className="flex flex-row my-1">
                        <FormInput value={Gdata.Lattice_Parameter[0]} />
                        <FormInput value={Gdata.Lattice_Parameter[1]} />
                        <FormInput value={Gdata.Lattice_Parameter[2]} />
                      </div>
                      <div className="flex flex-row my-1">
                        <FormInput value={Gdata.Lattice_Parameter[3]} />
                        <FormInput value={Gdata.Lattice_Parameter[4]} />
                        <FormInput value={Gdata.Lattice_Parameter[5]} />
                      </div>
                    </label>
                    <label className="block mt-3">
                      <span className="text-lg block font-normal  ml-3 my-1">
                        G Vector &nbsp; :
                      </span>
                      <div className="flex flex-row my-1 justify-around">
                        <input
                          className="border rounded-md ml-3 px-2 py-1"
                          value={otherPara.alpha_Para}
                          onChange={(e) =>
                            setOtherPara({
                              ...otherPara,
                              alpha_Para: e.target.value,
                            })
                          }
                          placeholder="Enter the h value"
                        />
                        <input
                          className="border rounded-md ml-3 px-2 py-1"
                          value={otherPara.beta_Para}
                          onChange={(e) =>
                            setOtherPara({
                              ...otherPara,
                              beta_Para: e.target.value,
                            })
                          }
                          placeholder="Enter the k value"
                        />
                        <input
                          className="border rounded-md ml-3 px-2 py-1"
                          value={otherPara.gamma_Para}
                          onChange={(e) =>
                            setOtherPara({
                              ...otherPara,
                              gamma_Para: e.target.value,
                            })
                          }
                          placeholder="Enter the l value"
                        />
                      </div>
                    </label>
                  </div>

                  <div className="flex flex-row justify-between mt-3">
                    <div className="">
                      <button className="rounded bg-red-500 text-white p-2 w-20 hover:shadow-lg">
                        Exit
                      </button>
                    </div>
                    <div className="">
                      <button
                        className="rounded bg-blue-500 text-white p-2 w-20 hover:shadow-lg"
                        onClick={handleOnTemplate2}
                      >
                        Next
                      </button>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Template1;
