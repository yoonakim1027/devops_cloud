from django.contrib.auth.mixins import UserPassesTestMixin


class ReviewUserCheckMixin(UserPassesTestMixin):
    # class 문법을 제대로 많이 알아야 할 수 있는 것...
    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user