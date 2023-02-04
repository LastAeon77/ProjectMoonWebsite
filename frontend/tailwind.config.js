const { url } = require("inspector");

module.exports = {
  purge: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      backgroundImage: {
        loading: 'url("/static/assets/Loading_Screeen_2.jpg")',
        wings: 'url("/static/assets/wings.png")',
        lorlogo: 'url("/static/assets/logo.png")',
        limbuslogo: 'url("/static/assets/limbus.png")',
        void: 'url("/static/assets/void.png")'
      },
      colors:{
        // 'black': "#393E46",
        // 'white': "#F7F7F7",
        // 'grey': "#5C636E",
        // 'yellow': "#F8B500"
        'black': "#222831",
        'white': "#EEEEEE",
        'grey': "#393E46",
        'new_yellow': "#FFD369",
        'total_black': '#000000'
      },
      fontFamily: {
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
