# RatelNet

Middleware hub to apply different security tools to different user messages or files that are catched from different data channels implemented in plugins.


# Scanners

## Ratel DLP (Data Loss Protection)


# Data channels

## Slack


# Plan

As I don't know how much time I have devote to this task, I decided to start with initial plan describing my vision about the application in the form of TODO list:

- setup slack app with files:read permission (to be extended later with all kind of messsages)

- ratel -- core app:
    - test dealing with messages in/out with dummy tasks Manager (implement __get_messages to be read from memory)
    - Slack data channel plugin (at this stage I would use well splitted monolith for data channels, and microservices for scanners)
        - add webhook to catch messages; manual test

- DPL as separate app -- this should serve API we can pass messages from different sources
    - I decided to keep db and admin panel ect. on the DPL side instead of core app because it is simpler and fits SRP rule for now. RatelNet core should know only about tasks and there results. Those result (DTOs) could be saved in the internal db in the future as well for the purpose of sharing data between different scaners, or applying different scanning policies but for now it will deal with pure tasks only
    - data models
        - model FileMessage (id, channel, content, leak: bool)   # to be extended with sender and receiver, date later
        - model RegexPattern (id, label, content)
    - implement the check: maching regex patterns
    - manage patterns via django admin (add, remove, view)
    - store catched messages with pattern id
    - view catched messages with pattern label

- add docker-compose:
   - ratelnet (main app with tasks management and data source plugins)
   - SQS instance
   - DLP
       - mysql instance

- (bonus) extend to all slack messages
    - listen to all messages using channels:history, groups:history, im:history, and mpim:history scopes
    - new DLP model: TextMessage model and rethink models hierarchy
    - Slack plugin public method: delete() for the original message: if the message contains leak we can use chat:write:user or chat:write:bot (?) to delete the original message using the chat.delete method
    - strucure different "policies" in slack app to handle negative checks:
        - watch_only
        - delete (with a notice)
        - redact (extention: original message but with redacted sensitive data `***`)
