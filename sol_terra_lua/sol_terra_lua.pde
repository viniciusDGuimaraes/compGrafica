float widSun   = 100, 
  heiSun   = 100, 
  widEarth = 50, 
  heiEarth = 50, 
  dt       = 325, 
  widMoon  = 25, 
  heiMoon  = 25, 
  dl       = 50;

PVector sunPos   = new PVector(0, 0);
PVector earthPos = new PVector(0, 0);
PVector moonPos  = new PVector(0, 0);


void setup() 
{  
  // Posição do sol
  sunPos.x = width/2;
  sunPos.y = height/2;

  // Posição da terra
  earthPos.x = sunPos.x;
  earthPos.y = sunPos.y + dt;

  // Posição da lua
  moonPos.x = earthPos.x;
  moonPos.y = earthPos.y - dl;

  size(1200, 800);
}

void draw()
{
  background(200);
  fill(255);

  // Angulo em que a terra se move
  float at = -millis() / 130000.0 * TWO_PI;
  float al = -millis() / 10000.0 * TWO_PI;

  earthPos.x = sunPos.x + dt * cos(at * TWO_PI);
  earthPos.y = sunPos.y + dt * sin(at * TWO_PI);

  moonPos.x = earthPos.x + dl * cos(al * TWO_PI);
  moonPos.y = earthPos.y + dl * sin(al * TWO_PI);

  ellipse(sunPos.x, sunPos.y, widSun, heiSun);
  ellipse(earthPos.x, earthPos.y, widEarth, heiEarth);
  ellipse(moonPos.x, moonPos.y, widMoon, heiMoon);
}
