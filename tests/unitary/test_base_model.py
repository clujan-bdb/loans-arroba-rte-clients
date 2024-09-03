import init  # noqa: F401
from unittest import TestCase
from unittest.mock import patch, MagicMock, call
from app.core.models.base import BaseModel


class TestBaseModel(TestCase):
    def setUp(self):
        class TestModel(BaseModel):
            name: str
            number: int

        self.model = TestModel

    @patch('app.core.models.base.datetime')
    @patch('app.core.models.base.uuid4')
    def test_instance_model_success(
        self, mock_uuid4: MagicMock, mock_datetime: MagicMock
    ):
        mock_uuid4.return_value = '123e4567-e89b-12d3-a456-426614174000'
        mock_datetime.now.return_value = '2021-01-01 00:00:00'

        instance = self.model(
            name='el pepito',
            number=1,
        )
        mock_uuid4.assert_called_once_with()
        assert mock_datetime.now.call_args_list == [call(), call(),]
        assert instance.name == 'el pepito'
        assert instance.number == 1
        assert instance.uid == '123e4567-e89b-12d3-a456-426614174000'
        assert instance.active is True
        assert instance.created_at == '2021-01-01 00:00:00'
        assert instance.updated_at == '2021-01-01 00:00:00'

    def test_instance_model_fail(self):
        expected = (
            "Field required [type=missing, input_value="
            "{'name': 'el pepito'}, input_type=dict]"
        )
        with self.assertRaises(ValueError) as error:
            self.model(
                name='el pepito',
            )
        assert expected in str(error.exception)

    def test_instance_model_overriding_default(self):
        # TODO: implement test case
        ...

    def test_update_instance_success(self):
        # TODO: implement test case
        ...

    def test_update_instance_fail(self):
        # TODO: implement test case
        ...
