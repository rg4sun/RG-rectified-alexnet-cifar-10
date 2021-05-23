import json
import sys

import alluxio
from alluxio import option


test_dir = '/test-py'
client = alluxio.Client('10.89.127.142', 39999)
opt = option.CreateDirectory(recursive=True)
client.create_directory(test_dir, opt)
print('test-py created!')