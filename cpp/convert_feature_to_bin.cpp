#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

typedef float FeatType;
const int N = 1000000;
int main(int argc, char** argv) {

  if (argc < 3) {
    std::cout << "Usage: ./a.out input output" << std::endl;
    exit(-1);
  }

  std::cout << "input: " << argv[1] << std::endl;
  std::cout << "output: " << argv[2] << std::endl;

  std::ifstream in(argv[1]);
  std::ofstream out(argv[2], std::ios::binary);

  if (in.is_open() == false) {
    std::cout << argv[1] << " open fail!" << std::endl;
    exit(-1);
  }

  if (out.is_open() == false) {
    std::cout << argv[2] << " open fail!" << std::endl;
    exit(-1);
  }

  std::string line;
  std::vector<FeatType> buffer(N);
  int now = 0;
  while (getline(in, line)) {
    int id;
    FeatType feat;
    std::stringstream feat_stream(line);
    feat_stream >> id;
    // std::cout << id << ": ";
    while (feat_stream >> feat) {
      // std::cout << feat << " ";
      buffer[now++] = feat;
      if (now == N) {
        for (int i = 0; i < now; ++i) {
          out.write((char*)&buffer[i], sizeof(buffer[i]));
        }
        now = 0;
      }
    }
    // std::cout << std::endl;
  }

  for (int i = 0; i < now; ++i) {
    // out << buffer[i];
    out.write((char*)&buffer[i], sizeof(buffer[i]));
  }
  now = 0;

  in.close();
  out.close();

  return 0;
}
