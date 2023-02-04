import React, { useState, useEffect } from "react";
import axios from "axios";
import { interview_lite } from "../components/types";
import { List } from "@mui/material";
import Link from "next/link";

const interview_map = (object: interview_lite, i: number) => {
  return (
    <Link passHref href={`interview/${object.id}`} key={i}>
      <div
        className="border-t-4"
        style={{ borderTopColor: "#7A8288" }}
      >
        <div className="flex flex-row w-full justify-center items-center">
          <div className="w-2/12">{object.id}</div>
          <div className="w-4/12">{object.name}</div>
          <div className="w-3/12">{object.last_modified}</div>
          <div className="w-3/12">{object.date}</div>
        </div>
      </div>
    </Link>
  );
};

function Interview() {
  const [interviews, setinterviews] = useState<Array<interview_lite>>();
  useEffect(() => {
    axios
      .get(`api/interview`)
      .then((res) =>
        setinterviews(
          res.data.sort((a: interview_lite, b: interview_lite) =>
            a.date < b.date ? 1 : b.date < a.date ? -1 : 0
          ) as Array<interview_lite>
        )
      )
      .catch((error) => console.log(error));
  }, []);
  return (
    <div className="bg-black bg-cover overflow-auto h-screen items-center">
      <div className="flex flex-col items-center w-full">
        <div className="flex flex-row items-center justify-center text-white w-4/5">
          <List
            sx={{ width: "100%", maxWidth: 1800, bgcolor: "#272B30" }}
            component="nav"
            aria-labelledby="nested-list-subheader"
          >
            <div className="flex flex-row w-full justify-center items-center bg-gray-400">
              <div className="w-2/12 ml-3">ID</div>
              <div className="w-4/12">Name</div>
              <div className="w-3/12">Last Modified</div>
              <div className="w-3/12">Date</div>
            </div>
            {interviews?.map((object, i) => interview_map(object, i))}
          </List>
        </div>
      </div>
    </div>
  );
}

export default Interview;
