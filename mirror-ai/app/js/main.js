"use strict";
const electron_1 = require("electron");
let mainWindow = null;
electron_1.app.on('ready', () => {
    console.log("hello from electron!");
    mainWindow = new electron_1.BrowserWindow();
    mainWindow.webContents.loadURL(`file://${__dirname}/../html/index.html`);
});
