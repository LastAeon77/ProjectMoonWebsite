import React from "react";
import { useState } from "react";
import axios from "axios";
import Navbar from "../../components/navbar";
import { one_abno } from "../../components/abnormality";
import { abno_card } from "../../components/types";

type floor = {
  history: Array<abno_card> | undefined;
  tech: Array<abno_card> | undefined;
  art: Array<abno_card> | undefined;
  lit: Array<abno_card> | undefined;
  science: Array<abno_card> | undefined;
  language: Array<abno_card> | undefined;
  social: Array<abno_card> | undefined;
  philosophy: Array<abno_card> | undefined;
  religion: Array<abno_card> | undefined;
  general: Array<abno_card> | undefined;
};
type floorhidden = {
  history: boolean;
  tech: boolean;
  art: boolean;
  lit: boolean;
  science: boolean;
  language: boolean;
  social: boolean;
  philosophy: boolean;
  religion: boolean;
  general: boolean;
};

const render_cards = (
  data: Array<abno_card> | undefined,
  floor_name: string,
  hidden: boolean
) => {
  data?.sort((a, b) => a.emotion_level - b.emotion_level);
  return (
    <div className={hidden ? "hidden" : undefined}>
      <div className="flex flex-col bg-black bg-opacity-70 items-center">
        <div className="text-bold text-2xl font-extrabold text-white">
          {floor_name}
        </div>
        <div className="flex flex-row items-center justify-center">
          <div>
            {data &&
              data.map((object, i) => (i % 3 == 0 ? one_abno(object) : null))}
          </div>
          <div>
            {data &&
              data.map((object, i) => (i % 3 == 1 ? one_abno(object) : null))}
          </div>
          <div>
            {data &&
              data.map((object, i) => (i % 3 == 2 ? one_abno(object) : null))}
          </div>
        </div>
      </div>
    </div>
  );
};

const Abno = () => {
  // const [dataRaw, setdataRaw] = useState<Array<abno_card> | null>();
  const [data, setdata] = useState<floor | null>();
  const [hidden, sethidden] = useState<floorhidden>({
    history: false,
    tech: false,
    art: false,
    lit: false,
    science: false,
    language: false,
    social: false,
    philosophy: false,
    religion: false,
    general: false,
  });
  const handle_click = (floor: String) => {
    switch (floor) {
      case "history":
        sethidden({
          history: false,
          tech: true,
          art: true,
          lit: true,
          science: true,
          language: true,
          social: true,
          philosophy: true,
          religion: true,
          general: true,
        });
        break;
      case "tech":
        sethidden({
          history: true,
          tech: false,
          art: true,
          lit: true,
          science: true,
          language: true,
          social: true,
          philosophy: true,
          religion: true,
          general: true,
        });
        break;
      case "art":
        sethidden({
          history: true,
          tech: true,
          art: false,
          lit: true,
          science: true,
          language: true,
          social: true,
          philosophy: true,
          religion: true,
          general: true,
        });
        break;
      case "lit":
        sethidden({
          history: true,
          tech: true,
          art: true,
          lit: false,
          science: true,
          language: true,
          social: true,
          philosophy: true,
          religion: true,
          general: true,
        });
        break;
      case "science":
        sethidden({
          history: true,
          tech: true,
          art: true,
          lit: true,
          science: false,
          language: true,
          social: true,
          philosophy: true,
          religion: true,
          general: true,
        });
        break;
      case "language":
        sethidden({
          history: true,
          tech: true,
          art: true,
          lit: true,
          science: true,
          language: false,
          social: true,
          philosophy: true,
          religion: true,
          general: true,
        });
        break;
      case "social":
        sethidden({
          history: true,
          tech: true,
          art: true,
          lit: true,
          science: true,
          language: true,
          social: false,
          philosophy: true,
          religion: true,
          general: true,
        });
        break;
      case "philosophy":
        sethidden({
          history: true,
          tech: true,
          art: true,
          lit: true,
          science: true,
          language: true,
          social: true,
          philosophy: false,
          religion: true,
          general: true,
        });
        break;
      case "religion":
        sethidden({
          history: true,
          tech: true,
          art: true,
          lit: true,
          science: true,
          language: true,
          social: true,
          philosophy: true,
          religion: false,
          general: true,
        });
        break;
      case "general":
        sethidden({
          history: true,
          tech: true,
          art: true,
          lit: true,
          science: true,
          language: true,
          social: true,
          philosophy: true,
          religion: true,
          general: false,
        });
        break;
      default:
        sethidden({
          history: false,
          tech: false,
          art: false,
          lit: false,
          science: false,
          language: false,
          social: false,
          philosophy: false,
          religion: false,
          general: false,
        });
        break;
    }
  };
  React.useEffect(() => {
    // const pid = parseInt(router.query.abnormality as string, 10);
    axios
      .get("api/lor/abno/")
      .then((res) => {
        setdata({
          history: res.data?.filter(
            (object: abno_card) => object.office === "Floor of History"
          ),
          tech: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Technology"
          ),
          art: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Art"
          ),
          lit: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Literature"
          ),
          science: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Natural Science"
          ),
          language: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Languages"
          ),
          social: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Social Sciences"
          ),
          philosophy: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Philosophy"
          ),
          religion: res.data?.filter(
            (object: abno_card) => object.office === "Floor of Religion"
          ),
          general: res.data?.filter(
            (object: abno_card) => object.office === "Floor of General Works"
          ),
        });
      })
      .catch((error) => console.log(error));
  }, []);
  return (
    <div className="bg-fixed overflow-auto bg-contain h-screen">
      <div className="flex flex-col items-center">
        <button
          className="bg-pink-300 hover:bg-blue-300 text-purple font-bold py-2 px-4 rounded"
          onClick={() => handle_click("all")}
        >
          All
        </button>
        <div className="flex flex-row items-center">
          <button
            className="bg-yellow-900 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            onClick={() => handle_click("history")}
          >
            History
          </button>
          <button
            className="bg-purple-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            onClick={() => handle_click("tech")}
          >
            Technology
          </button>
          <button
            className="bg-green-500 hover:bg-blue-700 text-black font-bold py-2 px-4 rounded"
            onClick={() => handle_click("art")}
          >
            Art
          </button>
          <button
            className="bg-yellow-500 hover:bg-blue-700 text-black font-bold py-2 px-4 rounded"
            onClick={() => handle_click("lit")}
          >
            Literature
          </button>
          <button
            className="bg-red-500 hover:bg-blue-700 text-green font-bold py-2 px-4 rounded"
            onClick={() => handle_click("language")}
          >
            Language
          </button>
          <button
            className="bg-yellow-300 hover:bg-blue-700 text-blue font-bold py-2 px-4 rounded"
            onClick={() => handle_click("science")}
          >
            Natural Sciences
          </button>
          <button
            className="bg-blue-500 hover:bg-blue-700 text-yellow font-bold py-2 px-4 rounded"
            onClick={() => handle_click("social")}
          >
            Chesed
          </button>
          <button
            className="bg-total_black hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            onClick={() => handle_click("philosophy")}
          >
            Philosophy
          </button>
          <button
            className="bg-white hover:bg-blue-700 text-black font-bold py-2 px-4 rounded"
            onClick={() => handle_click("religion")}
          >
            Religion
          </button>
          <button
            className="bg-gray-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            onClick={() => handle_click("general")}
          >
            General Works
          </button>
        </div>
        <div className="flex flex-col items-center justify-center">
          {render_cards(data?.history, "Floor of History", hidden.history)}
          {render_cards(data?.tech, "Floor of Technology", hidden.tech)}
          {render_cards(data?.art, "Floor of Art", hidden.art)}
          {render_cards(data?.lit, "Floor of Literature", hidden.lit)}
          {render_cards(data?.science, "Floor of Science", hidden.science)}
          {render_cards(data?.language, "Floor of Language", hidden.language)}
          {render_cards(data?.social, "Floor of Social", hidden.social)}
          {render_cards(
            data?.philosophy,
            "Floor of Philosophy",
            hidden.philosophy
          )}
          {render_cards(data?.religion, "Floor of Religion", hidden.religion)}
          {render_cards(
            data?.general,
            "Floor of General Works",
            hidden.general
          )}
        </div>
      </div>
    </div>
  );
};

export default Abno;
