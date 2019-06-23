
var array=[
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','r','r','r','k','k','k','k','k','k'],
    ['k','k','r','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','r','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','k','k','k','k'],
    ['k','k','k','k','k','k','g','k','k','k'],
    ['k','k','k','k','k','k','g','k','b','b'],
    ['k','k','k','k','k','g','g','k','b','b']
];

var width=10
var height=16
var invertFlag=false;
var strip=[];

for (let i = width-1; i >=0 ; i--) {
    for (let j = height-1; j >= 0; j--) {
        if(invertFlag==false){
            strip.push(array[j][i]);
        }else{
            strip.push(array[height-1-j][i]);
        }
    }    
    invertFlag=!invertFlag;
}
var stripMicro='';
strip.forEach(item => {
    stripMicro+=item;
});
console.log(stripMicro);