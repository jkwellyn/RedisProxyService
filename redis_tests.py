#!/usr/bin/env python3

import proxy_service as redisproxy
from concurrencytest import ConcurrentTestSuite, fork_for_tests
import threading
import time
import unittest

def test_threading(test_app, key):
    time.sleep(1)
    test_app.get(key)

class ProxyServiceTestCase(unittest.TestCase):

    def setUp(self):
        app = redisproxy
        self.app = app
        self.cache = app.cached
        self.db = redisproxy.db

    def tearDown(self):
        self.db.flushall()
        self.app = None
        self.cache = None

    def test_get_config(self):
        self.assertEqual(redisproxy.app.config['REDIS_HOST'], 'localhost')
        self.assertEqual(redisproxy.app.config['REDIS_PORT'], 6379)
        self.assertEqual(redisproxy.app.config['REDIS_DB'], 0)
        self.assertEqual(redisproxy.app.config['CAPACITY'], 10)
        self.assertEqual(redisproxy.app.config['TTL'], 360)

    def test_get_call(self):
        id = '1'
        name = 'test-user'
        self.app.post(id, name)
        result = self.app.get('1')
        self.assertIn(result, name)

    def test_routes_cached(self):
        key = '2'
        name = 'test-user2'
        self.assertTrue(self.cache.get(key) is None)
        self.app.post(key, name)
        self.app.get(key)
        self.assertTrue(self.cache.get(key) is not None)

    def test_threading(self):
        for i in range(10):
            threading.Thread(target=test_threading(test_app=self.app, key='3')).start()
        x = threading.active_count()
        print (x)
