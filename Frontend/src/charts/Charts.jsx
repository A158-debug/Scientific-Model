import React from "react";
import { Line } from "react-chartjs-2";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: "top",
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        callback: function (value, index, values) {
          return value.toExponential();
        },
      },
    },
  },
};

const Charts = ({ ChartData, ChartRef }) => {
  let string_hkl_list = [];
  ChartData?.final_hkl_list.forEach(myFunction);
  function myFunction(item) {
    string_hkl_list.push([
      [
        `G(h,k,l):${item[0]},${item[1]},${item[2]}| ξG=${
          Math.round(item[3] * 100) / 100
        }| SF=${item[4]}`,
      ],
    ]);
  }

  let datasets = [];
  const labels = ChartData?.thicknessData[0];
  console.log(ChartData?.SF_ThicknessFunction[0]);
  for (let i = 0; i < ChartData?.final_hkl_list?.length; i++) {
    var randomColor = "#000000".replace(/0/g, function () {
      return (~~(Math.random() * 16)).toString(16);
    });

    datasets.push({
      label: string_hkl_list[i],
      data: ChartData?.SF_ThicknessFunction[i],
      backgroundColor: randomColor,
    });
  }
  const data = {
    labels,
    datasets: datasets,
  };

  return (
    <>
      <div className="border mt-10 bg-white my-10 md:m-10">
        <Line options={options} data={data} ref={ChartRef} />;
      </div>
    </>
  );
};

export default Charts;
