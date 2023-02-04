import { One_Card, game_card } from "../components/card";
import cards from "../components/cards/[cards]";
import Navbar from "../components/navbar";
const demo_data: game_card = {
  office: "Streetlight Office",
  rank: "Urban Myth",
  Name: "Prepared Mind",
  Cost: 1,
  On_Play_Effect: "NULL",
  Dice_Number: 2,
  ImgPath: "django_static/assets/Cards.png",
  Roll1: "2-4",
  Rarity: "Hardcover",
  Eff1: "endurance1pw",
  Type1: "Block",
  CardType: "Melee",
  Roll2: "2-6",
  Eff2: null,
  Type2: "Slash",
  Roll3: null,
  Eff3: null,
  Type3: null,
  Roll4: null,
  Eff4: null,
  Type4: null,
  Roll5: null,
  Eff5: null,
  Type5: null,
  slug: "prepared-mind",
};
const test = () => {
  return (
    <div>
      <div className="bg-lor bg-fixed overflow-auto bg-contain h-full">
        {/* <Navbar /> */}
        <div className="flex flex-col items-center">
          <div className="decoration-clone overflow-auto h-screen w-11/12 px-5 text-white content-center bg-black bg-opacity-50 font-lor font-extrabold justify-center">
            <div className="flex flex-row justify-center">
              <div>{One_Card(demo_data)}{One_Card(demo_data)}{One_Card(demo_data)}</div>
              <div>{One_Card(demo_data)}{One_Card(demo_data)}{One_Card(demo_data)}</div>
              <div>{One_Card(demo_data)}{One_Card(demo_data)}{One_Card(demo_data)}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default test;
