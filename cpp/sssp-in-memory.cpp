/*
  author: Sanzo00
  github: github.com/Sanzo00
  road network: https://snap.stanford.edu/data/roadNet-CA.html
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <climits>
#include <cassert>
#include <unordered_map>
#include <queue>
using namespace std;

typedef int nodeTy;
typedef long long edgeTy;
const int inf = INT_MAX;

void readGraph(string filename, vector<int> &nodeDeg, vector<nodeTy> &edgeDst,
               vector<edgeTy> &edgeData, nodeTy &maxNode, int &numEdges) {
  ios::sync_with_stdio(false);
  // open file
  ifstream in(filename, ios::in);
  if (!in.is_open()) {
    cout << filename << " open fail!" << endl;
    exit(1);
  }

  nodeTy u, v;
  istringstream iss;
  string line;

  // get maxNum
  while (getline(in, line)) {
    if (line[0] != '#') {
      iss.clear();
      iss.str(line);
      iss >> u >> v;
      maxNode = max(maxNode, u);
      maxNode = max(maxNode, v);
    }
  }

  nodeDeg.resize(maxNode + 1, 0);
  in.clear();
  in.seekg(0, in.beg);
  // get degree
  while (getline(in, line)) {
    if (line[0] != '#') {
      iss.clear();
      iss.str(line);
      iss >> u >> v;
      nodeDeg[u]++;

      // Undirected
      // nodeDeg[v]++;
    }
  }
  for (int i = 1; i <= maxNode; ++i) {
    nodeDeg[i] += nodeDeg[i - 1];
  }
  numEdges = nodeDeg[maxNode];
  assert(numEdges > 0);

  in.clear();
  in.seekg(0, in.beg);
  edgeDst.resize(numEdges, 0);
  edgeData.resize(numEdges, 0);

  vector<nodeTy> start(maxNode + 1, 0);

  // get edgedst, edgedata
  while (getline(in, line)) {
    if (line[0] != '#') {
      iss.clear();
      iss.str(line);
      iss >> u >> v;
      int idx = u ? nodeDeg[u - 1] : 0;
      idx += start[u]++;
      edgeDst[idx] = v;
      iss >> edgeData[idx];
      // edgeData[idx] = 1;

      // Undirected
      // idx = v ? nodeDeg[v - 1] : 0;
      // idx += start[v]++;
      // edgeDst[idx] = u;
      // edgeData[idx] = 1;
    }
  }
  assert(start[maxNode] + nodeDeg[maxNode - 1] == nodeDeg[maxNode]);
  in.close();
}

void sssp(nodeTy src, nodeTy maxNode, vector<edgeTy> &dis, vector<bool> &vis,
       vector<int> &nodeDeg, vector<nodeTy> &edgeDst, vector<edgeTy> &edgeData) {

  dis[src] = 0;
  struct edge{
    nodeTy u;
    edgeTy c;
    bool operator < (const edge &x) const{
      return x.c < c;
    }
  };
  priority_queue<edge> que;

  que.push({src, 0});
  while (!que.empty()) {
    auto f = que.top();
    que.pop();
    nodeTy u = f.u;
    edgeTy c = f.c;
    if (vis[u]) {
      continue;
    }
    vis[u] = true;
    int idx = u ? nodeDeg[u - 1] : 0;
    while (idx < nodeDeg[u]) {
      nodeTy v = edgeDst[idx];
      if (!vis[v] && c + edgeData[idx] < dis[v]) {
        dis[v] = c + edgeData[idx];
        que.push({v, dis[v]});
      }
      idx++;
    }
  }
}

int main(int argc, char** argv) {
  if (argc < 3) {
    cout << "Usage: " << argv[0] << " input src" << endl;
    exit(-1);
  }

  string filename(argv[1]);
  nodeTy src = atoi(argv[2]);
  cout << "filename: " << filename << endl;
  cout << "src: " << src << endl;

  unordered_map<nodeTy, nodeTy> nodes;
  nodeTy maxNode = 0;
  int numEdges = 0;
  vector<int> nodeDeg;
  vector<nodeTy> edgeDst;
  vector<edgeTy> edgeData;

  readGraph(filename, nodeDeg, edgeDst, edgeData, maxNode, numEdges);
  cout << "maxNode: " << maxNode << endl;
  cout << "numEdges: " << numEdges << endl;
  if (numEdges == 0) {
    cout << "graph is empty!" << endl;
    exit(1);
  }

  vector<edgeTy> dis(maxNode + 1, inf);
  vector<bool> vis(maxNode + 1, false);
  sssp(src, maxNode, dis, vis, nodeDeg, edgeDst, edgeData);

  // print dis[100 - 120]
  cout << endl << "dis[100 - 120]" << endl;
  for (int i = 100; i < 120; ++i) {
    cout << dis[i] << " ";
  } cout << endl;

  return 0;
}
