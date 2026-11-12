测试：python3 -m unittest discover -s tests/deliberation_cycles -p 'test_*.py'
构建：python3 -m compileall -q deliberation_lake tests/deliberation_cycles
验收：python3 -m deliberation_lake.console.run fixtures/demo.json --database /tmp/deliberation_lake-acceptance.sqlite3
所有输入均为本地合成数据，运行不需要网络。
