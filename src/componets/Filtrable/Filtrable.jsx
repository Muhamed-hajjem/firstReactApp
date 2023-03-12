import React from "react";
import ProductRow from "../ProductRow/ProductRow";
import ProductTable from "../productTable/ProductTable";

import './Filtrable.css';

function Filtrable  ()  {
  return(
    <div className="filtrable" >
        <ProductTable/>
        <ProductRow/>
    </div>
  );

}

export default Filtrable; 