"use strict";
const MirrorAI_1 = require("./MirrorAI");
const msg = MirrorAI_1.MirrorAI();
console.log(msg);
document.getElementById("msg").innerHTML = "Msg: " + msg;
