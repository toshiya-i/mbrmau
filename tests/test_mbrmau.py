# -*- coding: utf-8 -*-

import sys
import textwrap
import mbrmau


def test_mbrau(capsys, monkeypatch):
    testargs = ["prog", "2016", "12"]
    monkeypatch.setattr(sys, 'argv', testargs)

    mbrmau.main()

    out, err = capsys.readouterr()
    message = """    hoge
    2016/12/1 begin end
    2016/12/2 begin end
    2016/12/5 begin end
    2016/12/6 begin end
    2016/12/7 begin end
    2016/12/8 begin end
    2016/12/9 begin end
    2016/12/12 begin end
    2016/12/13 begin end
    2016/12/14 begin end
    2016/12/15 begin end
    2016/12/16 begin end
    2016/12/19 begin end
    2016/12/20 begin end
    2016/12/21 begin end
    2016/12/22 begin end
    2016/12/23 begin end
    2016/12/26 begin end
    2016/12/27 begin end
    2016/12/28 begin end
    2016/12/29 begin end
    2016/12/30 begin end
    piyo
    """
    assert out == textwrap.dedent(message)
