from . import Deserializable
from .user import User


class Poll(Deserializable):
    def __init__(self, id, question, options, total_voter_count, is_closed, is_anonymous, type,
                 allows_multiple_answers, correct_option_id, explanation, explanation_entities, open_period,
                 close_date):
        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        id: str = raw_data.get('id')
        question: str = raw_data.get('question')
        options: list = raw_data.get('options')
        total_voter_count: int = raw_data.get('total_voter_count')
        is_closed: bool = raw_data.get('is_closed')
        is_anonymous: bool = raw_data.get('is_anonymous')
        type: str = raw_data.get('type')
        allows_multiple_answers: bool = raw_data.get('allows_multiple_answers')
        correct_option_id: int = raw_data.get('correct_option_id')
        explanation: str = raw_data.get('explanation')
        explanation_entities: list = raw_data.get('explanation_entities')
        open_period: int = raw_data.get('open_period')
        close_date: int = raw_data.get('close_date')
        return Poll(id, question, options, total_voter_count, is_closed, is_anonymous, type, allows_multiple_answers,
                    correct_option_id, explanation, explanation_entities, open_period, close_date)


class PollOption(Deserializable):
    __slots__ = ('poll_id', 'user', 'option_ids')

    def __init__(self, poll_id, user, option_ids):
        self.poll_id = poll_id
        self.user = user
        self.option_ids = option_ids

    @classmethod
    def de_json(cls, raw_data):
        raw_data = cls.check_json(raw_data)

        poll_id: str = raw_data.get('poll_id')
        user: User = raw_data.get('user')
        option_ids: list[int] = raw_data.get('option_ids')
        return PollOption(poll_id, user, option_ids)