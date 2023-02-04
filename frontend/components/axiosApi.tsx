import axios from "axios";
export const axiosInstance = axios.create({
    baseURL: axios.defaults.baseURL,
    timeout: 5000,
    headers: {
      Authorization: 'null',
      "Content-Type": "application/json",
      accept: "application/json",
    },
  });
