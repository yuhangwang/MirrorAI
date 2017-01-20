declare function require(name:string);


export function
connectMirrorAI()
{   let spawn = require('child_process').spawn;
    let py    = spawn('python', ['../py/proxyMirrorAI.py']);
    let data = [1,2,3,4,5,6,7,8,9];
    let dataString = '';

    py.stdout.on('data', function(d) {
      dataString += d.toString();
    });

    py.stdout.on('end', function() {
      console.log('Sum of numbers=',dataString);
    });

    py.stdin.write(JSON.stringify(data));

    py.stdin.end();
}
