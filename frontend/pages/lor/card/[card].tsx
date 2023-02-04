import React from "react";
import { useRouter } from "next/router";
import { useState } from "react";
import axios from "axios";
import { game_card } from "../../../components/card";
import { Box } from "@mui/system";
import { imgur_or_static } from "../../../components/misc";
import {
  Dice_Image,
  destroy_NULL,
  color_assign,
} from "../../../components/card";
const OneCardDisplay = (data: string | undefined, w: number, h: number) => {
  return (
    <img
      src={data && (imgur_or_static(data) as string)}
      alt="Image"
      width={w}
      height={h}
    />
  );
};
const check_null = (word: string | null | undefined) => {
  if (word) {
    return word.replaceAll(";", "\n");
  } else {
    return "";
  }
};
const card_content = (data2: game_card) => {
  const data = destroy_NULL(data2);
  return (
    <div className="flex flex-col m-8">
      <div className="text-2xl ml-2">Cost: {data?.Cost}</div>
      <div className="p-2 mt-5" style={{ whiteSpace: "pre-line" }}>
        {check_null(data?.On_Play_Effect)}
      </div>
      <div className="flex flex-row ">
        <div style={{ width: 50, height: 50 }}>
          {data.Type1 && Dice_Image(data.Type1)}
        </div>
        <div className="p-2" style={{ width: 60, height: 50 }}>
          {data.Roll1 && data.Roll1}
        </div>
        <div style={{ width: 300 }}>{data.Eff1 && data.Eff1}</div>
      </div>
      <div className="flex flex-row">
        <div style={{ width: 50, height: 50 }}>
          {data.Type2 && Dice_Image(data.Type2)}
        </div>
        <div className="p-2" style={{ width: 60, height: 50 }}>
          {data.Roll2 && data.Roll2}
        </div>
        <div>{data.Eff2 && data.Eff2}</div>
      </div>
      <div className="flex flex-row">
        <div style={{ width: 50, height: 50 }}>
          {data.Type3 && Dice_Image(data.Type3)}
        </div>
        <div className="p-2" style={{ width: 60, height: 50 }}>
          {data.Roll3 && data.Roll3}
        </div>
        <div>{data.Eff3 && data.Eff3}</div>
      </div>
      <div className="flex flex-row">
        <div style={{ width: 50, height: 50 }}>
          {data.Type4 && Dice_Image(data.Type4)}
        </div>
        <div className="p-2" style={{ width: 60, height: 50 }}>
          {data.Roll4 && data.Roll4}
        </div>
        <div>{data.Eff4 && data.Eff4}</div>
      </div>
      <div className="flex flex-row">
        <div style={{ width: 50, height: 50 }}>
          {data.Type5 && Dice_Image(data.Type5)}
        </div>
        <div className="p-2" style={{ width: 60, height: 50 }}>
          {data.Roll5 && data.Roll5}
        </div>
        <div>{data.Eff5 && data.Eff5}</div>
      </div>
    </div>
  );
};
function Card() {
  const [data, setdata] = useState<game_card | null>(null);
  const router = useRouter();
  React.useEffect(() => {
    const slug = router.query.card as string;
    axios
      .get(`api/lor/card/${slug}`)
      .then((res) => {
        setdata(res.data as game_card);
      })
      .catch((error) => console.log(error));
  }, [router.isReady]);
  return (
    <div className="bg-lor bg-fixed overflow-auto bg-contain h-screen">
      <div className="flex flex-row items-center justify-center">
        <div className="flex flex-col text-white">
          <Box
            sx={{
              width: 1200,
              height: "screen",
              backgroundColor: "black",
              opacity: [0.9, 0.9, 0.9],
            }}
            style={{
              boxShadow: `1px -20px 60px -20px ${
                data && color_assign(data.Rarity)
              } inset, 0px 0px 5px -1px #883C82 inset`,
            }}
          >
            <div className="flex flex-col items-center">
              <div className="text-5xl m-8">{data?.Name}</div>
              <div className="text-2xl ml-8">{data?.Rarity}</div>
              <div className="flex flex-row ml-3 mr-3">
                <div>{OneCardDisplay(data?.ImgPath, 600, 400)}</div>
                <div>{data && card_content(data)}</div>
                <div className="flex flex-col items-center">
                  <div>{OneCardDisplay(data?.office_picture, 300, 200)}</div>
                  <div>{OneCardDisplay(data?.rank_picture, 100, 100)}</div>
                  <div>{data?.rank}</div>
                </div>
              </div>
            </div>
          </Box>
        </div>
      </div>
    </div>
  );
}

export default Card;
