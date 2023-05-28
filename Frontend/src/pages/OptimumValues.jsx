<<<<<<< HEAD
import React, { useState, useEffect,useContext } from "react";
=======
import React, { useState, useEffect, useContext,useRef } from "react";
>>>>>>> codebase2
import { stateContext } from "../context/ContextProvider";
import axios from "axios";
import Table from "../components/Table";
import ReactPaginate from "react-paginate";
import Charts from "../charts/Charts";
<<<<<<< HEAD
=======
import { useNavigate } from "react-router-dom";
>>>>>>> codebase2

const Template3 = () => {
  const postsPerPage = 7;
  const [loading, setLoading] = useState(false);
<<<<<<< HEAD
  const [currentPage, setCurrentPage] = useState(0);
  const [thickness, setThickness] = useState("")
  const [gPoints, setGPoints] = useState("")


  const [G_Optimized_data, setG_Optimized_data] = useState([]);
  const [Output_Optimized_G_Parameters,setOutput_Optimized_G_Parameters] = useState([]);
  const [ChartData,SetChartData] = useState({thicknessData:[], SF_ThicknessFunction:[]});


  const { magneticAtoms,Gdata } = useContext(stateContext);
=======
  const [chartLoading, setChartLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(0);
  const [thickness, setThickness] = useState("");
  const [gPoints, setGPoints] = useState("");

  const [G_Optimized_data, setG_Optimized_data] = useState([]);
  const [Output_Optimized_G_Parameters, setOutput_Optimized_G_Parameters] =
    useState([]);
  const [ChartData, SetChartData] = useState({
    thicknessData: [],
    SF_ThicknessFunction: [],
    final_hkl_list:[]
  });

  const { magneticAtoms, Gdata, otherPara } = useContext(stateContext);
>>>>>>> codebase2

  useEffect(() => {
    (async () => {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
<<<<<<< HEAD
        magnetic_atom_dict: JSON.stringify({ magneticAtoms }),
      };

      const G_Optimzed_Values = await axios.post(
        `http://127.0.0.1:5000/g_optimized_values`,requestOptions);
        setG_Optimized_data(G_Optimzed_Values?.data?.Output_G_points_parameter);
        setOutput_Optimized_G_Parameters(G_Optimzed_Values?.data?.Output_Optimized_G_Parameters);
        setLoading(false);
      })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);
    
=======
        magnetic_atom_dict: JSON.stringify({ magneticAtoms, otherPara }),
      };

      const G_Optimzed_Values = await axios.post(
        `http://127.0.0.1:5000/g_optimized_values`,
        requestOptions
      );
      setG_Optimized_data(G_Optimzed_Values?.data?.Output_G_points_parameter);
      setOutput_Optimized_G_Parameters(
        G_Optimzed_Values?.data?.Output_Optimized_G_Parameters
      );
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

>>>>>>> codebase2
  const pageCount = Math.ceil(G_Optimized_data.length / postsPerPage);
  const paginate = (pageNumber) => {
    const newOffset =
      (pageNumber.selected * postsPerPage) % G_Optimized_data.length;
    setCurrentPage(newOffset);
  };

<<<<<<< HEAD
  const currentGdata = G_Optimized_data.slice( currentPage, currentPage + postsPerPage
=======
  const currentGdata = G_Optimized_data.slice(
    currentPage,
    currentPage + postsPerPage
>>>>>>> codebase2
  );

  const handleOnClickGraph = async (e) => {
    e.preventDefault();
<<<<<<< HEAD
    const cnm = Gdata?.Lattice_Parameter[2]
    // const cnm = 2
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      thickness_and_gpoints: JSON.stringify({cnm, thickness,gPoints,G_Optimized_data,}),
    };
    const G_Data_Chart_Values = await axios.post(`http://127.0.0.1:5000/thickness_gpoints_values`,requestOptions);
    if(G_Data_Chart_Values){
      SetChartData({thicknessData:G_Data_Chart_Values?.data?.final_2d_list_x,SF_ThicknessFunction:G_Data_Chart_Values?.data?.final_2d_list_y
      })
    }
  };

=======
    const cnm = Gdata?.Lattice_Parameter[2];
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      thickness_and_gpoints: JSON.stringify({
        cnm,
        thickness,
        gPoints,
        G_Optimized_data,
      }),
    };
    const G_Data_Chart_Values = await axios.post(
      `http://127.0.0.1:5000/thickness_gpoints_values`,
      requestOptions
    );
    if (G_Data_Chart_Values) {

      setChartLoading(true)
      SetChartData({
        thicknessData: G_Data_Chart_Values?.data?.final_2d_list_x,
        SF_ThicknessFunction: G_Data_Chart_Values?.data?.final_2d_list_y,
        final_hkl_list: G_Data_Chart_Values?.data?.final_parameter_list,

      });
      setLoading(true);
    }
  };
  const navigate = useNavigate()
  const ChartRef = useRef(null)
  const handleOnChartDownload = async(e)=>{
      e.preventDefault()
      const link = document.createElement('a');
      link.download = "chart.png";
      link.href = ChartRef.current.toBase64Image();
      link.click()
      navigate('/')
  }
>>>>>>> codebase2
  return (
    <>
      <div className="flex flex-col justify-center content-center pb-10">
        <div className="justify-center content-center glass-background">
          <form action="">
            <div className="flex flex-col p-3 md:flex-row">
              <div className="md:basis-6/12 basis-12">
                <h1 className="text-2xl font-semibold">
                  Optimized G-Value and Extinction Distance
                </h1>
                <div className="mt-5 text-lg text-black-400  px-10">
<<<<<<< HEAD
                  <p className="mt-2">Optimum G(h,k,l) : ({Output_Optimized_G_Parameters[0]},{Output_Optimized_G_Parameters[1]},{Output_Optimized_G_Parameters[2]}) </p>
                  <p className="mt-2">Max SF : {Output_Optimized_G_Parameters[3]?.toFixed(2)}</p>
                  <p className="mt-2">Extinction Distance :{Output_Optimized_G_Parameters[4]?.toFixed(2)} </p>
=======
                  <p className="mt-2">
                    Optimum G(h,k,l) : ({Output_Optimized_G_Parameters[0]},
                    {Output_Optimized_G_Parameters[1]},
                    {Output_Optimized_G_Parameters[2]}){" "}
                  </p>
                  <p className="mt-2">
                    Max SF : {Output_Optimized_G_Parameters[3]?.toFixed(2)}
                  </p>
                  <p className="mt-2">
                    Extinction Distance :
                    {Output_Optimized_G_Parameters[4]?.toFixed(2)}{" "}
                  </p>
>>>>>>> codebase2
                </div>
              </div>
              <div className="md:basis-6/12 basis-12">
                <h1 className="text-2xl font-semibold ">To Visvualize Plot</h1>
                <div className="flex flex-col md:flex-row gap-2 mt-5 content-center ">
                  <p className="text-lg text-black-400 basis-6/12">
                    Give a thickness range to plot :
                  </p>
                  <div className="w-full md:w-6/12">
                    <input
                      name="Material thickness :"
                      className="border rounded-md  px-2 py-1 w-10/12 text-black focus:outline-none"
                      placeholder="(nm)"
                      value={thickness}
<<<<<<< HEAD
                      onChange={(e)=>setThickness(e.target.value)}
=======
                      onChange={(e) => setThickness(e.target.value)}
>>>>>>> codebase2
                    />
                  </div>
                </div>
                <div className="flex flex-col md:flex-row gap-2 mt-5 content-center ">
                  <p className="text-lg text-black-400 basis-6/12">
                    Give number of points to plot :
                  </p>
                  <div className="w-full md:w-6/12">
                    <input
                      name="Material thickness :"
                      className="border rounded-md  px-2 py-1 w-10/12 text-black focus:outline-none"
<<<<<<< HEAD
                      value ={gPoints}
                      onChange={(e)=>setGPoints(e.target.value)}
=======
                      value={gPoints}
                      onChange={(e) => setGPoints(e.target.value)}
>>>>>>> codebase2
                    />
                  </div>
                </div>
                <div className="mt-5">
                  <button
                    className="rounded bg-blue-500 text-white p-2 px-5 hover:shadow-lg"
                    onClick={handleOnClickGraph}
                  >
                    Show Plot
                  </button>
<<<<<<< HEAD
=======
                 {
                  chartLoading && (<button
                    className="rounded bg-blue-500 text-white p-2 px-5 hover:shadow-lg ml-5"
                    onClick={handleOnChartDownload}
                  >
                    Download Plot
                  </button>)
                 }
>>>>>>> codebase2
                </div>
              </div>
            </div>
          </form>
        </div>
<<<<<<< HEAD
=======
        {
          loading &&  <Charts ChartData={ChartData} ChartRef={ChartRef} />
        }
>>>>>>> codebase2
        <Table currentGdata={currentGdata} loading={loading} />
        <ReactPaginate
          previousLabel={"< previous"}
          nextLabel={"next >"}
          onPageChange={paginate}
          pageCount={pageCount}
          breakLabel="..."
          pageRangeDisplayed={3}
          renderOnZeroPageCount={null}
<<<<<<< HEAD
          pageClassName={"px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"}
          previousClassName={"px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"}
          nextClassName={"px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"}
          className={"inline-flex -space-x-px my-5 self-center"}
          activeLinkClassName={"bg-red-700 text-white px-4 py-2"}
        />
        <Charts ChartData={ChartData}/>
=======
          pageClassName={
            "px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
          }
          previousClassName={
            "px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
          }
          nextClassName={
            "px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
          }
          className={"inline-flex -space-x-px my-5 self-center"}
          activeLinkClassName={"bg-red-700 text-white px-4 py-2"}
        />
>>>>>>> codebase2
      </div>
    </>
  );
};

export default Template3;
