import React from "react";
import {Line} from "react-chartjs-2";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

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

const Charts = ({ChartData}) => {

    const labels = ChartData?.thicknessData[0];
    let datasets=[]
  
    ChartData?.SF_ThicknessFunction.forEach(myFunction);

    // const setBg = () => {
    //   const randomColor = Math.floor(Math.random()*16777215).toString(16);
    //   return  "#" + randomColor;
    // }

    function myFunction(item){
      var randomColor = "#000000".replace(/0/g,function(){return (~~(Math.random()*16)).toString(16);});

      datasets.push({label:"Labels",data:item,backgroundColor:randomColor})
    }
    console.log(datasets)
    const data = {
      labels,
      // datasets: [
      //   {
      //     label: 'A dataset',
      //     data: ChartData?.SF_ThicknessFunction[0],
      //     backgroundColor: 'rgba(255, 99, 132, 1)',
      //   },
      // ],
      datasets:datasets
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
