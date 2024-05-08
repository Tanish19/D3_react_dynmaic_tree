import React, { useState, useEffect } from "react";
import TreeComponent from "./TreeComponent";

function App() {
  const [treeData, setTreeData] = useState(null);

  console.log(treeData);

  useEffect(() => {
    fetchInitialTreeData();
  }, []);

  useEffect(() => {
    fetchInitialTreeData();
    // Delete local storage on page reload
    localStorage.removeItem("treeData");
  }, []);
  
  const fetchInitialTreeData = () => {
    const storedData = localStorage.getItem("treeData");
    if (storedData) {
      setTreeData(JSON.parse(storedData));
    } else {
      fetch("http://localhost:8000/initial_tree_data")
        .then((response) => response.json())
        .then((data) => {
          setTreeData(data);
          localStorage.setItem("treeData", JSON.stringify(data));
        })
        .catch((error) =>
          console.error("Error fetching initial tree data:", error)
        );
    }
  };

  

  const handleNodeClick = (node) => {
    console.log("Clicked node:", node);
    if (!node.children) {
      fetchChildrenTreeData(node.data.id);
    }
    else {
      // Delete the children from the clicked node
      const updatedTreeData = deleteChildren(treeData, node.data.id);
      setTreeData(updatedTreeData);
      localStorage.setItem("treeData", JSON.stringify(updatedTreeData));
    }
    };
    const deleteChildren = (node, nodeId) => {
    if (node.id === nodeId) {
      return {
      ...node,
      children: [],
      };
    }
    if (node.children && node.children.length > 0) {
      return {
      ...node,
      children: node.children.map((child) =>
        deleteChildren(child, nodeId)
      ),
      };
    }
    return node;
  
  };

  const fetchChildrenTreeData = (nodeId) => {
    fetch(`http://localhost:8000/children_tree_data/${nodeId}`)
      .then((response) => response.json())
      .then((data) => {
        // Find the node in the treeData with the matching ID
        const updatedTreeData = updateChildren(treeData, nodeId, data.children);
        setTreeData(updatedTreeData);
        localStorage.setItem("treeData", JSON.stringify(updatedTreeData));
        console.log(updatedTreeData);
      })
      .catch((error) =>
        console.error("Error fetching children tree data:", error)
      );
  };

  const updateChildren = (node, nodeId, newChildren) => {
    if (node.id === nodeId) {
      return {
        ...node,
        children: [...node.children, ...newChildren],
      };
    }

    if (node.children && node.children.length > 0) {
      return {
        ...node,
        children: node.children.map((child) =>
          updateChildren(child, nodeId, newChildren)
        ),
      };
    }
    return node;
  };


  return (
    <div className="App">
      <TreeComponent treeData={treeData} onNodeClick={handleNodeClick} />
    </div>
  );
}

export default App;
