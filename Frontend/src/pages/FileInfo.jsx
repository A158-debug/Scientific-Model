import React, { useContext, useState } from "react";
import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";

const Template1 = () => {
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

  };

  const handleOnSelectMagneticAtoms = (e) => {
    setmagneticAtoms({ ...magneticAtoms, [e.target.name]: e.target.checked });
  };

  return (
    <>
      <div className="flex flex-col justify-center content-center">
        <form action="" className="flex justify-center">
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
                    onChange={(e) =>
                      setOtherPara({
                        ...otherPara,
                        accelerating_volt: e.target.value,
                      })
                    }
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                    placeholder="Enter voltage value"
                  />
                </div>
              </div>
            </div>

            {/*----------- Lattice Parameters --------   */}
            <div className="mt-5">
              <p className="text-lg block mt-3">Lattice Parameters &nbsp; :</p>
              <div className="flex flex-col md:flex-row mt-3 gap-3">
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="Material thickness :"
                      defaultValue={Gdata.Lattice_Parameter[0]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="Material thickness :"
                      defaultValue={Gdata.Lattice_Parameter[1]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="Material thickness :"
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
                      name="Material thickness :"
                      defaultValue={Gdata.Lattice_Parameter[3]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="Material thickness :"
                      defaultValue={Gdata.Lattice_Parameter[4]}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="Material thickness :"
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
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="k_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                      placeholder="Enter k value"
                    />
                  </div>
                </div>
                <div className="basis-1/3">
                  <div className="">
                    <input
                      name="l_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                      placeholder="Enter l value"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div className="mt-5">
              <p className="text-lg block mt-3">
                Select the magnetic atoms &nbsp; :
              </p>
              <div className=" my-2 p-2 flex  flex-wrap">
                {Gdata?.Atom_Name_List?.map((atom_present) => (
                  <div className=" mx-3">
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
    </>
  );
};

export default Template1;
