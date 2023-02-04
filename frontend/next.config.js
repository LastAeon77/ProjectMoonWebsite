/** @type {import('next').NextConfig} */
const withImages = require('next-images')
module.exports = withImages()
module.exports = {
  reactStrictMode: true,
  // async redirects() {
  //   return [

  //   ]
  // },
  images: {
    domains: ['localhost','i.imgur.com'],
  },
}


