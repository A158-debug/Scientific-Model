import React, { useContext } from "react";
import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";

const Template2 = () => {
  const { Gdata } = useContext(stateContext);
  const navigate = useNavigate();

  const onHandleClickOptimumValues = ()=>{
    navigate('/optimumvalues')
  }

  let molecule = {};
  let k = 0;
  for (let i = 0; i < Gdata.Mult_list.length; i++) {
    let elements_atoms = [];
    for (let j = 0; j < Gdata.Mult_list[i]; j++) {
      let atom_position = {};
      atom_position["X_coordinate"] = parseFloat(Gdata.X_Coordinate_List[k]);
      atom_position["Y_coordinate"] = parseFloat(Gdata.Y_Coordinate_List[k]);
      atom_position["Z_coordinate"] = parseFloat(Gdata.Z_Coordinate_List[k]);
      elements_atoms.push(atom_position);
      k++;
    }
    molecule[Gdata.Atom_Name_List[i]] = elements_atoms;
  }
  // console.log(atoms_coordinates);

  return (
    <>
      <div className="flex flex-col justify-center content-center">
        <form className="flex justify-center ">
          <div className="flex flex-col w-4/5 p-3">
              {Object.keys(molecule).map((atom_name,idx) => (
                <div className="flex flex-row flex-wrap"key={idx}>
                  <div className="mt-5">
                    <p className="text-2xl font-semibold">{atom_name}</p>
                    {molecule[atom_name].map((e,idx) => (
                      <div className="flex flex-row flex-wrap mt-3 gap-3 border py-4 px-3 border-violet-300 rounded-sm" key={idx}>
                        <div className=" flex flex-row gap-3 content-center">
                          <p className="text-lg text-black-400 basis-3/12">
                            X :{" "}
                          </p>
                          <div className="w-full md:w-9/12">
                            <input
                              name="Material thickness :"
                              defaultValue={e.X_coordinate}
                              className="border rounded-md  px-2 py-1 w-10/12 text-black focus:outline-none  text-lg"
                            />
                          </div>
                        </div>
                        <div className=" flex flex-row gap-3 content-center">
                          <p className="text-lg text-black-400 basis-3/12">
                            Y :
                          </p>
                          <div className="w-full md:w-9/12">
                            <input
                              name="Material thickness :"
                              defaultValue={e.Y_coordinate}
                              className="border rounded-md  px-2 py-1 w-10/12 text-black focus:outline-none  text-lg"
                            />
                          </div>
                        </div>
                        <div className=" flex flex-row gap-3 content-center">
                          <p className="text-lg text-black-400 basis-3/12">
                            Z :
                          </p>
                          <div className="w-full md:w-9/12">
                            <input
                              name="Material thickness :"
                              defaultValue={e.Z_coordinate}
                              className="border rounded-md  px-2 py-1 w-10/12 text-black focus:outline-none  text-lg"
                            />
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
 
              {/*----------- Buttons --------   */}
              <div className="flex flex-row justify-center gap-x-5 mt-10">
                <div className="">
                  <button className="rounded bg-red-500 text-white p-2 w-20 hover:shadow-lg">
                    Exit
                  </button>
                </div>
                <div className="">
                  <button className="rounded bg-blue-500 text-white p-2 w-20 hover:shadow-lg" onClick={onHandleClickOptimumValues}>
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

export default Template2;
