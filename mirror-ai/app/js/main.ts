import {app, BrowserWindow} from "electron";
import {render} from "./render";


let mainWindow = null;
app.on('ready',
    () => {
        console.log("hello from electron!");
        mainWindow = new BrowserWindow();
        mainWindow.webContents.loadURL(`file://${__dirname}/../html/index.html`);
    }
    );
