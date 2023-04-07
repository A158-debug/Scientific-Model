import React, { useState, useEffect } from "react";
import axios from "axios";
import Table from "../components/Table";
import ReactPaginate from "react-paginate";
import Charts from "../charts/Charts";

const Template3 = () => {
  const postsPerPage = 7;
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(0);
  const [G_Optimized_data, setG_Optimized_data] = useState([]);

  
  useEffect(() => {
    (async () => {
      const G_Optimzed_Values = await axios.get(
        `http://127.0.0.1:5000/g_optimized_values`
        );
        setG_Optimized_data(G_Optimzed_Values.data.Output_G_points_parameter);
        setLoading(false);
      })();
    }, []);
    
  const pageCount = Math.ceil(G_Optimized_data.length / postsPerPage);
  const paginate = (pageNumber) => {
    const newOffset =
      (pageNumber.selected * postsPerPage) % G_Optimized_data.length;
    setCurrentPage(newOffset);
  };

  const currentGdata = G_Optimized_data.slice( currentPage, currentPage + postsPerPage
  );

  const handleOnClickGraph = async (e) => {
    e.preventDefault();
    // Output format [[h, k, l, Vg(Volt), Phase, Extinction_distance].....] ,multiple array
  };

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
                <div className="mt-5 text-lg text-black-400">
                  <p className="mt-2">Optimum G(h,k,l) : (4,0,0)</p>
                  <p className="mt-2">Max SF : 3.87</p>
                  <p className="mt-2">Extinction Distance :143.69</p>
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
                      className="border rounded-md  px-2 py-1 w-10/12"
                      placeholder="(nm)"
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
                      className="border rounded-md  px-2 py-1 w-10/12"
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
                </div>
              </div>
            </div>
          </form>
        </div>
        <Table currentGdata={currentGdata} loading={loading} />
        <ReactPaginate
          previousLabel={"< previous"}
          nextLabel={"next >"}
          onPageChange={paginate}
          pageCount={pageCount}
          breakLabel="..."
          pageRangeDisplayed={3}
          renderOnZeroPageCount={null}
          pageClassName={"px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"}
          previousClassName={"px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"}
          nextClassName={"px-4 py-2 leading-tight text-gray-500  border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"}
          className={"inline-flex -space-x-px my-5 self-center"}
          activeLinkClassName={"bg-red-700 text-white px-4 py-2"}
        />
        <Charts/>
      </div>
    </>
  );
};

export default Template3;
