class TestTextTask:
    @classmethod
    def setup_class(cls):
        print("k")

    @classmethod
    def teardown_class(cls):
        print("e")

    def test_add(self):
        print("1111111")

    def test_del(self):
        print("222222")

