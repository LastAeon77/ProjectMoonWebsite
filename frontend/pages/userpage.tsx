import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import axios from "axios";
import { deck } from "../components/types";
import Link from "next/link";
import { Button } from "@mui/material";
import List from "@mui/material/List";


type errors = {
    email?: string;
    username?: string;
    password?: string;
};

const displayuserdecklist = (
    deck: deck,
    id: number,
    router: any
) => {
    const click_button = () => {
        axios.post("/api/lor/delete_deck", { id: deck.id }, {
            headers: {
                Authorization: `JWT ${localStorage.getItem(
                    "access_token"
                )}`,
                "Content-Type": "application/json",
                accept: "application/json",
            },
        })
        router.reload();
    };
    return (
        <div key={id} className="border-t-4" style={{ borderTopColor: "#7A8288" }}>
            <div className="flex flex-col w-full">
                <div className="flex flex-row w-full">
                    <div className="w-1/12">{deck.id}</div>
                    <div className="w-4/12">{deck.name}</div>
                    <div className="w-3/12">{deck.Recc_Rank}</div>
                    <Link passHref href={`/lor/deck/${deck.id}`}>
                        <div className="w-2/12 text-blue-500">Click me!</div>
                    </Link>
                    <Button variant="contained" color="error" onClick={click_button}>
                        Delete
                    </Button>
                </div>
            </div>
        </div>
    );
};

const UserPage = () => {
    const router = useRouter();
    const [userdecks, setuserdecks] = useState<Array<deck> | null>(null);
    useEffect(() => {
        // console.log(localStorage.getItem("access_token"));
        axios
            .get("api/checkauth", {
                headers: {
                    Authorization: `JWT ${localStorage.getItem("access_token")}`,
                    "Content-Type": "application/json",
                    accept: "application/json",
                },
            })
            .catch((errors) => {
                router.push(`/login?prevUrl=userpage`);
            });
        axios
            .get("api/lor/userdecks", {
                headers: {
                    Authorization: `JWT ${localStorage.getItem(
                        "access_token"
                    )}`,
                    "Content-Type": "application/json",
                    accept: "application/json",
                },
            })
            .then((res) =>
                setuserdecks(
                    res.data.sort((a: deck, b: deck) =>
                        a.id < b.id ? 1 : b.id < a.id ? -1 : 0
                    ) as Array<deck>
                )
            )
            .catch((error) => console.log(error));

    }, []);
    return (
        <div className="bg-lor bg-fixed overflow-auto bg-contain h-screen">
            <div className="flex flex-row items-center justify-center">
            <div className="flex flex-row items-center justify-center text-white w-4/5">
            <List
              sx={{ width: "100%", maxWidth: 1800, bgcolor: "#272B30" }}
              component="nav"
              aria-labelledby="nested-list-subheader"
            >
              <div className="flex flex-row w-full justify-center items-center bg-gray-400">
                <div className="w-1/12 ml-3"> ID</div>
                <div className="w-4/12">Name</div>
                <div className="w-3/12">Rank</div>
                <div className="w-2/12">Link</div>
                <div className="w-2/12">Delete?</div>
              </div>
              {userdecks?.map((object, i) =>
                displayuserdecklist(object, i,router)
              )}
            </List>
          </div>
            </div>
        </div>
    );
};

export default UserPage;
