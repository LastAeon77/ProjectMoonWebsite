import "../styles/globals.css";
import { useRouter } from "next/router";
import type { AppProps } from "next/app";
import { useState, useEffect } from "react";
import axios from "axios";
import Navbar from "../components/navbar";

if (typeof window !== "undefined") {
  axios.defaults.baseURL = window.location.origin;
}

function MyApp({ Component, pageProps }: AppProps) {
  const router = useRouter();
  const [pageLoading, setPageLoading] = useState<boolean>(false);
  useEffect(() => {
    const handleStart = () => {
      setPageLoading(true);
    };
    const handleComplete = () => {
      setPageLoading(false);
    };

    router.events.on("routeChangeStart", handleStart);
    router.events.on("routeChangeComplete", handleComplete);
    router.events.on("routeChangeError", handleComplete);
  }, [router]);
  if (pageLoading) {
    return (
      <div className="bg-loading bg-contain h-screen">
      </div>
    );
  } else {
    return (
      <div className="bg-black overflow-auto w-screen h-screen">
        <Navbar />
        <Component {...pageProps} />
      </div>
    );
  }
}

export default MyApp;
