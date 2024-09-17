import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/router";
import jwt_decode from "jwt-decode";
import axios from "axios";
const string_or_null = (string: string | string[] | null) => {
  if (string) {
    return string;
  }
  return "";
};

const Username = (
  username: string | null,
  prevUrl: string | string[] | null
) => {
  if (username) {
    return (
      <>
        <li className="nav-item">
          <Link href="/userpage" passHref>
            <div className="px-3 py-2 flex items-center text-lg uppercase font-bold leading-snug text-white hover:opacity-75">
              <i className="fab fa-facebook-square text-lg leading-lg text-white opacity-75"></i>
              <span className="ml-2">{username}</span>
            </div>
          </Link>
        </li>
        <li className="nav-item">
          <Link href={`/logout?prevUrl=${string_or_null(prevUrl)}`} passHref>
            <div className="px-3 py-2 flex items-center  text-lg uppercase font-bold leading-snug text-white hover:opacity-75">
              <i className="fab fa-twitter text-lg leading-lg text-white opacity-75"></i>
              <span className="ml-2">Logout</span>
            </div>
          </Link>
        </li>
      </>
    );
  } else {
    return (
      <>
        <li className="nav-item">
          <Link href={`/signup`} passHref>
            <div className="px-3 py-2 flex items-center text-lg uppercase font-bold leading-snug text-white hover:opacity-75">
              <i className="fab fa-facebook-square text-lg leading-lg text-white opacity-75"></i>
              <span className="ml-2">Register</span>
            </div>
          </Link>
        </li>
        <li className="nav-item">
          <Link href={`/login?prevUrl=${string_or_null(prevUrl)}`} passHref>
            <div className="px-3 py-2 flex items-center text-lg uppercase font-bold leading-snug text-white hover:opacity-75">
              <i className="fab fa-facebook-square text-lg leading-lg text-white opacity-75"></i>
              <span className="ml-2">Login</span>
            </div>
          </Link>
        </li>
      </>
    );
  }
};
type token = {
  exp: number;
  fav_color: string;
  iat: number;
  jti: string;
  token_type: string;
  user_id: number;
  username: string;
};
const Navbar = () => {
  const [username, setusername] = useState<string | null>(null);
  const [home_bg_color, sethome_color] = useState<string>('bg-grey')
  const [lor_bg_color, setlor_color] = useState<string>('bg-grey')
  const [interview_bg_color, setinterview_color] = useState<string>('bg-grey')
  const router = useRouter();
  useEffect(() => {
    const rawtoken = localStorage.getItem("access_token");
    try {
      const token: any = rawtoken && jwt_decode(rawtoken);
      setusername(token?.username);
    } catch (e) {
      setusername(null);
    }
    if (router.pathname.slice(0, 50) === '/') {
      sethome_color('bg-black')
    }
    else {
      sethome_color('bg-grey')
    }
    if (router.pathname.slice(0, 4) === '/lor') {
      setlor_color('bg-black')
    }
    else {
      setlor_color('bg-grey')
    }
    if (router.pathname.slice(0, 10) === '/interview') {
      setinterview_color('bg-black')
    }
    else {
      setinterview_color('bg-grey')
    }
  }, [router]);

  return (
    <nav className="relative justify-between bg-grey flex-wrap flex text-white">
      <button>
        <Link href="/" passHref>
          <div className={`w-72 h-16 ${home_bg_color} grid content-center justify-center`}>
            <div className="font-serif font-bold leading-relaxed inline-block py-2 uppercase place-content-center text-lg">
              Aeonmoon Homepage
            </div>
          </div>
        </Link>
      </button>
      <button>
        <Link href="/lor" passHref>
          <div className={` w-auto px-3 h-16 ${lor_bg_color} grid content-center justify-center`}>
            <div className=" text-base leading-relaxed inline-block py-2 whitespace-nowrap uppercase">
              Library of Ruina
            </div>
          </div>
        </Link>
      </button>
      <button>
        <Link href="/interview" passHref>
          <div className={` w-auto px-3 h-16 ${interview_bg_color} grid content-center justify-center`}>
            <div className=" text-base leading-relaxed inline-block py-2 whitespace-nowrap uppercase">
              Interview
            </div>
          </div>
        </Link>
      </button>
      <button className="flex flex-row ml-auto items-center" >
        <ul className="flex lg:flex-row content-end">
          {Username(username, router.pathname)}
        </ul>
      </button>
    </nav>
  );
};

export default Navbar;
