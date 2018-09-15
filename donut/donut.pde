void setup() 
{
  
  size(800,600);
}

void draw()
{
  background(200);
  
  translate(width/2, height/2);
  
  int x = 0;
  int y = 0;
  float values[] = new float[] {10.0, 15.0, 8.0, 20.0};
  /*color palette[]  = new color[]
  {
    color(255,0,0),
    color(255,128,0),
    color(255,255,0),
    color(0,255,0)
  };*/
  
  int totalValue = 0;
  
  for(int i = 0; i < values.length; i++)
  {
    totalValue += values[i];
  }
  
  float offset = 0;
  
  for(int i = 0; i < values.length; i++)
  {
    arc(x, y, 200, 200, offset, offset + (values[i]/totalValue) * TWO_PI);
    offset += (values[i]/totalValue) * TWO_PI;
    color(255,0,0);
  }
  
  arc(0,0,100,100,0,TWO_PI);
  //noFill();
}
