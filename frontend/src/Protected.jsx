// Accessing protected content

import { useEffect, useState } from "react";
import axios from "axios";

function Protected() {
  const [data, setData] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await axios.get("<MY_AWS_LOAD_BALANCER_URL>/protected", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setData(response.data.message);
      } catch (err) {
        setData("Error fetching protected data");
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Protected Data</h2>
      <p>{data}</p>
    </div>
  );
}

export default Protected;


// again, replace your aws load balancer URL with <MY_AWS_LOAD_BALANCER_URL>
