
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

var keyState ={
    'right':0,
    'left':0,
    'up':0,
    'down':0,
    'move':0 
}

app.get('/', function (req, res) {
   res.json(keyState);
})
app.post('/', function (req, res) {
   keyState.down= req.body.down;
   keyState.left= req.body.left;
   keyState.up= req.body.up;
   keyState.right= req.body.right;
   keyState.move= req.body.move;
   res.json(keyState);
})

var server = app.listen(3000, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})