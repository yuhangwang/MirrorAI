declare function require(name:string);


export function
MirrorAI()
{   let spawn = require('child_process').spawn;
    let py    = spawn('python', ['app/py/proxyMirrorAI.py']);
    let data = [1,2,3,4,5,6,7,8,9];
    let dataString = '';

    let d = py.stdout.on('data', function(d) {
      dataString += d.toString();
      return d.toString();
    });

    py.stderr.on('data', (data) => console.log(`stderr: ${data}`));

    py.stdout.on('end', function() {
      console.log('Sum of numbers=',dataString);
    });

    py.stdin.write(JSON.stringify(data));

    py.stdin.end();

    return "hello world - " + dataString;
}
