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
    },
  },
};

const Charts = ({ ChartData }) => {
  const labels = ChartData?.thicknessData[0];
  let datasets = [];

  ChartData?.SF_ThicknessFunction.forEach(myFunction);

  function myFunction(item) {
    var randomColor = "#000000".replace(/0/g, function () {
      return (~~(Math.random() * 16)).toString(16);
    });

    datasets.push({
      label: "Labels",
      data: item,
      backgroundColor: randomColor,
    });
  }
  const data = {
    labels,
    datasets: datasets,
  };

  return (
    <>
      <div className="border mt-10 bg-white m-10">
        <Line options={options} data={data} />;
      </div>
    </>
  );
};

export default Charts;
