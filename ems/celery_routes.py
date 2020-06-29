from kombu import Queue, Exchange

TASK_QUEUES = ([
    Queue('ems-search', Exchange('ems-search'), routing_key='ems-search')
])

TASK_ROUTES = {
    'entity.tasks.index_entity':{
        'queue': 'ems-search',
        'routing_key': 'ems-search',
        'exchange': 'ems-search'
    },
}