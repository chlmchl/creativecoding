let totalFrames = 120;
let counter = 0;
let steps = 20;
let w;
let h;
let theta = 0;


function setup() {
  createCanvas(400, 400);
  w = width / steps;
  h = height / steps;
  rectMode(CENTER);
  noStroke();
}

function draw() {
  let percent = counter / totalFrames;
  render(percent);
  counter++;

  // if (counter == totalFrames) {
  //   exit();
  // }
}

function render(percent) {
  background(6, 214, 160);
  let t = millis();

  

	for(let i =30;i<width-20; i+=30)
	{
	
		for (let k=30; k<height-20; k+=30)
		{ 
      push();
      translate(i,k);
      rotate(t * 0.0005);
      fill(248, 237, 235);
      w = 7 * sin(i + k) * sin(theta) + 15;
      rect(0,0, w, w);
      theta = theta + 0.00005;
      pop();
					
		}
		
	}
  
}