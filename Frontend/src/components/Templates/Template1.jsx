import React, { useContext, useState } from "react";
import { stateContext } from "../context/ContextProvider";
import { useNavigate } from "react-router-dom";

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
      <div className="flex flex-col justify-center content-center">
        <div className="justify-center content-center glass-background">
          <form action="" className="">
            <div className="flex flex-col p-3">
              <div className="flex flex-col md:flex-row">
                <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                  <p className="text-lg text-black-400 basis-5/12">Title :</p>
                  <div className="w-full md:w-7/12"><input name="Material thickness :" defaultValue={Gdata.Inequivalent_Atoms} className="border rounded-md  px-2 py-1 w-10/12"/></div>       
                </div>
                <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                  <p className="text-lg text-black-400 basis-5/12">Lattice :</p>
                  <div className="w-full md:w-7/12"><input name="Material thickness :" defaultValue={Gdata.Inequivalent_Atoms} className="border rounded-md  px-2 py-1 w-10/12"/></div>       
                </div>      
              </div>
              <div className="flex flex-col md:flex-row">
                <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                  <p className="text-lg text-black-400 basis-5/12">Inequivalent Atoms:</p>
                  <div className="w-full md:w-7/12"><input name="Material thickness :" defaultValue={Gdata.Inequivalent_Atoms} className="border rounded-md  px-2 py-1 w-10/12"/></div>       
                </div>
                <div className="basis-1/2 mt-5 flex flex-col md:flex-row gap-3 content-center ">
                  <p className="text-lg text-black-400 basis-5/12">Accelerating voltage :</p>
                  <div className="w-full md:w-7/12"><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} onChange={(e)=>setOtherPara({...otherPara,accelerating_volt:e.target.value})} className="border rounded-md  px-2 py-1 w-10/12"/></div>       
                </div>      
              </div>
              <div className="mt-5">
                <p className="text-lg block mt-3">Lattice Parameters &nbsp; :</p>
                  <div className="flex flex-col md:flex-row mt-3 gap-3">
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                  </div>
                  <div className="flex flex-col md:flex-row mt-3 gap-3">
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                  </div>
              </div>
              <div className="mt-5">
                <p className="text-lg block mt-3">G Vector Range &nbsp; :</p>
                  <div className="flex flex-col md:flex-row mt-3 gap-3">
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                    <div className="basis-1/3">
                      <div className=""><input name="Material thickness :" value={Gdata.Inequivalent_Atoms} className="border rounded-md px-2 py-1 w-11/12"/></div>
                    </div>
                  </div>    
                  {/* <div className="flex flex-row my-1">
                    <FormInput value={Gdata.Lattice_Parameter[3]} />
                    <FormInput value={Gdata.Lattice_Parameter[4]} />
                    <FormInput value={Gdata.Lattice_Parameter[5]} />
                  </div> */}
              </div>

              {/*----------- Buttons --------   */}
              <div className="flex flex-row justify-between mt-5">
                <div className="">
                  <button className="rounded bg-red-500 text-white p-2 w-20 hover:shadow-lg">Exit</button>
                </div>
                <div className="">
                  <button className="rounded bg-blue-500 text-white p-2 w-20 hover:shadow-lg" onClick={handleOnTemplate2}>Next</button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </>
  );
};

export default Template1;
