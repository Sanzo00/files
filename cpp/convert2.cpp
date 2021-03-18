#include <stdio.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>

bool file_exist(char *filename) {
  struct stat st;
  return stat(filename, &st) == 0;
}

int main(int argc, char **argv) {
  if (argc < 4) {
    printf("Usage: ./convert path isZeroIndex EdgeData\n");
    printf("path: file path need to be convert to binary file.\n");
    printf("isZeroIndex: does the vertex number start from 0.\n");
    printf("EdgeData: is there edge data.\n");
    exit(-1);
  }

  char *filename = argv[1];
  if (!file_exist(filename)) {
    printf("file not exist!\n");
    exit(-1);
  }
  bool isZeroIndex = atoi(argv[2]);
  bool EdgeData = atoi(argv[3]);
  printf("filename: %s, isZeroIndex: %d, EdgeData: %d\n", filename, isZeroIndex, EdgeData);

  FILE *in = fopen(filename, "r");
  if (in == NULL) {
    printf("file %s open error!\n", filename);
    exit(-1);
  }

  char str[256];
  strcpy(str, filename);
  strcat(str, ".bin");
  FILE *out = fopen(str, "wb");
  if (out == NULL) {
    printf("file %s open error!\n", str);
    exit(-1);
  }
  printf("%s\n", str);

  int N, M;
  fscanf(in, "%d\t%d", &N, &M);
  printf("Vertex: %d, Edge: %d\n", N, M);

  int u, v, c;
  for (int i = 0; i < M; ++i) {
    fscanf(in, "%d\t%d", &u, &v);
    if (isZeroIndex) {
      u--;
      v--;
    }
    fwrite(&u, sizeof(u), 1, out);
    fwrite(&v, sizeof(v), 1, out);
    // printf("%d -> %d", u, v);
    if (EdgeData) {
      fscanf(in, "\t%d", &c);
      fwrite(&c, sizeof(c), 1, out);
      // printf(", c: %d", c);
    }
    // printf("\n");
  }

  printf("convert is done!\n");

  fclose(in);
  fclose(out);

  return 0;
}