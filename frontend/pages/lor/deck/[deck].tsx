import React from "react";
import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import { deck } from "../../../components/types";
import { imgur_or_static } from "../../../components/misc";
import axios from "axios";
type combination = {
  ImgPath: string;
  Name: string;
  count: number;
};
const combine_img_count = (deck: deck) => {
  const img = deck.cards;
  const count = deck.card_count;
  const new_combination = img.map((object, i) => {
    const new_stuff: any = object;
    new_stuff.count = count.find(
      (count_object) => count_object.card_id === object.Name
    )?.card_count;
    return new_stuff;
  });
  return new_combination as Array<combination>;
};

const makeDeckPic = (cards: Array<combination>) => {
  console.log(cards);
  const deckPicWithCount = (id: number, card: combination) => {
    const final_str = [];
    for (let i = 0; i < card.count; i++) {
      final_str.push(
        <img
          src={card.ImgPath && imgur_or_static(card.ImgPath)}
          alt="Image"
          width={160}
          height={100}
        />
      );
    }
    return final_str;
  };
  return (
    <div className="flex flex-row flex-wrap">
      {cards.map((object, i) => deckPicWithCount(i, object))}
    </div>
  );
};

const One_Deck = () => {
  const router = useRouter();
  const [deck, setdeck] = useState<deck>();
  useEffect(() => {
    const pid = router.query.deck;
    axios
      .get(`api/lor/deck/${pid}`)
      .then((res) => setdeck(res.data as deck))
      .catch((error) => console.log(error));
  }, [router.isReady]);
  return (
      <div className="flex flex-col items-center w-full">
        <div className="decoration-clone h-screen w-5/6 px-5 text-white content-center bg-black bg-opacity-80">
          <div className="flex flex-col items-center w-full">
            <div className="text-6xl mb-10 text-yellow-300">{deck?.name}</div>
            <div className="flex flex-row w-full">
              <div className="w-1/2">
                <div className="flex flex-col text-lg">
                  <div className="m-2">Rank: {deck?.Recc_Rank}</div>
                  <div className="m-2">Best Floor: {deck?.Recc_Floor}</div>
                  <div className="m-2">Page: {deck?.Recc_Page}</div>
                  <div className="m-2">Description: {deck?.description}</div>
                  <div className="m-2">Effects:</div>
                  <div className="flex flex-col mt-2 ml-5">
                    {deck?.effect.map((object, i) => (
                      <div className="mb-4" key={i}>- {object}</div>
                    ))}
                  </div>
                </div>
              </div>
              <div className="w-1/2 ml-20">
                {deck && makeDeckPic(combine_img_count(deck))}
              </div>
            </div>
          </div>
        </div>
      </div>
  );
};

export default One_Deck;
