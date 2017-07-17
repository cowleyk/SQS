from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..amazon_sqs_send_message_block import SQSSendMessage
# from ..amazon_sqs_receive_message_block import SQSReceiveMessage


# CREDENTIALS
# queue_url: https://sqs.us-east-2.amazonaws.com/573416092345/KevinsQuirkyQueue
# access key id: AKIAJWODFLWHKXAEPKMA
# secret access key: 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

class TestSQS(NIOBlockTestCase):

    def test_send_message(self):
        """Signals ..."""
        blk = SQSSendMessage()
        self.configure_block(blk, {
            "message_body": "allo",
            "delay_seconds": 0,
            "message_attributes": {
                "attribute_name": "msgAttr",
                "attribute_type": "msgAttrType",
                "attribute_value": "msgAttrVal",
            },
        })

        blk.start()
        blk.process_signals([Signal({
            "message_body": "allo",
            "delay_seconds": 0,
            "message_attributes": {
                "attribute_name": "msgAttr",
                "attribute_type": "msgAttrType",
                "attribute_value": "msgAttrVal",
            },
        })])
        blk.stop()

        # Test 'assert_called_with'
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {
                'MD5OfMessageBody': 'string',
                'MD5OfMessageAttributes': 'string',
                'MessageId': 'string',
                'SequenceNumber': 'string'
            }
        )

    # def test_receive_message(self):
    #     """Signals ..."""
    #     blk = SQSReceiveMessage()
    #     self.configure_block(blk, {})
    #
    #     blk.start()
    #     blk.process_signals([Signal({"hello": "n.io"})])
    #     blk.stop()
    #
    #     # Test 'assert_called_with'
    #     self.assert_num_signals_notified(1)
    #     self.assertDictEqual(
    #         self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
    #         {
    #             'Messages': [
    #                 {
    #                     'MessageId': 'string',
    #                     'ReceiptHandle': 'string',
    #                     'MD5OfBody': 'string',
    #                     'Body': 'string',
    #                     'Attributes': {
    #                         'string': 'string'
    #                     },
    #                     'MD5OfMessageAttributes': 'string',
    #                     'MessageAttributes': {
    #                         'string': {
    #                             'StringValue': 'string',
    #                             'BinaryValue': b'bytes',
    #                             'StringListValues': [
    #                                 'string',
    #                             ],
    #                             'BinaryListValues': [
    #                                 b'bytes',
    #                             ],
    #                             'DataType': 'string'
    #                         },
    #                     }
    #                 },
    #             ]
    #         }
    #     )
