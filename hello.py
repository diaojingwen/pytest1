import allure
import  pytest
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


class Testa:
    def test_demo_1(self):
        assert inc(1) == 3

    def test_demo_2(self):
        assert not inc(2) != 4

    @pytest.mark.parameterize("data,expect",[
            (1,2),
            (3,4),
            (10.11),
            (14,17)
    ])

    def test_data(self,data,expect):
        allure.attach("this is test",attachment_type=allure.attachment_type.TEXT)
        allure.attach('<img src="https://img-blog.csdnimg.cn/2020102316024217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzYyMTkx,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">',
                      attachment_type=allure.attachment_type.HTML)
        assert inc(data) == expect


    def teardown(self):
        print("teardown")