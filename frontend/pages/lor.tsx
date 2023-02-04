import React from "react";
import Card from "@mui/material/Card";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import CardActionArea from "@mui/material/CardActionArea";
import Link from "next/link";

const lor = () => {
  return (
    <div className="flex flex-col items-center">
      <div className="flex font-serif text-new_yellow text-5xl my-3">
        Available Directories
      </div>
      <div className="flex flex-row" style={{ minHeight: 100 }}>
        <div className="flex-1 grid place-items-center px-4 ">
          <Card
            sx={{
              minWidth: 275, borderRadius: "10%"
            }}
            style={{ backgroundColor: "black" }}
          >
            <Link href="/lor/allcards" passHref>
              <CardActionArea>
                <CardMedia
                  component="img"
                  height="140"
                  image="https://malcute.aeonmoon.page/django_static/LoR_Data/Card/Canard/Basic/Basic_Thrust.png"
                  sx={{
                    filter: "brightness(50%)", ":hover": {
                      boxShadow: 20,
                      filter: "brightness(100%)"
                    },
                  }}

                />
                <CardContent>
                  <Typography variant="h5" component="div">
                    <div className="font-serif text-white">
                      Cards
                    </div>
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Link>
          </Card>
        </div>
        <div className="flex-1 grid place-items-center px-4">
          <Card
            sx={{ minWidth: 275, borderRadius: "10%" }}
            style={{ backgroundColor: "black" }}
          >
            <Link href="/lor/abno" passHref>
              <CardActionArea>
                <CardMedia
                  component="img"
                  height="100"
                  image="https://malcute.aeonmoon.page/django_static/LoR_Data/Abnormality%20Pages/Floor%20of%20History/Happy%20Teddy%20Bear/Happy%20Memories.png"
                  sx={{
                    filter: "brightness(50%)", ":hover": {
                      boxShadow: 20,
                      filter: "brightness(100%)"
                    },
                  }}
                />
                <CardContent>
                  <Typography variant="h5" component="div">
                    <div className="font-serif text-white">
                      Abnormalities
                    </div>
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Link>
          </Card>
        </div>
        <div className="flex-1 grid place-items-center px-4">
          <Card
            sx={{ minWidth: 275, borderRadius: "10%" }}
            style={{ backgroundColor: "black" }}
          >
            <Link href="/lor/deck" passHref>
              <CardActionArea>
                <CardMedia
                  component="img"
                  height="100"
                  image="https://malcute.aeonmoon.page/django_static/LoR_Data/Abnormality%20Pages/Floor%20of%20Social%20Sciences/Scarecrow%20Searching%20for%20Wisdom/Torn%20Off%20Wisdom.png"
                  sx={{
                    filter: "brightness(50%)", ":hover": {
                      boxShadow: 20,
                      filter: "brightness(100%)"
                    },
                  }}
                />
                <CardContent>
                  <Typography variant="h5" component="div">
                    <div className="font-serif text-white">
                      Decks
                    </div>
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Link>
          </Card>
        </div>
      </div>
    </div >
  );
};

export default lor;
