import {app, BrowserWindow} from "electron";


let mainWindow = null;
app.on('ready',
    () => {
        console.log("hello from electron!");
        mainWindow = new BrowserWindow();
        mainWindow.webContents.loadURL(`file://${__dirname}/../html/index.html`);
    }
    );
