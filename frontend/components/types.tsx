export type card_id = {
  id: number;
  Name: string;
  ImgPath: string;
};
export type abno_card = {
  id: number;
  office: string;
  name: string;
  effects: string;
  description: string;
  ImgPath: string;
  emotion_type: string;
  emotion_level: number;
};
export type office_id = {
  id: number;
  Name: string;
  Rank: number;
};
export type page_id = {
  Name: string;
  id: number;
};
export type effect_id = {
  id: number;
  Name: string;
  Description: string;
};
export type rank_id = {
  id: number;
  Name: string;
  Slogan: string;
  Description: string;
  ImgPath: string;
  slug: string;
};

export type game_card_light = {
  office: number;
  rank: number;
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
export type card_count = {
  card_count: number;
  card_id: string;
};
export type name_and_pic = {
  Name: string;
  ImgPath: string;
};
export type deck = {
  id: number;
  card_count: card_count[];
  cards: name_and_pic[];
  effect: Array<string>;
  Recc_Floor: string | null;
  Recc_Page: string | null;
  Recc_Rank: string | null;
  creator: string;
  name: string;
  description: string;
  show: boolean;
};
export type interview_lite = {
  id: number;
  name: string;
  date: Date;
  last_modified: string;
};

export type interview = {
  id: number;
  name: string;
  body:string;
  date: Date;
  last_modified: string;
};
export const colors = {
  white: "#F7F7F7",
  black: "#393E46",
  grey: "#5C636E",
  yellow: "#F8B500"
}