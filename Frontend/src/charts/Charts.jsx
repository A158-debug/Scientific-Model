import React,{useEffect,useState} from "react";
import {Line} from "react-chartjs-2";
import faker from "faker";
import axios from "axios";
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



const Charts = () => {
  const [structureFactor, setStructureFactor] = useState([]);

  useEffect(() => {
    (async () => {
      const G_Optimzed_Values = await axios.get(
        `http://127.0.0.1:5000/g_optimized_values`
        );
        const G_Optimized_data = G_Optimzed_Values.data.Output_G_points_parameter;
        const GdataStructureFactor = G_Optimized_data.map((points)=> {return points[5]}).slice(0,100)
        setStructureFactor(GdataStructureFactor)
      })();
    }, []);
    const labels = [0,20,40,60,80,100];
    const data = {
      labels,
      datasets: [
        {
          label: 'A dataset',
          data: structureFactor,
          backgroundColor: 'rgba(255, 99, 132, 1)',
        },
      ],
    };

  return (
    <>
      <div className="border mt-10 bg-white m-10">
        {/* <Scatter options={options} data={data} />; */}
        <Line options={options} data={data} />;
      </div>
    </>
  );
};

export default Charts;
