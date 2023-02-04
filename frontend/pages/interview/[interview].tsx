import React, { useState, useEffect } from "react";
import axios from "axios";
import { interview } from "../../components/types";
import parse from "html-react-parser";
import { Box } from "@mui/system";
import { useRouter } from "next/router";
const Interview = () => {
  const [interview, setinterview] = useState<interview>();
  const router = useRouter();
  React.useEffect(() => {
    if (router.query.interview) {
      const pid = router.query.interview;
      axios
        .get(`api/interview/${pid}`)
        .then((res) => setinterview(res.data as interview))
        .catch((error) => console.log(error));
    }
  }, [router.isReady]);
  //for debuggin
  if (interview) {
    return (
      <div className="bg-black bg-cover bg-fixed overflow-auto bg-contain h-screen">
        <div className="flex flex-col items-center justify-center">
          <Box
            minHeight={500}
            maxHeight={10000}
            minWidth={1200}
            maxWidth={1200}
            sx={{
              backgroundColor: "black",
            }}
          >
            <div className="flex flex-col text-white justify-center items-center m-3">
              <div className="text-3xl">{interview?.name}</div>
              <div>{parse(interview?.body)}</div>
            </div>
          </Box>
        </div>
      </div>
    );
  } else {
    return (
      <div className=" bg-black bg-cover bg-fixed overflow-auto h-screen items-center" />
    );
  }
};

export default Interview;
