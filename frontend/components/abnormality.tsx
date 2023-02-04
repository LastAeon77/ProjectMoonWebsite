import { Box } from "@mui/system";
import { imgur_or_static } from "./misc";
import Link from "next/link";
import { abno_card } from "./types";

export const choose_color = (emotiontype: string) => {
  switch (emotiontype) {
    case "BD":
      return "red";
    case "AW":
      return "green";
  }
};
export const one_abno = (data: abno_card) => {
  return (
    <Box
      key={data.id}
      sx={{
        width: 400,
        height: 260,
        backgroundColor: "black",
        borderRadius: "1em",
        "&:hover": {
          backgroundColor: "black",
          opacity: [0.9, 0.8, 0.7],
        },
      }}
      style={{
        backgroundColor: "black",
        margin: "6px",
        boxShadow: `1px -20px 60px -20px ${choose_color(
          data?.emotion_type
        )} inset, 0px 0px 5px -1px ${choose_color(data?.emotion_type)} inset`,
      }}
    >
      <Link passHref href={`abno/${data?.id}`}>
        <div className="flex flex-col items-center text-sm">
          <div className="text-white text-2xl">{data?.name}</div>
          <div className="flex flex-row items-left text-white">
            <div className="flex flex-col items-center justify-center w-1/2">
              <div className="ml-6">
                <img
                  src={data.ImgPath && imgur_or_static(data.ImgPath)}
                  alt="Image"
                  width={400}
                  height={400}
                />
              </div>
              <div className="text-2xl">Emotion {data?.emotion_level}</div>
            </div>
            <div className="w-1/2">{data?.effects}</div>
          </div>
        </div>
      </Link>
    </Box>
  );
};
