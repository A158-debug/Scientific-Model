import React from "react";

const Table = ({ currentGdata }) => {
  return (
    <div>
      <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
        <table className="w-11/12 text-sm text-left text-gray-500 dark:text-gray-400 mx-auto h-5/6">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                h
              </th>
              <th scope="col" className="px-6 py-3">
                k
              </th>
              <th scope="col" className="px-6 py-3">
                l
              </th>
              <th scope="col" className="px-6 py-3">
                Vg(Volt)
              </th>
              <th scope="col" className="px-6 py-3">
                Phase
              </th>
              <th scope="col" className="px-6 py-3">
                SF
              </th>
              <th scope="col" className="px-6 py-3">
                Extinction_distance (nm)
              </th>
            </tr>
          </thead>
          <tbody>
            {currentGdata.map((table_row, index) => (
              <tr
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
                key={index}
              >
                {table_row.map((row_values, index) => (
                  <th
                    scope="row"
                    className="px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white font-normal text-[15px]"
                    key={index}
                  >
                    {row_values}
                  </th>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Table;
