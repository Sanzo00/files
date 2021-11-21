/*
  author: Sanzo00
  github: github.com/Sanzo00
  date:   2021-11-21 21:35
*/

#include <iostream>
#include <fstream>
#include <unordered_set>
#include <vector>
#include <sstream>

const int N = 10000000;

int main(int argc, char** argv) {
  
  if (argc < 3) {
    std::cout << "Usage: " << argv[0] << " input output." << std::endl;
    exit(-1);
  }

//  struct edge {
//    int u, v, c;
//  };

  std::ifstream input(argv[1], std::ios::in);
  if (!input.is_open()) {
    std::cout << "input file " << argv[1] << " open failed!" << std::endl;
    exit(-1);
  }

  std::ofstream output(argv[2], std::ios::out);
  if (!output.is_open()) {
    std::cout << "output file " << argv[2] << " open failed!" << std::endl;
    exit(-1);
  }
  
  // stat the graph data
  int max_node = 0;
  int edge_count = 0;
  int step = 5000000;

  std::string line;
  std::vector<std::unordered_set<int> > G(N);
  int cnt_edge = 0;
  while (getline(input, line)) {
    cnt_edge++;
    std::stringstream ss(line);
    int u, v;
    ss >> u >> v;
    if (u >= N || v >= N) {
      std::cout << "node large than N!" << std::endl;
      exit(-1);
    }
    G[u].insert(v);
    G[v].insert(u);
  }

  int cnt_node = 0;
  for (int i = 0; i < N; ++i) {
    if (!G[i].empty()) {
      cnt_node++;
      // add self-loop
      G[i].insert(i);
    }
  }

  std::cout << "old graph: " << cnt_node << " nodes " << cnt_edge << " edges" << std::endl; 

  cnt_node = 0;
  cnt_edge = 0;
  for (int i = 0; i < N; ++i) {
    if (G[i].empty()) {
      continue;
    }
    cnt_node++;
    for (auto& it : G[i]) {
      cnt_edge++;
      output << i << " " << it << std::endl;
    }
  }

  std::cout << "processed graph: " << cnt_node << " nodes " << cnt_edge << " edges" << std::endl; 

  input.close();
  output.close();
  
  return 0;
}
