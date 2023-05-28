<<<<<<< HEAD
import React, { useContext, useState } from "react";
=======
import React, { useContext } from "react";
>>>>>>> codebase2
import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";

const Template1 = () => {
<<<<<<< HEAD
  const { Gdata, magneticAtoms, setmagneticAtoms } = useContext(stateContext);
  const navigate = useNavigate();

  const [otherPara, setOtherPara] = useState({
    Material_Thickness: "",
    accelerating_volt: "",
    alpha_Para: "",
    beta_Para: "",
    gamma_Para: "",
  });

  const handleOnTemplate2 = async () => {
    navigate("/atomicposition");

=======
  const { Gdata, magneticAtoms, setmagneticAtoms, otherPara, setOtherPara } = useContext(stateContext);
  const navigate = useNavigate();

  const handleOnTemplate2 = async () => {
    if(otherPara.h_para==="" || otherPara.k_para==="" || otherPara.l_para===""){
      alert("Please enter all required values");
    }else navigate("/atomicposition");
  };

  const handleOnMainPage = async () => {
    navigate("/");
>>>>>>> codebase2
  };

  const handleOnSelectMagneticAtoms = (e) => {
    setmagneticAtoms({ ...magneticAtoms, [e.target.name]: e.target.checked });
  };

  return (
    <>
      <div className="flex flex-col justify-center content-center">
<<<<<<< HEAD
        <form action="" className="flex justify-center">
=======
        <div className="flex justify-center">
>>>>>>> codebase2
          <div className="flex flex-col p-3 w-4/5 ">
            {/*----------- Title & Lattice --------   */}
            <div className="flex flex-col md:flex-row">
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">Title :</p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
                    defaultValue={Gdata.Material_Name}
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                  />
                </div>
              </div>
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">Lattice :</p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
                    defaultValue={Gdata.Lattice_Type}
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                  />
                </div>
              </div>
            </div>

            {/*----------- Inequivalent Atoms & Accelerating voltage : --------   */}
            <div className="flex flex-col md:flex-row">
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">
                  Inequivalent Atoms:
                </p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
                    defaultValue={Gdata.Inequivalent_Atoms}
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                  />
                </div>
              </div>
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">
                  Accelerating voltage :
                </p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
<<<<<<< HEAD
=======
                    type="number"
>>>>>>> codebase2
                    onChange={(e) =>
                      setOtherPara({
                        ...otherPara,
                        accelerating_volt: e.target.value,
                      })
                    }
<<<<<<< HEAD
=======
                    value={otherPara.accelerating_volt}
>>>>>>> codebase2
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                    placeholder="Enter voltage value"
                  />
                </div>
              </div>
            </div>

<<<<<<< HEAD
=======
            {/*----------- Material thickness --------   */}
            <div className="flex flex-col md:flex-row">
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">Thickness :</p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                    value={otherPara.Material_Thickness}
                    placeholder="thickness in (nm)"
                    type="number"
                      onChange={(e) =>
                        setOtherPara({
                          ...otherPara,
                          Material_Thickness: e.target.value,
                        })
                      }
                  />
                </div>
              </div>
            </div>

>>>>>>> codebase2
            {/*----------- Lattice Parameters --------   */}
            <div className="mt-5">
              <p className="text-lg block mt-3">Lattice Parameters &nbsp; :</p>
              <div className="flex flex-col md:flex-row mt-3 gap-3">
                <div className="basis-1/3">
                  <div className="">
                    <input
<<<<<<< HEAD
                      name="Material thickness :"
=======
                      name=" :"
>>>>>>> codebase2
                      defaultValue={Gdata.Lattice_Parameter[0]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
<<<<<<< HEAD
                      name="Material thickness :"
=======
                      name=" :"
>>>>>>> codebase2
                      defaultValue={Gdata.Lattice_Parameter[1]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
<<<<<<< HEAD
                      name="Material thickness :"
=======
                      name=" :"
>>>>>>> codebase2
                      defaultValue={Gdata.Lattice_Parameter[2]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
              </div>
              <div className="flex flex-col md:flex-row mt-3 gap-3">
                <div className="basis-1/3">
                  <div className="">
                    <input
<<<<<<< HEAD
                      name="Material thickness :"
=======
                      name=" :"
>>>>>>> codebase2
                      defaultValue={Gdata.Lattice_Parameter[3]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
<<<<<<< HEAD
                      name="Material thickness :"
=======
                      name=""
>>>>>>> codebase2
                      defaultValue={Gdata.Lattice_Parameter[4]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
<<<<<<< HEAD
                      name="Material thickness :"
=======
                      name=""
>>>>>>> codebase2
                      defaultValue={Gdata.Lattice_Parameter[5]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
              </div>
            </div>

            {/*----------- G Vector Range --------   */}
            <div className="mt-5">
              <p className="text-lg block mt-3">G Vector Range &nbsp; :</p>
              <div className="flex flex-col md:flex-row mt-3 gap-3">
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="h_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg pl"
                      placeholder="Enter h value"
<<<<<<< HEAD
=======
                      value={otherPara.h_para}
                      type="number"
                      onChange={(e) =>
                        setOtherPara({
                          ...otherPara,
                          h_para: e.target.value,
                        })
                      }
>>>>>>> codebase2
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="k_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                      placeholder="Enter k value"
<<<<<<< HEAD
=======
                      value={otherPara.k_para}
                      type="number"
                      onChange={(e) =>
                        setOtherPara({
                          ...otherPara,
                          k_para: e.target.value,
                        })
                      }
>>>>>>> codebase2
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="l_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                      placeholder="Enter l value"
<<<<<<< HEAD
=======
                      value={otherPara.l_para}
                      type="number"
                      onChange={(e) =>
                        setOtherPara({
                          ...otherPara,
                          l_para: e.target.value,
                        })
                      }
>>>>>>> codebase2
                    />
                  </div>
                </div>
              </div>
            </div>
<<<<<<< HEAD
=======

            {/*----------- Magnetic Atoms --------   */}
>>>>>>> codebase2
            <div className="mt-5">
              <p className="text-lg block mt-3">
                Select the magnetic atoms &nbsp; :
              </p>
              <div className=" my-2 p-2 flex  flex-wrap">
<<<<<<< HEAD
                {Gdata?.Atom_Name_List?.map((atom_present) => (
                  <div className=" mx-3">
=======
                {Gdata?.Atom_Name_List?.map((atom_present, idx) => (
                  <div className=" mx-3" key={idx}>
>>>>>>> codebase2
                    <input
                      type="checkbox"
                      name={atom_present}
                      id={atom_present}
                      className="h-4 w-4"
                      onChange={handleOnSelectMagneticAtoms}
                    />
                    <span className="text-xl mx-2">{atom_present}</span>
                  </div>
                ))}
              </div>
            </div>
            {/*----------- Buttons --------   */}
            <div className="flex flex-row justify-center gap-x-5 mt-10">
              <div className="">
<<<<<<< HEAD
                <button className="rounded bg-red-500 text-white p-2 w-20 hover:shadow-lg">
=======
                <button className="rounded bg-red-500 text-white p-2 w-20 hover:shadow-lg" 
                 onClick={handleOnMainPage}>
>>>>>>> codebase2
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
<<<<<<< HEAD
        </form>
=======
        </div>
>>>>>>> codebase2
      </div>
    </>
  );
};

export default Template1;
