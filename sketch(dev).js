//Ping Pong JS
//Uncomment code with "np" to enable 2 player mode.
var py = 0
var d = 0
var ps = 0
var cs = 0
var x = 250
var sp = Math.random() * 10 + 10
var y = 250
var xa = 0; var ya = 0
var z = 0
var pu, pd, cu, cd, cy = 0
var r = (Math.random() + 0.6) * 10
var a = (Math.random()) * 22 + 22 + (90 * Math.floor(Math.random() * 4))
var intel = Math.floor(Math.random() * 100)
var t = 400
// np = confirm('Please select a mode (1 player or 2 player). Press OK for 1 player, and press Cancel for 2 players.')

function scale(num, in_min, in_max, out_min, out_max){
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}


function ptc(dist, theta){
	var x = Math.cos(theta * (Math.PI/180)) * dist
	var y = Math.sin(theta * (Math.PI/180)) * dist
	return [x, y]
}
xa = ptc(r,a)[0]
ya = ptc(r,a)[1]

function pause(){
	if (z % 2 == 0){
		noLoop()
		console.log('pause')
	}
	else{
		loop()
	}
	z += 1

}

function collision(pdy){
  // y = py + 70 -> ya = 0
  //y = py -> ya = -1
  //y = py + 140 -> ya = 1
  console.log(x, y, xa, ya, a, py, cy, r, pdy, y - pdy)   
  a = scale(Math.abs(y - pdy), 0, 140, 315, 405) % 360
  console.log(scale(Math.abs(y - pdy), 0, 140, 315, 405) % 360)
  console.log(a)
  xa = ptc(r,a)[0]
  ya = ptc(r,a)[1]
}
function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
} 
function ai(){
	// cy = y
	sp = Math.abs((y - cy) / 10)
	if (y < cy){if (ya < 0){cy -= (sp + 0)} else{cy -= (sp + 0)}}
	else if (y > cy){if (ya > 0){cy += (sp + 0)} else{cy += sp}}
}

function physics(){
  if (x > t /*&& np && intel > 15*/){
    ai()
    
  }
  if (collideRectCircle(5, py, 10, 140, x, y, 20)){ //Ball has collided with player's paddle
    x = 26
    collision(py)
		sp = Math.random() * 10 + 7
    //xa = Math.abs(xa)
		// console.log(sp)
  }
  if (collideRectCircle(485, cy - 70, 10, 140, x, y, 20)){ //Ball has collided with computer's paddle
    x = 474
    //xa = Math.abs(xa) * -1
    collision(cy)

  }

  else if (x > 490){a += 90; xa *= -1; ps += 1; d = 2000; x = 250; y = 250; cy = 0}
  else if (x < 10){a += 90; xa *= -1; ps -= 1; d = 2000; x = 250; y = 250; cy = 0}
  else if (y > 490){a += 90; ya *= -1; y = 490}
  else if (y < 10){a += 90; ya *= -1; y = 10}


}
function setup(){
  createCanvas(500, 500)
}
function mouseMoved() {
  py = mouseY - 70
	// if (! np){
	// 	if (mouseX < 200){py = mouseY - 70}
	// 	if (mouseX > 400){cy = mouseY - 70}
	// }
	// else {py = mouseY - 70}
	return false

}
function mouseDragged(){
  
	py = mouseY - 70
	// if (! np){
	// 	if (mouseX < 200){py = mouseY - 70}
		
	// 	if (mouseX > 400){cy = mouseY - 70}
	// }
	// else {py = mouseY - 70}
	return false
}
function keyPressed(){
	if (keyCode == 27){
		pause()
	}
}
function draw(){
  a = a % 360
  var c = color(255)
  fill(c)
  noStroke()
  if (keyIsDown(83) || keyIsDown(DOWN_ARROW)){
    pd = true
    pu = false
  }
  else if (keyIsDown(87) || keyIsDown(UP_ARROW)){
    pu = true
    pd = false
  }



	else{pu = false; pd = false}
	// if (! np){
	// 	if (keyIsDown(UP_ARROW)){
	// 		cu = true
	// 		cd = false
	// 	}
	// 	else if (keyIsDown(DOWN_ARROW)){
	// 		cd = true
	// 		cu = false
	// 	}
	// 	else {
	// 		cd = false; cu = false
	// 	}
	// 	if(cu){cy -= 10}
	//   else if(cd){cy += 10}
	// }

  if(pu){py -= 10}
  else if (pd){py += 10}

  physics()
  background(0)
  rect(5, py, 10, 140) //Player's paddle
  c = color(255)
  fill(c)
  noStroke()
  ellipse(x, y, 20, 20) //Ball
  c = color(255)
  fill(c)
  noStroke()
  rect(485, cy, 10, 140) //computer's paddle
  if (d > 0){
    sleep(d)
    intel = Math.floor(Math.random() * 100)
		var r = (Math.random() + 0.3) * 10
		var a = (Math.random()) + 45 + (90 * Math.floor(Math.random() * 4))
		xa = ptc(r,a)[0]
		ya = ptc(r,a)[1]
  }
  d = 0
  x += xa
  y += ya
  document.getElementById('scr').innerHTML = 'Score: ' + ps
}
