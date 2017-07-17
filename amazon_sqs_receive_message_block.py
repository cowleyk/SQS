from nio.util.discovery import discoverable
from nio.properties import StringProperty, IntProperty, ListProperty
from .amazon_sqs_base_block import SQSBase


@discoverable
class SQSReceiveMessage(SQSBase):
    """Send message over Amazon SQS
        User needs to specify a queue url and message body
        If specifying a message attribute,
        it must include a name, type, and value"""

    attribute_names = ListProperty(
        title="Attributes Returned with each Message",
        default=[],
        allow_none=True
    )
    # ^ AWS has defined possibilies here, should it just be text input?
    message_attribute_names = ListProperty(
        title="Message Attribute to Return", default=[{}, {}], allow_none=True)
    max_number_of_messages = IntProperty(
        title="Max Number Messages to Receive", default=1, allow_none=True)
    visibility_timeout = IntProperty(
        title="Visibility Timeout", default=0, allow_none=True)
    wait_time_seconds = IntProperty(
        title="Time to wait for messages", default=10, allow_none=True)
    receive_request_attempt_id = StringProperty(
        title="ID to attempt retry", default="", allow_none=True)
        # ^ FIFO queues only

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            try:
                self.logger.debug("Receiving message via {} queue".format(
                    self.queue_url(signal)))
                response = self.client.receive_message(
                    QueueUrl=self.queue_url(signal),
                    AttributeNames=self.attribute_names(signal),
                    MessageAttributeNames=self.message_attribute_names(signal),
                    MaxNumberOfMessages=self.max_number_of_messages(signal),
                    VisibilityTimeout= self.visibility_timeout(signal),
                    WaitTimeSeconds= self.wait_time_seconds(signal),
                    ReceiveRequestAttemptId= self.receive_request_attempt_id(signal)
                )
                new_signals.append(response)

            except:
                self.logger.exception("Message was not received")

        self.notify_signals(new_signals)


    # response = {
    #     'Messages': [
    #         {
    #             'MessageId': 'string',
    #             'ReceiptHandle': 'string',
    #             'MD5OfBody': 'string',
    #             'Body': 'string',
    #             'Attributes': {
    #                 'string': 'string'
    #             },
    #             'MD5OfMessageAttributes': 'string',
    #             'MessageAttributes': {
    #                 'string': {
    #                     'StringValue': 'string',
    #                     'BinaryValue': b'bytes',
    #                     'StringListValues': [
    #                         'string',
    #                     ],
    #                     'BinaryListValues': [
    #                         b'bytes',
    #                     ],
    #                     'DataType': 'string'
    #                 }
    #             }
    #         },
    #     ]
    # }
