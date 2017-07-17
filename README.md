Amazon SQS
===========

Allows sending and receiving of messages using Amazon SQS

Amazon SQS Send Message
===========

Properties
--------------

**queue_url**(string): URL specifiying which SQS queue to connect to

**aws_access_key_id**(string): AWS Access Key

**aws_secret_access_key**(string): AWS Secret Access Key

**message_body**(string): Content of message to send

**delay_seconds**(integer): Seconds before message is availalbe for processing (0-900)

**message_attributes**(object): Structured meta data items (e.g. timestamps, geospatial data,signatures)

Dependencies
----------------
boto3

Commands
----------------
None

Input
-------
Any list of signals containing data for property assignments

Output
---------
A response object from AWS containing the message ID


Amazon SQS Receive Message
===========

Properties
--------------

**queue_url**(string): URL specifiying which SQS queue to connect to

**aws_access_key_id**(string): AWS Access Key

**aws_secret_access_key**(string): AWS Secret Access Key

**attribute_names**(list): Attributes that need to be returned with each message.  See AWS documentation for list of possibilities

**message_attribute_names**(list): Message Attributes that need to be returned with each message.

**max_number_of_messages**(integer): Max number of messages to return (1 to 10)

**visibility_timeout**(integer): Duration (in seconds) that received messages are hidden from subsequent retrieve requests after being retrieved

**wait_time_seconds**(integer): Duration (in seconds) for which the call waits for a message to arrive in the queue before returning

**receive_request_attempt_id**(string): *Only applies to FIFO queues*; If a network issues causes a generic error, use this ID to retrieve the same set of messages

Dependencies
----------------
boto3

Commands
----------------
None

Input
-------
Any list of signals containing data for property assignments

Output
---------
Signal of the requested message.