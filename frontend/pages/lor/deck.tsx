import React from "react";
import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import axios from "axios";
import List from "@mui/material/List";
import ListItemButton from "@mui/material/ListItemButton";
import Collapse from "@mui/material/Collapse";
import Link from "next/link";
import Button from "@mui/material/Button";
import { deck } from "../../components/types";

const displaydecklist = (
  deck: deck,
  id: number,
  activenum: number,
  setactivenum: any
) => {
  const click_button = () => {
    if (activenum === id) {
      setactivenum(-1);
    } else {
      setactivenum(id);
    }
  };
  return (
    <div key={id} className="border-t-4" style={{ borderTopColor: "#7A8288" }}>
      <ListItemButton onClick={click_button}>
        <div className="flex flex-col w-full">
          <div className="flex flex-row w-full">
            <div className="w-1/12">{deck.id}</div>
            <div className="w-4/12">{deck.name}</div>
            <div className="w-4/12">{deck.creator}</div>
            <div className="w-2/12">{deck.Recc_Rank}</div>
            <Link passHref href={`/lor/deck/${deck.id}`}>
              <div className="w-1/12 text-blue-500">Click me!</div>
            </Link>
          </div>
          <Collapse in={id === activenum} timeout="auto" unmountOnExit>
            <List component="div" disablePadding>
              <div className="flex flex-row">
                {deck.card_count.map((object, i) => (
                  <div key={i} className="mr-4 text-yellow-500">
                    {object.card_id} x{object.card_count}
                  </div>
                ))}
              </div>
            </List>
          </Collapse>
        </div>
      </ListItemButton>
    </div>
  );
};
const Deck = () => {
  const [decks, setdecks] = useState<Array<deck>>();
  const [activenum, setactivenum] = useState<number>(-1);
  const router = useRouter();
  useEffect(() => {
    axios
      .get("api/lor/deck")
      .then((res) =>
        setdecks(
          res.data.sort((a: deck, b: deck) =>
            a.id < b.id ? 1 : b.id < a.id ? -1 : 0
          ) as Array<deck>
        )
      )
      .catch((error) => console.log(error));
  }, []);
  const makedeck = () => {
    router.push("/lor/createdeck");
  };
  if (decks) {
    return (
      <div className="bg-fixed overflow-auto bg-contain h-screen">
        <div className="flex flex-col items-center w-full">
          <Button variant="contained" type="submit" onClick={makedeck}>
            Make your deck!
          </Button>
          <div className="flex flex-row items-center justify-center text-white w-4/5">
            <List
              sx={{ width: "100%", maxWidth: 1800, bgcolor: "#272B30" }}
              component="nav"
              aria-labelledby="nested-list-subheader"
            >
              <div className="flex flex-row w-full justify-center items-center bg-gray-400">
                <div className="w-1/12 ml-3"> ID</div>
                <div className="w-4/12">Name</div>
                <div className="w-4/12">Creator</div>
                <div className="w-2/12">Rank</div>
                <div className="w-1/12">Link</div>
              </div>
              {decks?.map((object, i) =>
                displaydecklist(object, i, activenum, setactivenum)
              )}
            </List>
          </div>
        </div>
      </div>
    );
  }
  else {
    return (
      <div className="flex flex-col items-center w-full">
        <div className="text-new_yellow text-4xl">
          Loading...
        </div>
      </div>)
  }
};

export default Deck;
