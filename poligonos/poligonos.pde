float n = 3;
float radius = height;

void setup()
{
  size(800,600);
}

void draw()
{
  float x = radius/2;
  float y = radius;
 
  background(200);
  
  translate(width/2, height/2);
  
  float angle = TWO_PI/n;
  
  beginShape();
  for (float i = 0; i < TWO_PI; i += angle) 
  {
    x += -cos(i) * radius;
    y += -sin(i) * radius;
    vertex(x, y);
  }
  
  endShape(CLOSE);
}

void keyPressed()
{
  if (key >= 51 && key <= 57)
  {
    n = key - 48;
  }
}
