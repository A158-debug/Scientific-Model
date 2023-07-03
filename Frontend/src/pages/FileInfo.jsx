import React, { useContext, useState } from "react";
import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";

const Template1 = () => {
  const navigate = useNavigate();
  const [showAlert, setShowAlert] = useState(false);
  const { Gdata, magneticAtoms, setmagneticAtoms, otherPara, setOtherPara } =
    useContext(stateContext);

  const handleOnTemplate2 = async () => {
    if (
      otherPara?.h_para === "" ||
      otherPara?.k_para === "" ||
      otherPara?.l_para === ""
    ) {
      setShowAlert(true);
      setTimeout(() => {
        setShowAlert(false);
      }, 3000);
      return;
    } else navigate("/atomicposition");
  };

  const handleOnMainPage = async () => {
    navigate("/");
  };

  const handleOnSelectMagneticAtoms = (e) => {
    setmagneticAtoms({ ...magneticAtoms, [e.target.name]: e.target.checked });
  };

  const handleChangeAlert = () => {
    setShowAlert(false);
  };

  return (
    <>
      <div className="flex flex-col justify-center content-center">
        {showAlert && (
          <div className="my-4 p-4 bg-red-500 text-white rounded w-10/12 flex justify-between items-center mx-auto">
            <span className="text-lg">Please Enter all the values</span>
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
        <div className="flex justify-center">
          <div className="flex flex-col p-3 w-4/5 ">
            {/*----------- Title & Lattice --------   */}
            <div className="flex flex-col md:flex-row">
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">Title :</p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
                    defaultValue={Gdata?.Material_Name}
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                  />
                </div>
              </div>
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">Lattice :</p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
                    defaultValue={Gdata?.Lattice_Type}
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
                    defaultValue={Gdata?.Inequivalent_Atoms}
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
                    type="number"
                    onChange={(e) =>
                      setOtherPara({
                        ...otherPara,
                        accelerating_volt: e.target.value,
                      })
                    }
                    value={otherPara.accelerating_volt}
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                    placeholder="Enter voltage value"
                  />
                </div>
              </div>
            </div>

            {/*----------- Material thickness --------   */}
            <div className="flex flex-col md:flex-row">
              <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                <p className="text-lg text-black-400 basis-5/12">Thickness :</p>
                <div className="w-full md:w-7/12">
                  <input
                    name="Material thickness :"
                    className="border rounded-md  px-2 py-1 w-10/12  text-black focus:outline-none  text-lg"
                    value={otherPara?.Material_Thickness}
                    placeholder="In (nm) default is 5nm"
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

            {/*----------- Lattice Parameters --------   */}
            <p className="text-lg block mt-5">Lattice Parameters &nbsp; :</p>
            <div className="mt-2">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {Gdata?.Lattice_Parameter?.map((item, index) => (
                  <div className="" key={index}>
                    <input
                      name={item}
                      defaultValue={item}
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                    />
                  </div>
                ))}
              </div>
            </div>

            {/*----------- G Vector Range --------   */}
            <p className="text-lg block mt-5">G Vector Range &nbsp; :</p>
            <div className="mt-2">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="">
                  <div className="">
                    <input
                      name="h_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg pl"
                      placeholder="Enter h value default is 4"
                      value={otherPara?.h_para}
                      type="number"
                      required
                      onChange={(e) =>
                        setOtherPara({
                          ...otherPara,
                          h_para: e.target.value,
                        })
                      }
                    />
                  </div>
                </div>
                <div className="">
                  <div className="">
                    <input
                      name="k_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                      placeholder="Enter k value default is 4"
                      value={otherPara?.k_para}
                      type="number"
                      required
                      onChange={(e) =>
                        setOtherPara({
                          ...otherPara,
                          k_para: e.target.value,
                        })
                      }
                    />
                  </div>
                </div>
                <div className="">
                  <div className="">
                    <input
                      name="l_value"
                      className="border rounded-md px-2 py-1 w-11/12 text-black focus:outline-none  text-lg"
                      placeholder="Enter l value default is 4"
                      value={otherPara?.l_para}
                      type="number"
                      required
                      onChange={(e) =>
                        setOtherPara({
                          ...otherPara,
                          l_para: e.target.value,
                        })
                      }
                    />
                  </div>
                </div>
              </div>
            </div>

            {/*----------- Magnetic Atoms --------   */}
            <div className="mt-5">
              <p className="text-lg block mt-3">
                Select the magnetic atoms &nbsp; :
              </p>
              <div className=" my-2 p-2 flex  flex-wrap">
                {Gdata?.Atom_Name_List?.map((atom_present, idx) => (
                  <div className=" mx-3" key={idx}>
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
                <button
                  className="rounded bg-red-500 text-white p-2 w-20 hover:shadow-lg"
                  onClick={handleOnMainPage}
                >
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
        </div>
      </div>
    </>
  );
};

export default Template1;
