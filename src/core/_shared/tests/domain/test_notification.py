from src.core._shared.domain.notification import Notification
class TestNotification:
    def test_append_notification(self):
        notification = Notification()
        notification.add_error('error 1')
        notification.add_error('error 2')
        assert notification.messages == 'error 1,error 2'

    