import React from "react";

const Template1 = () => {
  return (
    <>
      <div class="container w-screen">
        <div class="container bg-red-200 flex flex-row">
          <div class="basis-1/2">
            <label class="block my-4">
              <span class="text-lg font-normal text-slate-700 mx-5 w-6/12 ">
                Title :
              </span>
              <input
                type="text"
                // value="tbone"
                class="px-3 py-2  w-6/12 ml-28 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
              />
            </label>
            <label class="block my-4">
              <span class="text-lg font-normal text-slate-700 mx-5">
                Inequivalent atoms :
              </span>
              <input
                type="text"
                // value="tbone"
                class="px-3 py-2 w-6/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
              />
            </label>
            <label class="block my-4">
              <span class="text-lg font-normal text-slate-700 mx-5">
                Material thickness :
              </span>
              <input
                type="text"
                // value="tbone"
                class="px-3 py-2 w-6/12 ml-2 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
              />
             
            </label>
          </div>
          <div class="basis-1/2">
          <label class="block my-4">
            <span class="text-lg font-normal text-slate-700 mx-5 w-6/12 ">
              Lattice &nbsp; :
            </span>
            <input
              type="text"
              // value="tbone"
              class="px-3 py-2 w-6/12 ml-24 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
            />
          </label>
          <label class="block my-4">
            <span class="text-lg font-normal text-slate-700 mx-5">
              Accelerating voltage :
            </span>
            <input
              type="text"
              // value="tbone"
              class="px-3 py-2 w-6/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
            />
          </label>
          <label class="block my-4">
          <input type="checkbox" class=" checked:bg-blue-500 w-4 h-4 p-5 mt-3" />
            <span class="text-lg font-normal text-slate-700 mx-5">
              Not known 
            </span>
           
          </label>
          </div>
        </div>

        <div class="container bg-red-200"> 
          <label class="block  w-9/12">
            <span class="text-lg block font-normal text-slate-700 mx-5">
              Lattice Parameters &nbsp; :
            </span>
            <div class="flex flex-row mt-5 pl-5">
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
            </div>
            <div class="flex flex-row mt-5 pl-5">
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
            </div>
          </label> 
          <label class="block  pb-4 w-9/12">
            <span class="text-lg block font-normal text-slate-700 mx-5">
              Lattice Parameters &nbsp; :
            </span>
            <div class="flex flex-row mt-5 pl-5">
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
              <div class="basis-1/3 ">
                {" "}
                <input
                  type="text"
                  // value="tbone"
                  class="py-2 w-10/12 bg-white border border-slate-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500
      disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                />
              </div>
            </div>
          
          </label> 
     
        </div>
        <div class="container bg-red-200 flex flex-row justify-around" >
          <div class="">
          <button class="rounded bg-red-400 text-white p-2 w-20">Exit</button>
          
          </div>
          <div class="">
          <button class="rounded bg-blue-400 text-white p-2 w-20">Next</button>
          </div>
        </div>
      </div>
    </>
  );
};

export default Template1;
