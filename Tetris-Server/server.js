
var express = require('express');
var app = express();
var cors = require('cors')
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(cors());
app.use(bodyParser.urlencoded({
    extended: true
}));

var keyState ={
    'right':0,
    'left':0,
    'move':0,
    'down':0,
    'play':0,
    'reboot':0
}
function reboot(){
    return {
      'right':0,
      'left':0,
      'move':0,
      'down':0,
      'play':0,
      'reboot':0
  }
}
app.get('/', function (req, res) {
   res.json(keyState);
   keyState = reboot();
})
app.post('/', function (req, res) {
   keyState.down = req.body.down;
   keyState.left = req.body.left;
   keyState.right = req.body.right;
   keyState.move = req.body.move;
   keyState.play = req.body.play;
   keyState.reboot = req.body.reboot;
   res.json('done');

   console.log('OK');
})

app.post('/draw', function (req, res) {
   
   res.json('done');

   console.log(req.body);
})

var server = app.listen(3000, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})