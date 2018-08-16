float psx;
float psy;
float rs  = 100;
float ptx;
float pty;
float rt  = 30;
float plx;
float ply;
float rl  = 10;
float dt;
float dl;

void setup() 
{
  size(1200,800);
  psx = width/2;
  psy = height/2;
  ptx = psx;
  pty = psy + 300;
  plx = ptx;
  ply = pty - 75;
  
  dl = sqrt(pow(ptx - plx,2) + pow(pty - ply,2));
  textAlign(CENTER,CENTER);
  textSize(36);
  stroke(0);
}

void draw()
{
  background(200);
  fill(255);
  int al = 5;  //Angula rotação lua
  int at = 65; //Angulo rotação terra
  
  ellipse(psx,psy,rs*2,rs*2);
  ellipse(ptx,pty,rt*2,rt*2);
  ellipse(plx,ply,rl*2,rl*2);
  
  //float[] newEarthPos = rotateEarth(psx, psy, ptx, pty,  at, dt);
  //float[] newMoonPos  = rotateMoon (ptx, pty, plx, ply, al, dl);
  
  /*ptx = newEarthPos[0];
  pty = newEarthPos[1];
  /*plx = newMoonPos[0];
  ply = newMoonPos[1];*/
}

float[] rotateEarth(float psx, float psy, float ptx, float pty, int at)
{
  float dt = sqrt(pow(psx - ptx,2) + pow(psy - pty,2));
  float newPtx = dt * cos(at) + psx;
  float newPty = dt * sin(at) + psy;
  
  return new float[] {newPtx, newPty};
}

float[] rotateMoon(float ptx, float pty, float plx, float ply, int al, float dl)
{
  float newPlx = dl * cos(al) + psx;
  float newPly = dl * sin(al) + pty;
  
  return new float[] {newPlx, newPly};
}
