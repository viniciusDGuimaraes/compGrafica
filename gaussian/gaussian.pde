float f(float x)
{
  return cos(x);
}

void setup()
{
  size(1000,800);
  background(255);
  noFill();
}

void draw()
{
  float x0   = -TWO_PI;
  float xf   = TWO_PI;
  float dx   = 0.01;
  float ymax = 1.0;
  float ymin = -1.0;
  int margin = 10;
  float x    = x0;
  float y;
  float xt;
  float yt;
  
  beginShape();
  
  line(margin, height/2, width - margin, height/2);
  line(width/2, margin, width/2, height - margin);
  
  while(x <= xf)
  {
    y  = f(x);
    xt = map(x, x0, xf, margin, width - margin);
    yt = map(y, ymin, ymax, margin, height - margin);
    vertex(xt, yt);
    x += dx;
  }
  
  endShape();
}
