import React, { useContext } from "react";
import FormInput from "../FormInput";
import temp1svg from "../images/temp1svg.svg";
import { stateContext } from "../context/ContextProvider";
import { Link } from "react-router-dom";

const Template2 = () => {
  const { Gdata } = useContext(stateContext);

  let Mult_List = ["4", "4"];
  let X_Coordinate_List = ["0.13500000","0.63500000","0.86500000","0.36500000","0.84200000","0.34200000","0.15800000","0.65800000"];
  let Y_Coordinate_List = ["0.13500000","0.36500000","0.63500000","0.86500000","0.84200000","0.65800000","0.34200000", "0.15800000"];
  let Z_Coordinate_List = ["0.13500000","0.86500000","0.36500000","0.63500000","0.84200000","0.15800000","0.65800000","0.34200000"];
  let Atom_Name_List = ["Fe", "Ge"];

  let molecule = {};
  let k = 0;
  for (let i = 0; i < Mult_List.length; i++) {
    let elements_atoms = [];
    for (let j = 0; j < parseInt(Mult_List[i]); j++) {
      let atom_position = {};
      atom_position["X_coordinate"] = parseFloat(X_Coordinate_List[k]);
      atom_position["Y_coordinate"] = parseFloat(Y_Coordinate_List[k]);
      atom_position["Z_coordinate"] = parseFloat(Z_Coordinate_List[k]);
      elements_atoms.push(atom_position);
      k++;
    }
    molecule[Atom_Name_List[i]] = elements_atoms
  }
  // console.log(atoms_coordinates);
  return (
    <>
      <div className="flex flex-col justify-center content-center">
        <div className="justify-center content-center glass-background2">
          <form action="">
          <div className="flex flex-col">
              <div className="">
              {
                Object.keys(molecule).map((atom_name)=> (
                  <div className="flex flex-row flex-wrap ">
                   <div className="mt-5">
                    <p className="text-2xl font-semibold">{atom_name}</p>
                    {molecule[atom_name].map((e)=>
                    <div className=" flex flex-row flex-wrap mt-3 gap-3">
                      <div className=" flex flex-row gap-3 content-center">
                        <p className="text-lg text-black-400 basis-3/12">X : </p>
                        <div className="w-full md:w-9/12"><input name="Material thickness :" defaultValue={e.X_coordinate} className="border rounded-md  px-2 py-1 w-10/12"/></div>     
                      </div> 
                      <div className=" flex flex-row gap-3 content-center">
                        <p className="text-lg text-black-400 basis-3/12">Y :</p>
                        <div className="w-full md:w-9/12"><input name="Material thickness :" defaultValue={e.Y_coordinate} className="border rounded-md  px-2 py-1 w-10/12"/></div>     
                      </div> 
                      <div className=" flex flex-row gap-3 content-center">
                        <p className="text-lg text-black-400 basis-3/12">Z :</p>
                        <div className="w-full md:w-9/12"><input name="Material thickness :" defaultValue={e.Z_coordinate} className="border rounded-md  px-2 py-1 w-10/12"/></div>     
                      </div> 
                    </div>
                    )}
                   </div>
                  </div>
                ))
              }
              {/*----------- Buttons --------   */}
             <div className="flex flex-row justify-between mt-5 w-1/2">
                <div className=""><button className="rounded bg-red-500 text-white p-2 w-20 hover:shadow-lg">Exit</button></div>
                <div className=""><button className="rounded bg-blue-500 text-white p-2 w-20 hover:shadow-lg">Next</button></div>
              </div>
            </div>
          </div>
          </form>
        </div>
      </div>
    </>
  );
};

export default Template2;
