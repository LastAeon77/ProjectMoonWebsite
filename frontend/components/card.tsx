import React from "react";
import axios from "axios";
import { Box } from "@mui/system";
import { imgur_or_static } from "./misc";
import Link from "next/link";
import Image from "next/dist/client/image";
import { game_card_light } from "./types";
export type game_card = {
  office: string;
  rank: string;
  rank_picture: string;
  office_picture: string;
  Name: string;
  Cost: number;
  On_Play_Effect: string | null;
  Dice_Number: number;
  ImgPath: string;
  Roll1: string | null;
  Rarity: string | null;
  Eff1: string | null;
  Type1: string | null;
  CardType: string;
  Roll2: string | null;
  Eff2: string | null;
  Type2: string | null;
  Roll3: string | null;
  Eff3: string | null;
  Type3: string | null;
  Roll4: string | null;
  Eff4: string | null;
  Type4: string | null;
  Roll5: string | null;
  Eff5: string | null;
  Type5: string | null;
  slug: string;
};

export const Dice_Image = (dicetype: string) => {
  // This assigns dice images to each name
  const size = 40;
  switch (dicetype) {
    case "Blunt":
      return (
        <Image
          src="/static/dice_type/AtkBlunt.png"
          alt="Blunt"
          height={size}
          width={size}
        />
      );
    case "Thurst":
      return (
        <Image
          src="/static/dice_type/AtkPierce.png"
          alt="Thrust"
          height={size}
          width={size}
        />
      );
    case "Pierce":
      return (
        <Image
          src="/static/dice_type/AtkPierce.png"
          alt="Thrust"
          height={size}
          width={size}
        />
      );
    case "Slash":
      return (
        <Image
          src="/static/dice_type/AtkSlash.png"
          alt="Slash"
          height={size}
          width={size}
        />
      );
    case "Evade":
      return (
        <Image
          src="/static/dice_type/DefEvade.png"
          alt="Evade"
          height={size}
          width={size}
        />
      );
    case "Block":
      return (
        <Image
          src="/static/dice_type/DefGuard.png"
          alt="Block"
          height={size}
          width={size}
        />
      );
    case "Blunt Counter":
      return (
        <Image
          src="/static/dice_type/StandbyBlunt.png"
          alt="Blunt Counter"
          height={size}
          width={size}
        />
      );
    case "Pierce Counter":
      return (
        <Image
          src="/static/dice_type/StandbyPierce.png"
          alt="Thrust Counter"
          height={size}
          width={size}
        />
      );
    case "Slash Counter":
      return (
        <Image
          src="/static/dice_type/StandbySlash.png"
          alt="Slash Counter"
          height={size}
          width={size}
        />
      );
    case "Evade Counter":
      return (
        <Image
          src="/static/dice_type/StandbyEvade.png"
          alt="Evade Counter"
          height={size}
          width={size}
        />
      );
    case "Block Counter":
      return (
        <Image
          src="/static/dice_type/StandbyGuard.png"
          alt="Block Counter"
          height={size}
          width={size}
        />
      );
    default:
      return null;
  }
};

export const destroy_NULL = (obj: any) => {
  for (let keys in obj) {
    if (obj[keys] === "NULL") {
      obj[keys] = null as any;
    }
  }
  return obj;
};
export const color_assign = (str: string | null) => {
  switch (str) {
    case "Objet d'art":
      return "gold";
    case "Paperback":
      return "green";
    case "Hardcover":
      return "blue";
    case "Limited":
      return "purple";
    case "EGO":
      return "red";
    default:
      return "green";
  }
};
export const One_Card = (data2: game_card | game_card_light) => {
  // Generate the Card Element
  const data = destroy_NULL(data2);
  return (
    <Link href={`/lor/card/${data?.slug}`} passHref key={data?.id}>
      <div className="text-white">
        <Box
          sx={{
            borderRadius: "1em",
          }}
          style={{
            width: 400,
            height: 230,
            backgroundColor: "black",
            margin: "6px",
            boxShadow: `1px -20px 60px -20px ${color_assign(
              data.Rarity
            )} inset, 0px 0px 5px -1px ${color_assign(data.Rarity)} inset`,
          }}
        >
          <div className="flex flex-col content-center text-white">
            <div className="text-white ml-4 text-xl">{data?.Name}</div>
            <div className="flex flex-row items-left">
              <div className="flex flex-col items-center">
                <div className="ml-4" style={{ width: 150 }}>
                  <img
                    width={150}
                    src={String(data.ImgPath && imgur_or_static(data.ImgPath))}
                  />
                </div>
                <div className="flex-1 text-3xl">{data?.Cost}</div>
              </div>
              <div>
                <div className="flex flex-col flex-wrap text-sm">
                  <div>{data.On_Play_Effect && data.On_Play_Effect}</div>
                  <div className="flex flex-row">
                    <div className="text-sm">
                      {data.Type1 && Dice_Image(data.Type1)}
                    </div>
                    <div className="mr-2">{data.Roll1 && data.Roll1}</div>
                    <div>{data.Eff1 && data.Eff1}</div>
                  </div>
                  <div className="flex flex-row">
                    <div>{data.Type2 && Dice_Image(data.Type2)}</div>
                    <div className="mr-2">{data.Roll2 && data.Roll2}</div>
                    <div className="flex-wrap">{data.Eff2 && data.Eff2}</div>
                  </div>
                  <div className="flex flex flex-row">
                    <div>{data.Type3 && Dice_Image(data.Type3)}</div>
                    <div className="mr-2">{data.Roll3 && data.Roll3}</div>
                    <div className="flex flex-wrap">
                      {data.Eff3 && data.Eff3}
                    </div>
                  </div>
                  <div className="flex flex-row">
                    <div style={{ width: 50, height: 50 }}>
                      {data.Type4 && Dice_Image(data.Type4)}
                    </div>
                    <div className="mr-2">{data.Roll4 && data.Roll4}</div>
                    <div className="flex flex-wrap">
                      {data.Eff4 && data.Eff4}
                    </div>
                  </div>
                  <div className="flex flex-row">
                    <div style={{ width: 50, height: 50 }}>
                      {data.Type5 && Dice_Image(data.Type5)}
                    </div>
                    <div className="mr-2">{data.Roll5 && data.Roll5}</div>
                    <div className="flex flex-wrap">
                      {data.Eff5 && data.Eff5}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Box>
      </div>
    </Link>
  );
};
