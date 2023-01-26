import React from 'react'

const Template3 = () => {
  return (
    <>
    <div className="flex flex-col justify-center content-center">
      <div className="justify-center content-center glass-background">
        <form action="">
            <div className="flex flex-col p-3 md:flex-row">
              <div className="md:basis-6/12 basis-12">
                <h1 className="text-2xl font-semibold text-cyan-800">Optimized G-Value and Extinction Distance</h1>
                <div className="mt-5 text-lg text-black-400">
                    <p className="mt-2">Optimum G(h,k,l) : (4,0,0)</p>
                    <p className="mt-2">Max SF :  3.87</p>
                    <p className="mt-2">Extinction Distance :143.69</p>
                </div>
              </div>
              <div className="md:basis-6/12 basis-12">
                <h1 className="text-2xl font-semibold text-cyan-800">To Visvualize Plot</h1>
                <div className="flex flex-col md:flex-row gap-2 mt-5 content-center ">
                  <p className="text-lg text-black-400 basis-6/12">Give a thickness range to plot :</p>
                  <div className="w-full md:w-6/12"><input name="Material thickness :" className="border rounded-md  px-2 py-1 w-10/12" placeholder='(nm)'/></div>       
                </div>
                <div className="flex flex-col md:flex-row gap-2 mt-5 content-center ">
                  <p className="text-lg text-black-400 basis-6/12">Give number of points to plot :</p>
                  <div className="w-full md:w-6/12"><input name="Material thickness :" className="border rounded-md  px-2 py-1 w-10/12"/></div>       
                </div>
                <div className="mt-5"><button className="rounded bg-blue-500 text-white p-2 px-5 hover:shadow-lg">Show Plot</button></div>
              </div> 
            </div>
        </form>
      </div>
    </div>
    </>
  )
}

export default Template3