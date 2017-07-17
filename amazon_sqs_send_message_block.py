from nio.util.discovery import discoverable
from nio.properties import (StringProperty, IntProperty, Property,
                            PropertyHolder, ObjectProperty, ListProperty)
from .amazon_sqs_base_block import SQSBase


class MessageAttributes(PropertyHolder):
    attribute_name = Property(
        title="Message Attribute Name", default="Attr Name", allow_none=False)
    attribute_type = Property(
        title="Message Attribute Type", default="Attr Name", allow_none=False)
    attribute_value = Property(
        title="Message Attribute Value", default="Attr Name", allow_none=False)


@discoverable
class SQSSendMessage(SQSBase):
    """Send message over Amazon SQS
        User needs to specify a queue url and message body
        If specifying a message attribute,
        it must include a name, type, and value"""

    message_body = StringProperty(
        title="Message Body", default="Hello Mr. SQS", allow_none=False)
    delay_seconds = IntProperty(
        title="Delay sending message", default=0, allow_none=True)
    message_attributes = ListProperty(MessageAttributes,
                                        title="Message Attributes",
                                        default=MessageAttributes(),
                                        allow_none=True)

    # ^ message_attributes are not required, but if used, they need a name/type/value
    # did I configure this correctly?
    # It needs to be able to add multiple attributes
        # TODO: MAKE 'ADD' BUTTON LIKE IN DYNAMIC FIELDS BLOCK
    # Should this block include batch sending of messages

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            print('@@@@@@@@@@@', self.message_attributes(signal).to_dict())
            try:
                self.logger.debug("Sending message via {} queue".format(
                    self.queue_url(signal)))

                response = self.client.send_message(
                    QueueUrl=self.queue_url(signal),
                    DelaySeconds=self.delay_seconds(signal),
                    MessageAttributes=self.message_attributes(signal),
                    MessageBody=self.message_body(signal)
                )
                new_signals.append(response)

            except:
                self.logger.exception("Message failed to send")

        self.notify_signals(new_signals)


    # response = {
    #     'MD5OfMessageBody': 'string',
    #     'MD5OfMessageAttributes': 'string',
    #     'MessageId': 'string',
    #     'SequenceNumber': 'string'
    # }