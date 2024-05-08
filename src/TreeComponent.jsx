import React from "react";
import Tree from "react-d3-tree";

const TreeComponent = ({ treeData, onNodeClick }) => {


  return (
    <div id="treeWrapper" style={{ width: "100%", height: "100vh" }}>
      {treeData ? (
        <Tree
          data={treeData}
          orientation="vertical"
          translate={{ x: 300, y: 50 }}
          onNodeClick={onNodeClick}
        />
      ) : (
        <div>Loading tree data...</div>
      )}
    </div>
  );
};

export default TreeComponent;
