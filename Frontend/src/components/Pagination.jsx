import React from "react";
const Pagination = ({ postsPerPage, totalPosts, paginate }) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(totalPosts / postsPerPage); i++) {
    pageNumbers.push(i);
  }

  return (
    <ul className="">
      {pageNumbers.map((number) => (
        <li key={number} onClick={() => paginate(number)}>
          {number}
        </li>
      ))}
    </ul>
  );
};

export default Pagination;
