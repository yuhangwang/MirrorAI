let PythonShell = require('python-shell');
let pyshell = new PythonShell('hello.py');

pyshell.send('Steven');
pyshell.on('message', (msg) => console.log(msg));

pyshell.end(
    (err) => {
        if (err) throw err;
        console.log('finished!');
    }
);
