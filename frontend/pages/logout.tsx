import axios from "axios";
import React, { useEffect } from "react";
import { useRouter } from "next/router";

function Logout() {
  const router = useRouter();
  const prevUrl = router.query.prevUrl;
  useEffect(() => {
    axios
      .post("/blacklist/", {
        refresh_token: localStorage.getItem("refresh_token"),
      })
      .then((res) => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
      })
      .catch((errors) => console.log(errors));
    if (prevUrl) {
      router.push(`/${prevUrl}`);
    } else {
      router.push("/");
    }
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
  }, []);
  return <div>Logging out...</div>;
}

export default Logout;
