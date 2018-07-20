#include <stdio.h>
#include <stdlib.h>

int main(){
  FILE *IMAGE;
  IMAGE = fopen("image.ppm", "w");

  int i, r, g, b;


  fprintf(IMAGE, "P3\n500 500\n255\n");
  for(i=0; i<250000; i++){
    r = rand() % 255;
    g = rand() % 255;
    b = rand() % 255;
    fprintf(IMAGE, "%d %d %d\n", r, g, b);
  }

  fclose(IMAGE);

  return 0;
}
