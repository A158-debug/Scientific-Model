import React, { useState, useEffect, useContext, useRef } from "react";
import { stateContext } from "../context/ContextProvider";
import axios from "axios";
import Table from "../components/Table";
import ReactPaginate from "react-paginate";
import Charts from "../charts/Charts";
import { useNavigate } from "react-router-dom";

const Template3 = () => {
  const postsPerPage = 7;
  const [loading, setLoading] = useState(false);
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
    final_hkl_list: [],
  });

  const { magneticAtoms, Gdata, otherPara } = useContext(stateContext);

  useEffect(() => {
    (async () => {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
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

  const pageCount = Math.ceil(G_Optimized_data.length / postsPerPage);
  const paginate = (pageNumber) => {
    const newOffset =
      (pageNumber.selected * postsPerPage) % G_Optimized_data.length;
    setCurrentPage(newOffset);
  };

  const currentGdata = G_Optimized_data.slice(
    currentPage,
    currentPage + postsPerPage
  );

  const handleOnClickGraph = async (e) => {
    e.preventDefault();
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
      setChartLoading(true);
      SetChartData({
        thicknessData: G_Data_Chart_Values?.data?.final_2d_list_x,
        SF_ThicknessFunction: G_Data_Chart_Values?.data?.final_2d_list_y,
        final_hkl_list: G_Data_Chart_Values?.data?.final_parameter_list,
      });
      setLoading(true);
    }
  };
  const navigate = useNavigate();
  const ChartRef = useRef(null);
  const handleOnChartDownload = async (e) => {
    e.preventDefault();
    const link = document.createElement("a");
    link.download = "chart.png";
    link.href = ChartRef.current.toBase64Image();
    link.click();
    navigate("/");
  };
  return (
    <>
      <div className="flex flex-col justify-center content-center p-5">
          <div className="flex flex-col md:flex-row my-5">
            <div className="md:basis-6/12 basis-12">
              <h1 className="text-3xl font-[400]">Optimized Parameters</h1>
              <div className="mt-5 text-lg text-black-400  ">
                <li className="mt-2">
                  Optimum G(h,k,l) : ({Output_Optimized_G_Parameters[0]},
                  {Output_Optimized_G_Parameters[1]},
                  {Output_Optimized_G_Parameters[2]}){" "}
                </li>
                <li className="mt-2">
                  Max SF : {Output_Optimized_G_Parameters[3]?.toFixed(2)}
                </li>
                <li className="mt-2">
                  Extinction Distance :
                  {Output_Optimized_G_Parameters[4]?.toFixed(2)}{" "}
                </li>
              </div>
            </div>
            <div className="md:basis-6/12 basis-12 mt-5 md:mt-0">
              <h1 className="text-3xl font-[400]">To Visvualize Plot</h1>
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
                    onChange={(e) => setThickness(e.target.value)}
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
                    value={gPoints}
                    onChange={(e) => setGPoints(e.target.value)}
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
                {chartLoading && (
                  <button
                    className="rounded bg-blue-500 text-white p-2 px-5 hover:shadow-lg ml-5"
                    onClick={handleOnChartDownload}
                  >
                    Download Plot
                  </button>
                )}
              </div>
            </div>
          </div>
        {loading && <Charts ChartData={ChartData} ChartRef={ChartRef} />}
        <Table currentGdata={currentGdata} loading={loading} />
        <ReactPaginate
          previousLabel={"< previous"}
          nextLabel={"next >"}
          onPageChange={paginate}
          pageCount={pageCount}
          breakLabel="..."
          pageRangeDisplayed={3}
          renderOnZeroPageCount={null}
          pageClassName={
            "px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
          }
          previousClassName={
            "px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
          }
          nextClassName={
            "px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
          }
          className={"flex flex-wrap justify-center items-center mx-auto my-5"}
          activeLinkClassName={"bg-red-700 text-white px-4 py-2"}
        />
      </div>
    </>
  );
};

export default Template3;
