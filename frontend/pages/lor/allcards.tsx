import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import { One_Card } from "../../components/card";
import { List, ListItemButton } from "@mui/material";
import { office_id, rank_id, game_card_light } from "../../components/types";
import Collapse from "@mui/material/Collapse";

const generate_office_list = (
  id: number,
  office: office_id,
  cards: Array<game_card_light>|undefined,
  activeoffice: number,
  setactiveoffice: any
) => {
  const click_office_button = () => {
    if (activeoffice === id) {
      setactiveoffice(-1);
    } else {
      setactiveoffice(id);
    }
  };
  return (
    <div key={id}>
      <div className="flex flex-col w-full">
        <ListItemButton onClick={click_office_button}>
          <p className="text-xl text-white">{office.Name}</p>
        </ListItemButton>
        <Collapse in={id === activeoffice} timeout="auto" unmountOnExit>
          <List>
            <div className="flex flex-wrap items-center justify-center">
              {cards?.map((object, i) => One_Card(object))}
            </div>
          </List>
        </Collapse>
      </div>
    </div>
  );
};
const generate_rank_list = (
  id: number,
  activerank: number,
  activeoffice: number,
  rank: rank_id,
  office: Array<office_id>|undefined,
  cards: Array<game_card_light>|undefined,
  setactiverank: any,
  setactiveoffice: any
) => {
  const click_rank_button = () => {
    if (activerank === id) {
      setactiverank(-1);
    } else {
      setactiverank(id);
    }
  };
  return (
    <div
      key={id}
      className="border-b-4"
      style={{ borderBottomColor: "#7A8288" }}
    >
      <div className="flex flex-col w-full">
        <ListItemButton onClick={click_rank_button}>
          <p className="text-2xl text-white">{rank.Name}</p>
        </ListItemButton>
        <Collapse in={id === activerank} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {office?.map((object, i) =>
              generate_office_list(
                i,
                object,
                cards?.filter((object_card) => object_card.office === object.id),
                activeoffice,
                setactiveoffice
              )
            )}
          </List>
        </Collapse>
      </div>
    </div>
  );
};

const Cards = () => {
  const [ranks, setranks] = useState<Array<rank_id>>();
  const [offices, setoffices] = useState<Array<office_id>>();
  const [cards, setcards] = useState<Array<game_card_light>>();
  const [activerank, setactiverank] = useState<number>(-1);
  const [activeoffice, setactiveoffice] = useState<number>(-1);
  useEffect(() => {
    axios
      .get("api/lor/rank")
      .then((res) =>
        setranks(
          res.data.sort((a: rank_id, b: rank_id) =>
            a.id > b.id ? 0 : -1
          ) as Array<rank_id>
        )
      )
      .catch((errors) => console.log(errors));
    axios
      .get("api/lor/office")
      .then((res) => setoffices(res.data as Array<office_id>))
      .catch((errors) => console.log(errors));
    axios
      .get("api/lor/cardlight")
      .then((res) => setcards(res.data as Array<game_card_light>))
      .catch((errors) => console.log(errors));
  }, []);
  if (ranks) {
    return (
      <div className="bg-lor bg-fixed overflow-auto h-screen">
        <div className="flex flex-col items-center">
          <List
            sx={{ width: "100%", maxWidth: 1300, bgcolor: "black" }}
            component="nav"
            aria-labelledby="nested-list-subheader"
          >
            {ranks.map((object, i) =>
              generate_rank_list(
                i,
                activerank,
                activeoffice,
                object,
                offices?.filter(
                  (office_object) => office_object.Rank === object.id
                ),
                cards?.filter((card_object) => card_object.rank === object.id),
                setactiverank,
                setactiveoffice
              )
            )}
          </List>
        </div>
      </div>
    );
  } else {
    return (
      <div className="bg-lor bg-fixed overflow-auto h-screen">
        <div className="flex flex-col items-center text-white">
          Loading... This may take a while
        </div>
      </div>
    );
  }
};

export default Cards;
