from . import Deserializable


class Poll(Deserializable):
    __slots__ = ('id', 'question', 'options', 'total_voter_count', 'is_closed', 'is_anonymous', 'type',
                 'allows_multiple_answers', 'correct_option_id', 'explanation', 'explanation_entities', 'open_period',
                 'close_date')

    def __init__(self, data, id, question, options, total_voter_count, is_closed, is_anonymous, type,
                 allows_multiple_answers, correct_option_id, explanation, explanation_entities, open_period,
                 close_date):
        self.data = data
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
    def de_json(cls, data):
        data = cls.check_json(data)

        id: str = data.get('id')
        question: str = data.get('question')
        options: list = data.get('options')
        total_voter_count: int = data.get('total_voter_count')
        is_closed: bool = data.get('is_closed')
        is_anonymous: bool = data.get('is_anonymous')
        type: str = data.get('type')
        allows_multiple_answers: bool = data.get('allows_multiple_answers')
        correct_option_id: int = data.get('correct_option_id')
        explanation: str = data.get('explanation')
        explanation_entities: list = data.get('explanation_entities')
        open_period: int = data.get('open_period')
        close_date: int = data.get('close_date')
        return Poll(data, id, question, options, total_voter_count, is_closed, is_anonymous, type,
                    allows_multiple_answers, correct_option_id, explanation, explanation_entities, open_period,
                    close_date)
