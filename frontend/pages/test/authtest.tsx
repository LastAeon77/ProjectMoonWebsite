import React, { useEffect, useState } from "react";
import axios from "axios";
const Authtest = () => {
  const [data, setdata] = useState<string | null>();
  useEffect(() => {
    axios
      .get("api/lor/cardtest", {
        headers: {
          Authorization: `JWT ${localStorage.getItem("access_token")}`,
          "Content-Type": "application/json",
          accept: "application/json",
        },
      })
      .then((res) => {
        setdata("You are logged in")
        console.log(res)
      })
      .catch((error) => {
        
        setdata("You are not logged in, Please login")
             });
  }, []);
  return <div>{data}</div>;
};

export default Authtest;
