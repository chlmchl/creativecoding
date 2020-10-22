/*eslint-disable*/

// give a speed value
let speed = 0.005;
let pos_x = 0;
let pos_y = 0;
let w = 10;
let h = 10;
let r = 100;
let g = 100;
let b = 100;
let col;



// défini un array
//let amps = [];
//let speeds = [];

function setup() {
  //console.log("hello from setup");
  createCanvas(400, 400, WEBGL);
  //frameRate(3);

  /*for (let i = 0; i<20; i = i + 1) {
    //amps.push(0); // 20 fois j'ajoute zéro dans ma console = un array avec 20 zéros; 
    amps.push(random(10,100));
    speeds.push(random(0.0001,0.01));
  }*/

  //console.log(amps);
  //console.log("get the first value: ", amps[0]);

  rectMode(CENTER);
}

function draw() {
  background(250,250,255);
  noFill();
  strokeWeight(2);

  let t = millis();
  
  
  
  
  // amp = amplitude
  //let amp = 100;

  // sin renvoie toujours une valeur qui varie entre -1 et 1;
  //let s = sin(0.001 * t);


  //console.log(millis());

  // declare a loop to draw a certain number of rectangles
  for (let i = 0; i < 10; i = i + 1) {
    
    // affect width and height according to their number
    let w = i * 20; /* * random(0.95, 1.1)*/
    let h = i * 20; /* * random(0.95, 1.1)*/

    // affect position on x-axis and y-axis using sin so it oscillates back and forth
    // creates wiggly effect
    let x = 0;
    let y = 0;
    
    
    // animate rotation amplified with mouse position
    let rx = 0.0002 * t ;
    let ry = 0.0002 * t;
    rotateZ(rx);
    //rotateY(ry);
    
    // animate stroke color
    //let col = "hsl(" + ((i + frameCount*2)%360) +", 100%, 90%)";
    stroke(0, 0, 200);
    strokeWeight(i * 0.2 + 1.5);

    //draw the rectangles
    rect(x, y, w, h);
    
  

  }
  
  
  
  

  //noLoop();
}


