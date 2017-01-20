import {MirrorAI} from "./MirrorAI";

const msg = MirrorAI();
console.log(msg);
document.getElementById("msg").innerHTML = "Msg: " + msg;