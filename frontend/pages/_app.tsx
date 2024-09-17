import "../styles/globals.css";
import { useRouter } from "next/router";
import type { AppProps } from "next/app";
import { useState, useEffect } from "react";
import axios from "axios";
import Navbar from "../components/navbar";

// This makes sure we call our own domain for information when you set your own domain.
if (typeof window !== "undefined") {
  axios.defaults.baseURL = window.location.origin;
  // axios.defaults.baseURL = "http://127.0.0.1:8000"
  // axios.defaults.baseURL = "https://malcute.aeonmoon.page/"
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
