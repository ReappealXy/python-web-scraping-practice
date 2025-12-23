import CryptoJS from "crypto-js";

const md5 = CryptoJS.MD5("abc").toString();
console.log(md5);