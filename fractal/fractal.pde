void setup(){
  size(800,600);
}

void draw(){
  background(200);
  float ax = 10;
  float ay = 300;
  float bx = 790;
  float by = 300;
  
  koch(ax,ay,bx,by, 8*mouseX/width);
}

void koch(float ax,float ay,float bx,float by,float n){
  if(n == 0){
    line(ax,ay,bx,by);
  }
  else{
    float cx = ax + (bx-ax)/3.0;
    float cy = ay + (by-ay)/3.0;
    float dx = ax + 2.0*(bx-ax)/3.0;
    float dy = ay + 2.0*(by-ay)/3.0;
    float ex = ((dx-cx)*cos(-PI/3)-(dy-cy)*sin(-PI/3))+cx;
    float ey = ((dx-cx)*sin(-PI/3)+(dy-cy)*cos(-PI/3))+cy;
    koch(ax,ay,cx,cy,n-1);
    koch(cx,cy,ex,ey,n-1);
    koch(ex,ey,dx,dy,n-1);
    koch(dx,dy,bx,by,n-1);
  }
}
