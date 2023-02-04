import type { NextPage } from "next";
import Link from "next/link";
import Image from "next/image";

// lol
const Home: NextPage = () => {
  return (
      <div className="flex flex-col items-center mt-5">
        <div className="text-white text-5xl font-serif">SELECT GAME</div>
        <div className="flex flex-row items-center">
          <Link passHref href="/lor">
            <div
              className="transform items-center bg-lorlogo w-1/2 justify-center hover:transition duration-500 hover:scale-125"
              style={{
                height: 360,
                width: 640,
              }}
            />
          </Link>
          <div
            className="transform mr-20 items-center justify-center w-1/2 bg-limbuslogo hover:transition duration-500 hover:scale-125"
            style={{
              height: 487,
              width: 502,
            }}
          ></div>
        </div>
      </div>
  );
};

export default Home;
