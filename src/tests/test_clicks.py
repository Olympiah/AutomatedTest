import pytest
from clicks.LikeButton import LikeState, click_many


def test_empty_click():
    assert click_many(LikeState.empty, '') is LikeState.empty


def test_single_click():
    assert click_many(LikeState.empty, 'l') is LikeState.liked
    assert click_many(LikeState.empty, 'd') is LikeState.disliked


@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
])

def test_multi_clicks(test_input, expected):
    assert click_many(LikeState.empty, test_input) is expected

# def test_click():
#     assert click_many(LikeState.empty, '') is LikeState.empty
#     assert click_many(LikeState.empty, 'l') is LikeState.liked
#     assert click_many(LikeState.empty, 'd') is LikeState.disliked
#     assert click_many(LikeState.empty, 'll') is LikeState.empty
#     assert click_many(LikeState.empty, 'dd') is LikeState.empty
#     assert click_many(LikeState.empty, 'ld') is LikeState.disliked
#     assert click_many(LikeState.empty, 'dl') is LikeState.liked
#     assert click_many(LikeState.empty, 'ldd') is LikeState.empty
#     assert click_many(LikeState.empty, 'lldd') is LikeState.empty
#     assert click_many(LikeState.empty, 'ddl') is LikeState.liked

# to skip
# @pytest.mark.skip(reason="....")

# to avoid a test that is an obvious fail from failing(b4 test you put that)
# @pytest.mark.xfail