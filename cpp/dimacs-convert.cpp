/*
  author: Sanzo00
  github: github.com/Sanzo00
  http://www.diag.uniroma1.it//~challenge9/download.shtml
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

int main(int argc, char** argv) {
  
  if (argc < 3) {
    std::cout << "Usage: " << argv[0] << " input output." << std::endl;
    exit(-1);
  }

  struct edge {
    int u, v, c;
  };

  std::vector<edge> edges;

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
  char c;
  edge t;
  while (getline(input, line)) {
    std::stringstream ss(line);
    char c;
    ss >> c;
    if (c == 'a') {
      ss >> t.u >> t.v >> t.c;
      edges.push_back(t);
      max_node = std::max(std::max(t.u, t.v), max_node);
      edge_count++;
     // std::cout << t.u << " " << t.v << " " << t.c << std::endl;
    }

    // if (edge_count == 10) {
    //   break;
    // }
    
    while (edges.size() == step) {
      for (auto edge : edges) {
        output << edge.u << " " << edge.v << " " << edge.c << std::endl;
      }
      edges.clear();
      std::cout << edge_count << " edges have writed to " << argv[2] << std::endl;
    }
  }

  if (!edges.empty()) {
    for (auto edge : edges) {
      output << edge.u << " " << edge.v << " " << edge.c << std::endl;
    }
    edges.clear();
  }

  std::cout << "max node number: " << max_node << " total edges: " << edge_count << std::endl;

  input.close();
  output.close();
  
  return 0;
}
