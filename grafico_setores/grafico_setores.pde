void setup() 
{
  
  size(800,600);
  textAlign(CENTER,CENTER);
  textSize(36);
  stroke(0);
}

void draw()
{
  background(200);
  int x = width/2;
  int y = height/2;
  float values[] = new float[] {10.0, 15.0, 8.0, 20.0};
  color palette[]  = new color[]
  {
    color(255,0,0),
    color(255,128,0),
    color(255,255,0),
    color(0,255,0)
  };
  int totalValue = 0;
  
  for(int i = 0; i < values.length; i++)
  {
    totalValue += values[i];
  }
  
  float offset = 0;
  
  for(int i = 0; i < values.length; i++)
  {
    if(i == 0)
    {
      arc(x, y, 100, 100, offset, offset + (values[i]/totalValue) * TWO_PI);
      offset += (values[i]/totalValue) * TWO_PI;
      fill(palette[i]);
    }
    else
    {
      arc(x, y, 100, 100, offset, offset + (values[i]/totalValue) * TWO_PI);
      offset += (values[i]/totalValue) * TWO_PI;
      fill(palette[i]);
    }
  }
}
