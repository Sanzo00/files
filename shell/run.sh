cd ..
make -j4 || exit 1

cd tests

# ps -ef | grep test_ | grep -v grep | awk  '{print $2}' | xargs kill -9
out=$(ps -ef | grep test_ | grep -v grep | awk  '{print $2}')

# if [ ! $out ]; then
if test -z $out; then
  echo "all thread is already cleared!"
else
  for tid in $out
  do
    echo "kill $tid"
    kill -9 $tid
  done
fi


./local.sh 1 1 ./test_example
# ./local.sh 1 1 ./test_simple_app
# ./local.sh 1 1 ./test_kv_app
# ./local.sh 1 1 ./test_kv_app_benchmark
# ./local_multi_workers.sh 1 20 ./test_kv_app_multi_workers
